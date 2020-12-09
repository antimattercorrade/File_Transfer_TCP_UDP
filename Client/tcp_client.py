#########################################
#Import libraries
#########################################
import socket
import os
import time

#########################################
#Declaring Connection Variables
#########################################
BUFFER_SIZE = 32                        #Buffer Size for receiving file in chunks
HOST = 'localhost'                      #Server IP
PORT = 12345                            #Server Port Number

#########################################
#Input Filename to Download
#########################################

print("Enter the corresponding number to download book:")
print("1. Atlas Shrugged by Ayn Rand")
print("2. Don Quixote by Miguel de Cervantes")
print("3. Shogun by James Clavell")
print("4. The Stand by Stephen King")
print("5. War and Peace by Leo Tolstoy")

file_number = int(input())

if(file_number == 1):
    file_name = "Atlas Shrugged.txt"
elif(file_number == 2):
    file_name = "Don Quixote.txt"
elif(file_number == 3):
    file_name = "Shogun.txt"
elif(file_number == 4):
    file_name = "The Stand.txt"
elif(file_number == 5):
    file_name = "War and Peace.txt"

file = file_name.split('.')

#########################################
#Initializing UDP Socket
#########################################

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#########################################
#Uncomment the line below for disabling Nagle's Algortihm
#########################################

# sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

#########################################
#Uncomment the line below for disabling Delayed Ack
#########################################

# sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_QUICKACK, 1)

try:
    print('Connecting to ',HOST)
    sock.connect((HOST, PORT))                                        #Connect to server
    start = time.time()                                               #Start timer
    print('Connected')
    sock.send(f"{file_name}".encode())                                #Send filename
    
    file_name = file[0] + "+Protocol=TCP" + "+" + str(os.getpid()) + "." + file[1]

    with open(file_name, 'wb') as f:                                  #Open file in write mode
        print('Receiving Data')
        while True:
            byte = sock.recv(BUFFER_SIZE)                             #Recieve data from server

            if not byte:
                break

            f.write(byte)                                             #Write to file
    
finally:
    sock.close()                                                      #Close connection to the server
    end = time.time()                                                 #End timer           
    print(f"Time taken to download: {end - start} sec")               #Print download time

    file_stat = os.stat(file_name)                                    #Get downloaded file size
    file_size = file_stat.st_size

    throughput = round((file_size*0.001)/(end - start), 3)            #Caculate throughput
    print("Downloaded ",file_name)
    print("Throughput: ",throughput,"kB/s")
    
