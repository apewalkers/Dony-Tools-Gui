import os
import subprocess

COLORS = [
    "\033[37m",  # White 0
    "\033[31m",  # Red 1
    "\033[32m",  # Green 2
    "\033[33m",  # Yellow 3
    "\033[34m",  # Blue 4
    "\033[35m",  # Magenta 5
    "\033[36m",  # Cyan 6
    "\033[30m",  # Black 7
    "\033[90m",  # Bright Black (Gray) 8
    "\033[91m",  # Bright Red 9
    "\033[92m",  # Bright Green 10
    "\033[93m",  # Bright Yellow 11
    "\033[94m",  # Bright Blue 12 
    "\033[95m",  # Bright Magenta 13
    "\033[96m",  # Bright Cyan 14 
    "\033[97m",  # Bright White 15
]

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

def colored_line(line, color_index=0):
    """Applies a single color to a line."""
    color = COLORS[color_index % len(COLORS)]
    return color + line + "\033[0m"

def terminal_interface():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bin_dir = os.path.join(script_dir, "bin")  # Path to the bin directory

    while True:
        # Apply bold and larger font size (if your terminal supports it)
        title = "\033[1mTerminal Interface\033"
        Option1 = "1. READ BIN FILE"
        Option2 = "2. Interactive UART Terminal BAUD 115200"
        Option3 = "3. Exit"

        print(color_gradient_terminal(title, COLORS))
        print(colored_line(Option1, 6))
        print(colored_line(Option2, 13)) 
        print(colored_line(Option3, 15)) 

        choice = input("Select an option (1, 2, or 3): ")

        if choice == "1":
            nor_path = os.path.join(bin_dir, "nor.py")
            if os.path.exists(nor_path):
                print(color_gradient_terminal(f"Executing {nor_path}...", COLORS))
                subprocess.run(["python", nor_path], check=True)
            else:
                print(color_gradient_terminal(f"File not found: {nor_path}", COLORS))
        elif choice == "2":
            terminal_path = os.path.join(bin_dir, "terminal.py")
            if os.path.exists(terminal_path):
                print(color_gradient_terminal(f"Executing {terminal_path}...", COLORS))
                subprocess.run(["python", terminal_path], check=True)
            else:
                print(color_gradient_terminal(f"File not found: {terminal_path}", COLORS))
        elif choice == "3":
            print(color_gradient_terminal("Exiting...", COLORS))
            break
        else:
            print(color_gradient_terminal("Invalid choice. Please try again.", COLORS))

if __name__ == "__main__":
    terminal_interface()