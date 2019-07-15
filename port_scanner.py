#Wes Smith
__date__ = "4/23/2018"
'''*
DESCRIPTION: Simple port scanner using socket
*'''

import socket
import sys
from datetime import datetime

remoteServer    = input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

'''print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)'''

t1 = datetime.now()

try:
    for port in range(int(input("Enter Starting Port #: ")),
                      int(input("Enter Ending Port #: "))):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {0}: 	 Open".format(port))
        sock.close()
        
        print("-" * 60)
        print("Please wait, scanning remote host", remoteServerIP)
        print("-" * 60)

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

t2 = datetime.now()

total =  t2 - t1

print("\nStart Time: {0}" .format(t1))
print("\nEnd Time: {0}" .format(t2))
print("\nScan Duration: {0}" .format(total))
