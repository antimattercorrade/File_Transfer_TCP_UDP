## File Transfer using TCP and UDP ⭐

Simple TCP and UDP client-server programs in python for file transfer. The servers and clients have settings to configure Nagle's Algorithm and Quick Ack for TCP. 

### Directory Architecture: 📁

```
File_Transfer_TCP_UDP
├─ Client
│  ├─ tcp_client.py
│  └─ udp_client.py
├─ README.md
└─ Server
│  ├─ Atlas Shrugged.txt
│  ├─ Don Quixote.txt
│  ├─ Shogun.txt
│  ├─ The Stand.txt
│  ├─ War and Peace.txt
│  ├─ tcp_server.py
└─ └─ udp_server.py

```

### Instructions to Run :runner:

TCP Client and Server
  - To run the client, run `python3 tcp_client.py` in the Client folder. It will ask for a number corresponding to which will be the book to download. 
  - To run the server, run `python3 tcp_server.py` in the Server folder.
  - After the input is received, it will connect to the server and download the respective book in the "Client" folder.
  - The buffer size in the client and server can be set by changing the value corresponding to variable "BUFFER_SIZE" in "tcp_client.py" and "tcp_server.py" files.
  - To disable Nagle's Algorithm and Delayed Ack, comments are provided in the respective programs.
  - The client displays the calculated throughput and download time after download.

UDP Client and Server

  - To run the client, run `python3 udp_client.py` in the Client folder. It will ask for a number corresponding to which will be the book to download. 
  - To run the server, run `python3 udp_server.py` in the Server folder.
  - After the input is received, it will download the respective book in the "Client" folder.
  - The buffer size in the client and server can be set by changing the value corresponding to variable "BUFFER_SIZE" in "udp_client.py" and "udp_server.py" files.
  - The client displays the calculated throughput and download time after download.

