# bin/nor.py
import os
import sys

bin_dir = os.path.dirname(os.path.abspath(__file__)) # bin directory path
sys.path.append(bin_dir) # Append bin directory to sys.path for module import
parent_dir = os.path.dirname(bin_dir) # Parent directory path
sys.path.append(parent_dir) # Append parent directory to sys.path for 'decoded' import

import decoded # Import 'decoded' from the parent directory
import msvcrt # For getch() in Windows, or use alternative for other OS


def extract_hex_data(file_path, start_offset, end_offset):
    with open(file_path, "rb") as file:
        file.seek(start_offset)
        data = file.read(end_offset - start_offset)
        if len(data) % 4 != 0:
            raise ValueError("Data length is not a multiple of 4 bytes, check the offsets.")
        hex_data = [f"{int.from_bytes(data[i:i+4], 'little'):08X}" for i in range(0, len(data), 4)]
        return hex_data
    
def color_gradient_terminal(terminal_output, colors):
    """
    Applies alternating color gradients to a terminal output string.

    Args:
        terminal_output: The terminal output string.
        colors: A list of 5 color codes for the gradient.
               Each color code should be a string representing an ANSI escape code
               for setting text color, e.g., "\033[31m" for red.

    Returns:
        The terminal output string with color gradients applied.
    """

    lines = terminal_output.splitlines()
    colored_lines = []
    color_index = 0

    for line in lines:
        colored_line = colors[color_index % len(colors)] + line + "\033[0m"  # Apply color, reset color
        colored_lines.append(colored_line)
        color_index += 1

    return "\n".join(colored_lines)

def format_emc_error_log_data(hex_data, file_path):
    formatted_data = f"{file_path}\n== Emc Error Log ==\n"
    formatted_data += "# No  Code      Rtc           PowState      UpCause         SeqNo      DevPm     T(SoC)  T(Env)  Padding(0) Padding(1) | Decoded Messages\n"
    formatted_data += "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"

    for index in range(0, len(hex_data), 8):
        row = hex_data[index:index+8]
        if len(row) == 8:
            formatted_row = f"{index//8:02d} {row[0]} {row[1]} {row[2]} {row[3]} {row[4][:4]} {row[4][4:]} {row[5][:4]} {row[5][4:]} {row[6][:4]} {row[6][4:]} {row[7][:4]} {row[7][4:]}\n"
            formatted_row += "    Decoded:\n"
            formatted_row += f"      ErrCode     : {decoded.err_code(row[0]).strip()}\n"
            formatted_row += f"      PowerState  : {decoded.pw_state(row[2]).strip()}\n"
            formatted_row += f"      UpCause     : {decoded.upcause(row[3]).strip()}\n"
            formatted_row += f"      PSQ         : {decoded.psq(row[4][4:8]).strip()}       {(row[4][4:8]).strip()}\n"
            formatted_row += f"      DevPower    : {decoded.devpower(row[4][:4]).strip()}\n"
            formatted_row += "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
            formatted_data += formatted_row

    return formatted_data


def decode_nor_functionality(output_area=None):  # output_area is now optional for terminal use
    if output_area:
        output_area.delete(1.0, tk.END)  # Clear previous output if in GUI mode
        output_area.insert(tk.END, "\n--- Decode Dumped NOR ---\n")

    script_dir = os.path.dirname(os.path.abspath(__file__)) # Script's directory
    current_dir = os.path.dirname(script_dir)  # Start in the parent directory of the script

    while True:
        items = os.listdir(current_dir)
        bin_files = [item for item in items if item.lower().endswith('.bin') and os.path.isfile(os.path.join(current_dir, item))]
        dirs = [item for item in items if os.path.isdir(os.path.join(current_dir, item))]

        print(f"\n--- Current directory: {current_dir} ---")
        print("0: Go up one directory")

        colors = [
        "\033[31m",  # Red
        "\033[32m",  # Green
        "\033[33m",  # Yellow
        "\033[34m",  # Blue
        "\033[35m",  # Magenta
        ]

        for i, d in enumerate(dirs):
            colored_line = colors[i % len(colors)] + f"{i + 1}: [DIR] {d}" + "\033[0m"
            print(colored_line)

        for i, bin_file in enumerate(bin_files):
            colored_line = colors[(len(dirs) + i) % len(colors)] + f"{len(dirs) + i + 1}: [BIN] {bin_file}" + "\033[0m"
            print(colored_line)
        if not bin_files and not dirs:
            print("No .bin files or directories found in this directory.")
            choice = input("Enter 0 to go up or 'q' to quit: ")
        else:
            choice = input(f"Select a directory (1-{len(dirs)}), a bin file ({len(dirs) + 1}-{len(dirs) + len(bin_files)}), 0 to go up, or 'q' to quit: ")

        if choice == 'q':
            if output_area:
                output_area.insert(tk.END, "Operation cancelled by user.\n")
            print("Exiting.")
            break
        elif choice == '0':
            parent_directory = os.path.dirname(current_dir)
            if parent_directory != current_dir: # Prevent going above root directory in some systems
                current_dir = parent_directory
            else:
                print("Already at the root directory.")
        elif choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(dirs):
                current_dir = os.path.join(current_dir, dirs[index])
            elif len(dirs) <= index < len(dirs) + len(bin_files):
                bin_file = bin_files[index - len(dirs)]
                bin_file_path = os.path.join(current_dir, bin_file)
                if output_area:
                    output_area.insert(tk.END, f"\nProcessing file: {bin_file_path}\n")
                print(f"\nProcessing file: {bin_file_path}")
                try:
                    with open(bin_file_path, 'rb') as f:  # Use full path to open the file
                        header = f.read(8)
                        if header == b'SONY COM':
                            if output_area:
                                output_area.insert(tk.END, "Header 'SONY COM' found. Proceeding with data extraction.\n")
                            print("Header 'SONY COM' found. Proceeding with data extraction.")
                            f.seek(0)


                            data_offsets = { 
                            "Chassis Model               ": {"offset": 0x1C7230, "size": 0x20, "type": "string"}, 
                            "Console Package ID          ": {"offset": 0x1C73E0, "size": 0x8, "type": "string"}, 
                            "Serial_Number               ": {"offset": 0x1C7210, "size": 0x11, "type": "string"}, 
                            "Model_Number                ": {"offset": 0x1C7250, "size": 0x10, "type": "string"}, 
                            "SOC_UID                     ": {"offset": 0x1C7260, "size": 0x10, "type": "hex"}, 
                            
                            "Platform ID:                ": {"offset": 0x1C4000, "size": 0x8, "type": "hex"},

                            "WLAN_MAC                    ": {"offset": 0x1C73C0, "size": 0x6, "type": "mac"}, # Change type to 'mac'
                            "Ethernet MAC                ": {"offset": 0x1C4020, "size": 0x6, "type": "mac"}, # Change type to 'mac'
                            "Ethernet 2 MAC (Dev Kit)    ": {"offset": 0x1C4026, "size": 0x6, "type": "hex"}, # Change type to 'mac'
                            } 

                            extracted_data = {} 
                            hardware_info_text = "== HARDWARE INFO ==\n" 

                            # Assuming 'f' is your file object
                            # f = open("your_binary_file", "rb") # Example: open your binary file

                            for name, params in data_offsets.items(): 
                                f.seek(params["offset"]) 
                                data = f.read(params["size"]).rstrip(b'\x00').rstrip(b'\xff') 
                                if params["type"] == "string": 
                                    extracted_data[name] = data.decode('ascii', errors='ignore') 
                                elif params["type"] == "hex": 
                                    extracted_data[name] = data.hex().upper()
                                elif params["type"] == "mac": # Handle MAC address formatting
                                    mac_bytes = data
                                    if len(mac_bytes) == 6:
                                        mac_address = ":".join(f"{byte:02X}" for byte in mac_bytes)
                                        extracted_data[name] = mac_address
                                    else:
                                        extracted_data[name] = "Invalid MAC length"

                                hardware_info_text += f"{name.replace('_', ' '):<20}= {extracted_data.get(name, 'N/A')}\n" # Format here 

                            #print(hardware_info_text)

                            # f.close() # Close your file object

                            if output_area:
                                output_area.insert(output_area.index('end'), hardware_info_text)  # Output Hardware Info to GUI
                            print(color_gradient_terminal(hardware_info_text, colors))

                            serial_number_filename = extracted_data.get("Serial_Number               ", "UNKNOWN_SERIAL") + ".txt"

                            # EMC Error Log Extraction and Formatting
                            start_offset_error_log = 0x1CE100
                            end_offset_error_log = 0x1CEC70

                            try:
                                hex_error_log_data = extract_hex_data(bin_file_path, start_offset_error_log, end_offset_error_log)
                                formatted_error_log = format_emc_error_log_data(hex_error_log_data, bin_file_path)

                                # Output first 5 Error Codes to GUI (with decoding)
                                if output_area:
                                    output_area.insert(output_area.index('end'), "== EMC ERROR LOG (First 5 Codes with Decoding) ==\n")
                                    output_area.insert(output_area.index('end'), "# No  Code      Rtc           PowState      UpCause         SeqNo      DevPm     T(SoC)  T(Env)  Padding(0) Padding(1) | Decoded Messages\n")
                                    output_area.insert(output_area.index('end'), "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                                print("\n== EMC ERROR LOG (First 5 Codes with Decoding) ==")
                                print("# No  Code      Rtc           PowState      UpCause         SeqNo      DevPm     T(SoC)  T(Env)  Padding(0) Padding(1) | Decoded Messages")
                                print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                for i in range(min(5, len(hex_error_log_data) // 8)):  # Loop for max 5 error codes
                                    start_index = i * 8
                                    end_index = start_index + 8
                                    row = hex_error_log_data[start_index:end_index]
                                    if len(row) == 8:
                                        formatted_row = f"{i:02d} {row[0]} {row[1]} {row[2]} {row[3]} {row[4][:4]} {row[4][4:]} {row[5][:4]} {row[5][4:]} {row[6][:4]} {row[6][4:]} {row[7][:4]} {row[7][4:]}\n"
                                        formatted_row += "    Decoded:\n"
                                        formatted_row += f"      ErrCode     : {decoded.err_code(row[0]).strip()}       {row[0]}\n"
                                        formatted_row += f"      PowerState  : {decoded.pw_state(row[2]).strip()}\n"
                                        formatted_row += f"      UpCause     : {decoded.upcause(row[3]).strip()}\n"
                                        formatted_row += f"      PSQ         : {decoded.psq(row[4][4:8]).strip()}       {(row[4][4:8]).strip()}\n"
                                        formatted_row += f"      DevPower    : {decoded.devpower(row[5][:4]).strip()}\n"
                                        formatted_row += "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
                                        if output_area:
                                            output_area.insert(output_area.index('end'), formatted_row)
                                        print(formatted_row, end="")


                                    output_text = hardware_info_text + formatted_error_log  # Combine without UART data


                                output_text += "\n\n== FULL EMC ERROR LOG WITH DECODING ==\n"  # Add section title for full log in file
                                output_text += formatted_error_log  # Append full formatted error log with decoding to output
                                output_text += formatted_uart_log  # Append UART log to output file as well
                                print("------------------------------------\n")
                                print("== See Above Error Data ==")
                                print(color_gradient_terminal(hardware_info_text, colors))
                                print("Output File :", {serial_number_filename})
                                print("------------------------------------\n")


                                with open(serial_number_filename, 'w') as outfile:
                                    outfile.write(output_text)
                                if output_area:
                                    output_area.insert(output_area.index('end'), f"\nData saved to: {serial_number_filename}\n")
                                print(f"\nData saved to: {serial_number_filename}")

                            except ValueError as e:
                                if output_area:
                                    output_area.insert(output_area.index('end'), f"Error processing EMC Error Log: {e}\n")
                                    output_area.insert(output_area.index('end'), "Error log data will not be included in the output file.\n")
                                print(f"Error processing EMC Error Log: {e}")
                                print("Error log data will not be included in the output file.")


                        else:
                            if output_area:
                                output_area.insert(output_area.index('end'), f"Header 'SONY COM' not found in {bin_file}. Skipping.\n")
                            print(f"Header 'SONY COM' not found in {bin_file}. Skipping.")
                except Exception as e:
                    if output_area:
                        output_area.insert(output_area.index('end'), f"Error processing file {bin_file}: {e}\n")
                    print(f"processing file {bin_file}:", {serial_number_filename})
                    print(color_gradient_terminal(hardware_info_text, colors))
                break # After processing a bin file, break the loop to re-display directory content
            else:
                print("Invalid selection.")
        else:
            print("Invalid input. Please enter a number or 'q' to quit.")

        print("\nPress any key to continue...")
        if os.name == 'nt': # Windows
            msvcrt.getch()
        else: # For Linux/macOS
            input() # Using input() as cross-platform alternative for simple pause

if __name__ == "__main__":
    decode_nor_functionality() # Call function without output_area for terminal use
    print("\nPress any key to continue...")
if os.name == 'nt': # Windows
    msvcrt.getch()
else: # For Linux/macOS
    input() # Using input() as cross-platform alternative for simple pause