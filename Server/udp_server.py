#########################################
#Import libraries
#########################################
import socket
import os
import time
from time import sleep

#########################################
#Declaring Connection Variables
#########################################
BUFFER_SIZE = 32                #Buffer Size for receiving file in chunks
BUFFER_FILENAME = 1024          #Buffer Size for receiving filename from client
SERVER_IP = 'localhost'         #Server IP
SERVER_PORT = 12345             #Server Port Number

#########################################
#Initializing UDP Socket
#########################################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Starting server on port ',SERVER_PORT)

sock.bind((SERVER_IP, SERVER_PORT))     

while True:
    print('Waiting to receive message')                                #Waiting for connection
    file_name, client_addr = sock.recvfrom(BUFFER_FILENAME)
    print(client_addr,' connected')
    start = time.time()                                                #Start Timer

    file_name = file_name.decode()                                     #Decode file name received
    file_name = os.path.basename(file_name)

    fd = open(file_name, 'rb')                                         #Open file in read mode
    buf = fd.read(BUFFER_SIZE)                                         #Read from file equal to buffer size

    print('Sending Data')

    while(buf):                                                        #Send data to client while end of file is not encountered
        sock.sendto(buf, client_addr)
        
        ###########################################
        # Uncomment the next line for question 4
        ###########################################
        
        #sleep(100/1000000)

        buf = fd.read(BUFFER_SIZE)
    
    fd.close()                                                         #Close file 
    
    end = time.time()                                                  #End timer
    print(f"Time taken to upload: {end - start} sec")                  #Print upload time
    print(file_name," uploaded")
