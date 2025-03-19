# bin/uart.py
import serial
import serial.tools.list_ports
import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk

uart_client = None # Global variable for UartClientEmc instance (within uart.py)

class UartClientEmc:
    # ... (UartClientEmc class remains the same) ...
    def __init__(self):
        self.uart = None

    def init(self, port_name):
        try:
            self.uart = serial.Serial(port_name, baudrate=115200, timeout=1) # 1 second timeout for read operations
            return True
        except serial.SerialException as e:
            print(f"Error opening serial port {port_name}: {e}")
            return False

    def close(self):
        if self.uart and self.uart.is_open:
            self.uart.close()

    def checksum(self, buf):
        csum = 0
        for b in buf.encode(): # Iterate over bytes of the encoded string
            csum += b
        return csum

    def cmd_send(self, cmdline, wait_echo=True):
        if not self.uart or not self.uart.is_open:
            print("UART port is not initialized or open.")
            return False

        cmd_checksummed = cmdline + f":{self.checksum(cmdline):02X}\n"
        try:
            self.uart.write(cmd_checksummed.encode()) # Encode the command string to bytes

            if not wait_echo:
                return True

            # Wait for echo (read line until timeout or echo received)
            timeout_ms = len(cmd_checksummed) * 200 / 1000 # timeout in seconds, adjusted for command length
            self.uart.timeout = timeout_ms if timeout_ms > 0.1 else 0.1 # Minimum timeout of 0.1s
            echo_line = self.uart.readline().decode().strip() # Decode bytes to string, remove leading/trailing whitespace

            if echo_line == cmdline:
                return True
            else:
                print(f"Echo mismatch, expected: '{cmdline}', received: '{echo_line}'")
                return False

        except serial.SerialException as e:
            print(f"Serial communication error: {e}")
            return False
        except UnicodeDecodeError as e:
            print(f"Unicode decode error during echo read: {e}")
            return False

        return False # Should not reach here, but for completeness


def list_serial_ports():
    ports = serial.tools.list_ports.comports()
    port_list = []
    for port, desc, hwid in sorted(ports):
        port_list.append(f"{port}: {desc} [{hwid}]")
    return port_list


def read_error_codes_action(output_area, selected_port):
    global uart_client # Access the global uart_client defined in uart.py
    output_area.insert(tk.END, f"\nRead Error Codes button pressed for port: {selected_port} - Action IMPLEMENTED in bin/uart.py\n")
    # Implement UART command sending and response handling here
    if uart_client: # Now correctly using the uart_client from uart.py
        if uart_client.init(selected_port): # Re-initialize UART every time to ensure port is open
            command = "READ_ERROR_CODES" # Replace with actual command
            if uart_client.cmd_send(command):
                output_area.insert(tk.END, f"Successfully sent command: {command}\n")
                # Logic to read response from UART and display in output_area
                response = uart_client.uart.read(100).decode() # Example: read up to 100 bytes, decode
                output_area.insert(tk.END, f"Response:\n{response}\n")
                uart_client.close() # Close port after command
            else:
                output_area.insert(tk.END, f"Failed to send command: {command}\n")
                uart_client.close() # Close port even on failure
        else:
            output_area.insert(tk.END, f"Failed to initialize UART on port {selected_port}\n")
    else:
        output_area.insert(tk.END, "UART client not initialized.\n")


def clear_error_codes_action(output_area, selected_port):
    global uart_client # Access the global uart_client defined in uart.py
    output_area.insert(tk.END, f"\nClear Error Codes button pressed for port: {selected_port} - Action IMPLEMENTED in bin/uart.py\n")
    # Implement UART command sending and response handling here
    if uart_client: # Now correctly using the uart_client from uart.py
        if uart_client.init(selected_port): # Re-initialize UART every time to ensure port is open
            command = "CLEAR_ERROR_CODES" # Replace with actual command
            if uart_client.cmd_send(command):
                output_area.insert(tk.END, f"Successfully sent command: {command}\n")
                # Logic to read response if needed
                response = uart_client.uart.read(100).decode() # Example: read up to 100 bytes, decode
                output_area.insert(tk.END, f"Response:\n{response}\n")
                uart_client.close() # Close port after command
            else:
                output_area.insert(tk.END, f"Failed to send command: {command}\n")
                uart_client.close() # Close port even on failure
        else:
            output_area.insert(tk.END, f"Failed to initialize UART on port {selected_port}\n")
    else:
        output_area.insert(tk.END, "UART client not initialized.\n")


def open_terminal_action(output_area, selected_port):
    output_area.insert(tk.END, f"\nTerminal button pressed for port: {selected_port}. Feature not implemented yet.\n")
    # Logic to open a terminal interface will go here - in a more advanced version


def set_com_port(port_name, output_area):
    global selected_com_port, uart_client # Access the global selected_com_port and uart_client from main.py
    selected_com_port.set(port_name)
    output_area.insert(tk.END, f"\nSelected COM Port: {port_name}\n")

    global uart_client # Use the global uart_client defined in uart.py module
    uart_client = UartClientEmc() # Initialize the UART client when COM port is selected

    # Create a frame to hold the new buttons
    uart_control_frame = ttk.Frame(output_area.master) # Use output_area.master to place in main window
    uart_control_frame.pack(pady=5) # Add some vertical padding

    # Read Error Codes Button
    read_errors_button = ttk.Button(uart_control_frame, text="Read Error Codes", command=lambda: read_error_codes_action(output_area, port_name))
    read_errors_button.pack(side=tk.LEFT, padx=5)

    # Clear Error Codes Button
    clear_errors_button = ttk.Button(uart_control_frame, text="Clear Error Codes", command=lambda: clear_error_codes_action(output_area, port_name))
    clear_errors_button.pack(side=tk.LEFT, padx=5)

    # Terminal Button
    terminal_button = ttk.Button(uart_control_frame, text="Terminal", command=lambda: open_terminal_action(output_area, port_name))
    terminal_button.pack(side=tk.LEFT, padx=5)

    output_area.window_create(tk.END, window=uart_control_frame) # Embed frame in scrolledtext
    output_area.insert(tk.END, "\n") # Add newline after buttons