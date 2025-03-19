import tkinter as tk
from tkinter import scrolledtext, ttk, messagebox
import serial
import serial.tools.list_ports
import threading
import os
import sys
import time


bin_dir = os.path.dirname(os.path.abspath(__file__)) # bin directory path
sys.path.append(bin_dir) # Append bin directory to sys.path for module import
parent_dir = os.path.dirname(bin_dir) # Parent directory path
sys.path.append(parent_dir) # Append parent directory to sys.path for 'decoded' import

import decoded # Import 'decoded' from the parent directory
import msvcrt # For getch() in Windows, or use alternative for other OS

# Define tags for different colors
def create_tags():
    log_box.tag_configure("highlight", foreground="red")  # Highlight in red
    log_box.tag_configure("info", foreground="blue")  # Info in blue
    log_box.tag_configure("power", foreground="green")  # Power-related rows in green
    log_box.tag_configure("thermal", foreground="purple")  # Thermal-related rows in purple



def checksum(buf):
    return sum(buf.encode('utf-8')) & 0xFF

def send_command2(command):
    if uart:
        cmd_checksum = checksum(command)
        full_command = f'{command}:{cmd_checksum:02X}\n'
        uart.write(full_command.encode('utf-8'))
        #log_message(f"=====================", tag="info")
        #log_message(f"Sent: {full_command.strip()}")
        #log_message(f"=====================", tag="info")
    else:
        log_message("UART not connected")

def send_command(command):
    if uart:
        cmd_checksum = checksum(command)
        full_command = f'{command}:{cmd_checksum:02X}\n'
        uart.write(full_command.encode('utf-8'))
        log_message(f"=====================", tag="info")
        log_message(f"Sent: {full_command.strip()}")
        log_message(f"=====================", tag="info")
    else:
        log_message("UART not connected")

def receive_data():
    while uart and uart.is_open:
        try:
            data = uart.readline().decode('utf-8').strip()
            if data:
                log_message(f"Received: {data}")
                log_message(f"=====================", tag="info")
                decode_message(data)
        except Exception as e:
            log_message(f"Error: {e}")

import re

# Function to strip the checksum part (after the colon)
def strip_checksum(field):
    if ':' in field:
        return field.split(':')[0]  # Return everything before the colon
    return field  # If there's no colon, return the original field

# Function to check if a string is a valid hexadecimal value
def is_hex(value):
    # Check if the string only contains valid hexadecimal characters (0-9, A-F)
    return bool(re.match(r'^[0-9A-Fa-f]+$', value))

# Update your decode_message function to handle validation better
def decode_message(data):
    reply_data = data

    # Split the received data into fields using space as a delimiter
    fields = data.split()

    

    # Ensure you have enough fields to unpack into the corresponding variables
    if len(fields) >= 9:
        # Extract each piece of information from the fields
        ack = fields[0]  # 'OK'
        ack_data = fields[1]  # '00000000'
        err_code = fields[2]  # '80000009'
        rtc = fields[3]  # 'FFFFFFFF'
        power_state = fields[4] if len(fields) > 4 else None  # '00FF0042', optional
        upcause = fields[5]  # '00000000'
        psq = fields[6]  # '217C'
        devpm = fields[7]  # '0000'
        tsoc = fields[8]  # 'FFFF'
        tenv = fields[9] if len(fields) > 9 else "Unknown"  # 'FFFF' (optional)
        checksum = fields[-1] if len(fields) > 9 else "Unknown"  # 'FA' (last field)

        # Strip the checksum part (anything after ':')
        tenv = strip_checksum(tenv)  # Strip checksum from tenv

        if not is_hex(err_code):
            log_message(f"Invalid err_code: {err_code}")
            return

        if not is_hex(rtc):
            log_message(f"Invalid RTC: {rtc}")
            return

        # Check if power_state exists and is valid before processing
        if power_state and not is_hex(power_state):
            log_message(f"Invalid Power State: {power_state}")
            return

        if not is_hex(upcause):
            log_message(f"Invalid Wake Cause: {upcause}")
            return

        if not is_hex(psq):
            log_message(f"Invalid PSQ: {psq}")
            return

        if not is_hex(devpm):
            log_message(f"Invalid DevPower: {devpm}")
            return

        if not is_hex(tsoc):
            log_message(f"Invalid TSOC: {tsoc}")
            return

        if not is_hex(tenv):
            log_message(f"Invalid TEnv: {tenv}")
            return

        # Decode each field
        error = decoded.err_code(err_code)
        rtc = format_rtc_field(rtc)

        # Only decode power_state if it's present and valid
        if power_state:
            power_state_msg = decoded.pw_state(power_state).strip()
        else:
            power_state_msg = "No Power State"

        wake_cause = decoded.upcause(upcause)
        dev_pwr = decoded.devpower(power_state) if power_state else "Unknown DevPower"
        PSQ = decoded.psq(psq)
        tsoc_temp = calculate_temp(tsoc)
        tenv_temp = calculate_temp(tenv)

        # Format the decoded data
        formatted_data = ( 
            f" {ack:<13} Code    Rtc    PowState UpCause  SeqNo  DevPm  T(SoC)  T(Env)\n"  
            f"{reply_data}\n\n" 
            f"" 
            f"     {fields[2]}          =     {error:<17}\n"  
            f"     Time              =     {rtc:<12}\n"  
            f"     Power State       =     {power_state_msg:<16}\n" 
            f"     Wake Cause        =     {wake_cause:<8}\n\n"
            f"     Power Sequence    =     {PSQ}\n"
            f"     DevPower          =     {dev_pwr}\n\n"  
            f"     Thermal\n"   
            f"     Temperature:     SOC: {tsoc_temp:<7}  Env: {tenv_temp}\n"
        )

        log_message(f"Decoded:\n{formatted_data}", tag="info")
        log_message(f"Error Code:           {err_code} = {error}", tag="highlight")
        log_message(f"Power Sequence:       {psq}      = {PSQ}", tag="power")
        log_message(f"Thermal data: =       SOC:{tsoc}     ENV: {tenv}", tag="thermal")







def calculate_temp(hex_value):
    temp_value = int(hex_value, 16)
    temp_celsius = temp_value / 256.0
    return f"{temp_celsius:.2f}°C"

import datetime

TIME_ZERO = 1325376000  # Reference point for timestamp calculation

def format_rtc_field(rtc_field):
    """Format the RTC/TIME field to a human-readable timestamp or calculated value."""
    try:
        # Assuming the RTC field is in 'YYYY/MM/DD HH:MM:SS' format
        time = datetime.datetime.strptime(rtc_field + '+00:00', '%Y/%m/%d %H:%M:%S%z')
        unix_timestamp = int(time.timestamp() - TIME_ZERO)
        return f"{unix_timestamp} ({rtc_field})"  # Show both the timestamp and original field
    except ValueError:
        return "Invalid RTC Field (FF:FF:FF)"
    
# Function to log message with tag (this version handles the tag argument)
def log_message(message, tag=None):
    log_box.config(state='normal')
    if tag:
        log_box.insert(tk.END, message + "\n", tag)  # Apply tag for color
    else:
        log_box.insert(tk.END, message + "\n")
    log_box.see(tk.END)
    log_box.config(state='disabled')

def list_ports():
    ports = serial.tools.list_ports.comports()
    return [(port.device, port.description) for port in ports]

def refresh_ports():
    # List all available ports and update the drop-down
    ports = list_ports()
    
    # Create a list of strings with both device and description
    port_strings = [f"{p[0]} - {p[1]}" for p in ports]
    
    # Update the combo box with both port device and description
    port_menu['values'] = port_strings
    
    # Set the default value to the first available port with description
    if ports:
        port_var.set(port_strings[0])  # Set the first port device + description as the default value
    else:
        port_var.set('')  # If no ports are available, clear the default value



import time
# Global variables
uart = None
is_connected = False  # Flag to track connection status
root = None  # We will create a new root window when reopening the GUI

def connect_uart():
    global uart, is_connected

    selected = port_var.get()  # Get the full string (port device + description)
    port_device = selected.split(' ')[0]  # Extract the port device (e.g., COM1)
    description = ' '.join(selected.split(' ')[1:])  # Get the full description (e.g., Prolific USB-to-Serial)

    # Disable the connect button while trying to connect or disconnect
    connect_button.config(state='disabled')

    if is_connected:
        # If already connected, disconnect first
        try:
            if uart and uart.is_open:
                restart_gui()
                log_message(f"Disconnected from {uart.name}")  # Display the port that was disconnected
                is_connected = False
                connect_button.config(text="Connect")  # Change button text to 'Connect'
                uart = None  # Dereference the UART object after closing
            else:
                log_message("UART connection is already closed.")
                is_connected = False
                connect_button.config(text="Connect")  # Change button text to 'Connect'
        except Exception as e:
            log_message(f"Error while closing UART: {str(e)}")  # Log any error that happens during close
            connect_button.config(state='normal')  # Enable the button if disconnecting fails
            return

    else:
        # Wait a small moment to ensure the port is released by the system
        time.sleep(0.1)

        # Try to establish a new UART connection
        try:
            uart = serial.Serial(port_device, 115200, timeout=1)  # Use the port device for connection
            send_command2("version")
            log_message(f"Connected to {port_device} ({description})")  # Display both port and description
            is_connected = True
            connect_button.config(text="Close Connection (Exit)")  # Change button text to 'Disconnect'
            threading.Thread(target=receive_data, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Connection Error", str(e))

    connect_button.config(state='normal')  # Re-enable the button after the operation

def restart_gui():
    # Quit the current instance of the GUI
    root.quit()


def send_errlog(level):
    send_command(f"errlog {level}")

def send_errlog_all(num_logs):
    # Sends errlog from 0 to num_logs-1 in hex (0, 1, 2, ..., num_logs-1)
    for i in range(num_logs):
        time.sleep(0.1)  # Wait for a short time before sending the next command
        send_command(f"errlog {hex(i)[2:].upper()}")  # Send in hexadecimal format
        #log_message(f"Sent: errlog {hex(i)[2:].upper()}")  # Log the command sent
        time.sleep(0.1)  # Wait for a short time before sending the next command

def clear_errlog():
    send_command("errlog Clear")

def version():
    send_command("version")

def get_errlog():
    try:
        num_logs = int(logs_entry.get())  # Get the number of logs from the entry widget
        if num_logs < 0:
            raise ValueError("Number of logs must be a non-negative integer.")
        send_errlog_all(num_logs)
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Please enter a valid number of logs. {str(e)}")

def clear_log_box():
    """Clear the log message window"""
    log_box.config(state='normal')  # Temporarily enable the widget
    log_box.delete(1.0, tk.END)    # Clear the contents
    log_box.config(state='disabled')  # Re-disable the widget


# GUI Setup
root = tk.Tk()
root.title("UART Communication")
root.geometry("1600x900")
root.minsize(800, 600)

uart = None
is_connected = False  # Global flag to track connection status

frame_top = tk.Frame(root)
frame_top.grid(row=0, column=0, pady=5, sticky="ew")

port_var = tk.StringVar()
port_menu = ttk.Combobox(frame_top, textvariable=port_var, state='readonly', justify="center")  # Add justify="center" here
port_menu.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

# Configure the top frame to expand in x-direction when window is resized
frame_top.grid_columnconfigure(0, weight=1)

# Call refresh_ports to populate the drop-down and set the default value
refresh_ports()

refresh_button = tk.Button(frame_top, text="Refresh", command=refresh_ports)
refresh_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

connect_button = tk.Button(frame_top, text="Connect", command=connect_uart)
connect_button.grid(row=1, column=0, columnspan=4, pady=5, padx=5, sticky="ew")

# Configure bottom part of the frame for expanding as well
frame_bottom = tk.Frame(root)
frame_bottom.grid(row=2, column=0, pady=10, padx=5, sticky="nsew")

# Configure the bottom frame to expand in x-direction when window is resized
frame_bottom.grid_columnconfigure(0, weight=1)
frame_bottom.grid_columnconfigure(1, weight=1)
frame_bottom.grid_columnconfigure(2, weight=1)
frame_bottom.grid_columnconfigure(3, weight=1)

frame_middle = tk.Frame(root)
frame_middle.grid(row=1, column=0, pady=5, sticky="nsew")

log_box = scrolledtext.ScrolledText(frame_middle, wrap=tk.WORD)
log_box.grid(row=0, column=0, pady=5, padx=5, sticky="nsew")  # Use grid for better control

# Configure the middle frame to expand in both x and y directions when window is resized
frame_middle.grid_rowconfigure(0, weight=1)
frame_middle.grid_columnconfigure(0, weight=1)

# User input for the number of logs to send
logs_label = tk.Label(frame_bottom, text="number of logs:")
logs_label.grid(row=0, column=1, pady=5, padx=5)

logs_entry = tk.Entry(frame_bottom)
logs_entry.grid(row=0, column=2, pady=5, padx=5, sticky="ew")
logs_entry.insert(0, "1")  # Set default value to 3

get_button = tk.Button(frame_bottom, text="GET errlog", command=get_errlog)
get_button.grid(row=1, column=1, columnspan=2, pady=5, padx=50, sticky="ew")

clear_button = tk.Button(frame_bottom, text="Clear errlog", command=clear_errlog)
clear_button.grid(row=5, column=0, columnspan=5, pady=5, padx=2, sticky="ew")

#exit_button = tk.Button(frame_bottom, text="EXIT", command=root.quit)
#exit_button.grid(row=4, column=0, columnspan=4, pady=5, padx=5, sticky="ew")

# Button to clear the log message window
clear_log_button = tk.Button(frame_bottom, text="Clear Window", command=clear_log_box)
clear_log_button.grid(row=1, column=0, columnspan=1, pady=1, padx=1, sticky="ew")

# Allow the window to resize properly
root.grid_rowconfigure(0, weight=0)  # Top row
root.grid_rowconfigure(1, weight=1)  # Middle row
root.grid_rowconfigure(2, weight=0)  # Bottom row

root.grid_columnconfigure(0, weight=1)  # Main column

# Refresh ports on startup
refresh_ports()

create_tags()

root.mainloop()