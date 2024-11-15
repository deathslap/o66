import os
import subprocess 

def splash():
    print('''
          
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⠉⠁⠀⠀⠀⠀⠈⢉⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢻⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⠏⠀⠀⠀⣴⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⢠⣤⣤⣼⣿⣿⣿⣿⣿
                ⣿⣿⣿⠃⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿
                ⣿⣿⡏⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⣀⣠⣤⣾⣿⣿⣿⣿⣿
                ⣿⣿⠁⠀⠀⠀⠀⠀⠀⠉⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⣿⣿
                ⣿⣿⠶⣶⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⠶⣿⣿
                ⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⣀⣀⣿⣿
                ⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣴⣶⣿⣿⣿⣿
                ⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠛⠛⢻⣿⣿⣿⣿
                ⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⡀⠀⠀⠀⠀⣠⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿      

 ██████╗ ██████╗ ██████╗ ███████╗██████╗      ██████╗  ██████╗ 
██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██╔════╝ ██╔════╝ 
██║   ██║██████╔╝██║  ██║█████╗  ██████╔╝    ███████╗ ███████╗ 
██║   ██║██╔══██╗██║  ██║██╔══╝  ██╔══██╗    ██╔═══██╗██╔═══██╗
╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║    ╚██████╔╝╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝  ╚═════╝ 
          
          ''')

# BASE FUNCTIONS
## BANNER
def welcome():
    print("Welcome to Order 66")
    print ("")

## CLEAR SCREEN
def clear():
    os.system("clear")

# ENTER TO RETURN 
def exit():
    input("\nPress ENTER to return!")

# LIST MENU
def list_menu():
    print("[ 1 ] - /root")
    print("[ 2 ] - /etc")
    print("[ x ] - Return to menu")

def list_loop():
    while True:
        clear()
        splash()
        list_menu()
        print("\nWhich directory would you like to list?\n")
        try:
            ANS = input(">>> ")
            if ANS == "x":
                break
            elif ANS == "1":
                result = subprocess.run(["/bin/bash", "echo 'hello'"])
                clear()
                splash()
                print(result.stdout)
                exit()
            elif ANS == "2":
                result = subprocess.run("ls /etc", shell=True, capture_output=True, text=True)
                clear()
                splash()
                print(result.stdout)
                exit()
            else:
                splash()
                print("Invalid choice! Please select a number.")
                exit()
        except ValueError:
            splash()
            print("Invalid choice! Please select a number from the menu.")
            exit()

def list_files():
    clear()
    splash()
    """Lists files in the current directory."""
    result = subprocess.run("ls", shell=True, capture_output=True, text=True)
    print("Output of 'ls':\n", result.stdout)
    exit()

def show_current_directory():
    clear()
    splash()
    """Shows the current working directory."""
    result = subprocess.run("pwd", shell=True, capture_output=True, text=True)
    print(result.stdout)
    exit()

def display_date():
    clear()
    splash()
    """Displays the current date and time."""
    result = subprocess.run("date", shell=True, capture_output=True, text=True)
    print("Output of 'date':\n", result.stdout)
    exit()

def display_disk_usage():
    clear()
    splash()
    """Displays disk usage."""
    result = subprocess.run("df -h", shell=True, capture_output=True, text=True)
    print("Output of 'df -h':\n", result.stdout)
    exit()

def check_memory_usage():
    clear()
    splash()
    """Checks memory usage."""
    result = subprocess.run("free -h", shell=True, capture_output=True, text=True)
    print("Output of 'free -h':\n", result.stdout)
    exit()

def main_menu():
    print("Choose a command to run:\n")
    print("[ 1 ] - List files in the current directory (ls)")
    print("[ 2 ] - Show the current working directory (pwd)")
    print("[ 3 ] - Display the current date and time (date)")
    print("[ 4 ] - Display disk usage (df -h)")
    print("[ 5 ] - Check memory usage (free -h)")
    print("[ x ] - Exit the program")

# Reading from a config file
def read_lines_to_variables(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Strip newline characters from each line
    lines = [line.strip() for line in lines]

    # Assign each line to a variable
    if len(lines) > 0:
        var1 = lines[0]
    if len(lines) > 1:
        var2 = lines[1]
    if len(lines) > 2:
        var3 = lines[2]

    # Print the variables to confirm
    print("var1:", var1 if 'var1' in locals() else "Not available")
    print("var2:", var2 if 'var2' in locals() else "Not available")
    print("var3:", var3 if 'var3' in locals() else "Not available")

# File path/name
filename = '/tmp/example.txt'


# MAIN LOOP
if __name__ == "__main__":
    splash()
    welcome()
    main_menu()

while True:
    clear()
    splash()
    main_menu()
    try:
        ANS = input("\nEnter your choice (0-5): ")
        if ANS == "x":
            print("Exiting program. Goodbye!")
            break
        elif ANS == "1":
            list_menu()
            list_loop()
        elif ANS == "2":
            show_current_directory()
        elif ANS == "3":
            display_date()
        elif ANS == "4":
            display_disk_usage()
        elif ANS == "5":
            check_memory_usage()
        elif ANS == "6":
            clear()
            splash()
            read_lines_to_variables(filename)
            exit()
        else:
            splash()
            print("Invalid choice! Please select a number between 0 and 5.")
            exit()
    except ValueError:
        splash()
        print("Invalid choice! Please select a number between 0 and 5.")
        exit()
