Project Documentation: Python Network Port Scanner



Project Overview

This project is a custom-engineered network reconnaissance tool developed to audit the attack surface of a given host. The script identifies active services and potential security vulnerabilities, providing a foundational layer for network security assessments. This project was driven by a curiosity regarding network architecture and how foundational Python concepts can be applied to cybersecurity tasks.


Technical Specifications

Language: Python 3.x
Library: socket (for access to the internet)
Environment: macOS 
Interface: VsCode
Output: Console logging and persistent .txt audit reports


Core Features

Automates the testing of a user-defined range of ports (e.g., 20–100) using a for loop.


Utilizes socket.connect_ex to perform a non-blocking TCP three-way handshake, capturing error codes without crashing the application.


Implements a 0.5-second timeout per port to balance scanning speed with network reliability.


Generates a timestamped scan_report.txt file containing the target IP, port range, and the status of every scanned port.


Usage Instructions


Open the terminal in VS Code.

Execute the script using: python3 RangeScanner.py


Input the target (e.g., scanme.nmap.org).


Define the port boundaries (e.g., 20 to 80).


Review the live results in the console and the finalized report in scan_report.txt.


*****Security & Ethics Disclaimer******************************
This tool is intended for authorized auditing and educational purposes only. Unauthorized scanning of networks is a violation of the Computer Fraud and Abuse Act (CFAA) and ethical hacking standards. All tests were performed on local environments or authorized targets (scanme.nmap.org).

