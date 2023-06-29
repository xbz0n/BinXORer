# Reverse XOR Encrypted Shellcode Generator & Injector

This script generates a reverse HTTPS shellcode using Metasploit's msfvenom, encrypts it with XOR, and injects the encrypted shellcode into a predefined location in a C# file. It also compiles the updated C# code and runs Metasploit console to listen for incoming connections.

## Requirements

Metasploit Framework
Mono C# Compiler (mcs)
Python 3
Usage

Place the C# file (program.cs) that will receive the encrypted shellcode in the same directory as this script.
Run the script with python binXORer.py, and it will prompt for LHOST and LPORT values.
The script will generate and insert the shellcode, compile the C# program, and run Metasploit console to listen for incoming connections.
## Limitations

This script is tailored for a Windows target, using a reverse HTTPS payload.
It is recommended to review and modify the script as necessary for different payload types or target systems.
## Contributing

Please fork the project, create a new branch, and submit a pull request. For major changes, please open an issue first to discuss the proposed change.

## License

This project is licensed under the MIT License.

## Disclaimer

This script is for educational purposes and preparing for the OSEP certification exam. It should only be used in environments where you have permission to perform penetration testing.

## Acknowledgements

A big thank you to the Offensive Security team for creating the OSEP certification. Their dedication to fostering advanced penetration testing skills is greatly appreciated.
