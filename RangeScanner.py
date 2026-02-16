import socket                      #Socket allows for us to talk to the internet
from datetime import datetime      #Timestamps the scan report

print("-" * 50)                    #Prints a line of dashes for better readability in the console
print("--- STARTING PORT SCANNER ---")
print("-" * 50)

#Put the IP address and Ports of the target you want to scan
target = input("Enter the target: ")
start_port = input("Enter the start port you want to scan: ")
end_port = input("Enter the end port you want to scan: ")


#converts the port inputs to integers
start_port = int(start_port)
end_port = int(end_port)

print(f"Scanning {target})...")
print(f"Scanning ports {start_port} to {end_port}...")
print(f'Scan started at: {datetime.now()}')                 #Prints the current date and time when the scan starts for better tracking of scan duration
print("-" * 50)


with open('scan_report.txt', 'w') as report:
    report.write("---Port Scan Report---\n")
    report.write(f'Port Scan started at: {datetime.now()}\n') #Writes the timestamp of when the scan started to the report
    report.write(f'Target: {target}\n')
    report.write(f'Port: {start_port} to {end_port}\n')


#Create the connection with a loop to scan the range of ports
    try:

        for port in range(start_port,end_port + 1):

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Tells the socket to use IPv4 and TCP
            socket.setdefaulttimeout(0.5) #waits 0.5 seconds for a response

            result = s.connect_ex((target, port)) #Doesn't crash the program if the port is closed, instead it returns an error code that we can check

            if result == 0: #If the result is 0, it means the connection was successful and the port is open.
                print(f'Port {port}: OPEN')
                report.write(f'Port {port}: OPEN\n')
            else:
                print(f'Port {port}: CLOSED\n')
                report.write(f'Port {port}: CLOSED\n')
                s.close() #Closes the socket connection after each port scan to free up resources
    
    
    except:
        #If there is a problem with the socket connection
        print('\n\n Could not connect to server. Exiting...')   


print("- " * 50)
print("--- SCAN COMPLETE ---")    

print("\n Scan Report has been generated successfully. Check 'scan_report.txt' for details.")  


