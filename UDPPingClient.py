# UDP Pinger

#import all libraries

import random
import time
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)

# To set waiting time of one second for reponse from server
clientSocket.settimeout(1)

# Setting the message and Address of Server

address = ('localhost', 12000)

# Ping ten times
for counter in range(10):
    
	#Start time
    startTime = time.time()
	#messge to be sent
    message = 'Packet No --' + str(counter+1)
	#sends message to server
    clientSocket.sendto(message, address)
    
    try:
		#receives message from the server
        data, server = clientSocket.recvfrom(1024)
		#End Time
        endTime = time.time()
		#Round Trip Time is the difference between the time when client sends and receives the message
        RTT = endTime - startTime
        print  data
        print "Round Trip Time", RTT
        print
    
    except timeout:
        print 'REQUEST TIMED OUT'
        print
