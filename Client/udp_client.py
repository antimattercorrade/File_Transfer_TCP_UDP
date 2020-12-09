#########################################
#Import libraries
#########################################
import socket
import os
import time

#########################################
#Declaring Connection Variables
#########################################

BUFFER_SIZE = 32                #Buffer Size for receiving file in chunks
HOST = 'localhost'              #Server IP
PORT = 12345                    #Server Port Number
server_addr = (HOST,PORT)       #Tuple to identify the UDP connection while sending

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

file = file_name.split('.')                 #Get filename without extension

#########################################
#Initializing UDP Socket
#########################################

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    start = time.time()                                                                 #Start timer
    sock.sendto(f"{file_name}".encode(),server_addr)                                    #Send filename to download to server
    file_name = file[0] + "+Protocol=UDP" + "+" + str(os.getpid()) + "." + file[1]      #Create received filename in given format

    with open(file_name, 'wb') as f:                                                    #Open file to write in write byte format
        print('Receiving Data')
        while True:
            sock.settimeout(2)                                                          #Set timeout interval

            byte, server = sock.recvfrom(BUFFER_SIZE)                                   #Receive book data from the server
            
            if not byte:
                break

            f.write(byte)                                                               #Write received data to file


except:                                                                                 #If timeout occurs
    print("Timeout Occurred")
    end = time.time()                                                                   #End timer
    print(f"Time taken to download: {end - start - 2} sec")                             #Calculate Download Time
    print("Downloaded ",file_name)

    file_stat = os.stat(file_name)                                                      #Get downloaded file size 
    file_size = file_stat.st_size

    throughput = round((file_size*0.001)/(end - start), 3)                              #Calculate Throughput rounded to 3 decimal places
    print("Throughput: ",throughput,"kB/s")
    
    sock.close()                                                                        #Close socket

finally:
    sock.close()
    
