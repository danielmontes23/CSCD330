#!/usr/bin/env python3
# author: Daniel Montes

from sys import argv
from socket import *
from urllib.parse import urlparse

def main():
    res = clientSocket()
    res = res.split('\r\n\r\n')[1]

    # Check for either '-p' or '-f'
    if argv[1] == '-p':
        print(res)
    if argv[1] == '-f':
        # Write a file and name it output.txt
        f = open("output.txt", "w")
        string = res
        f.write(string)
        f.close()

def clientSocket():
    serverPort = int(argv[2])
    url = urlparse(argv[3])
    serverName = url[1]
    path = url[2]
    # Creates a TCP socket and connects it to the server
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    # Constructs and sends HTTP GET request
    message = f"GET /{path} HTTP/1.1\r\nHost: {serverName}\r\n\r\n"
    clientSocket.send(message.encode())
    # Receives the HTTP message and decodes it
    res = clientSocket.recv(4000).decode()
    # Closes the socket
    clientSocket.close()
    # Return the result of the HTTP message
    return res



if __name__ == "__main__":
    main()