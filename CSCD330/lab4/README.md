Questions:
1. Why did you have to encode() function your request and decode() the response(s)? What do these functions do?
    The encode was used was used in line 27 and I used it to convert a string into a sequence of bytes. Its required when sending data through a socket because they(sockets) can only take bytes. I used the decode() function in the next line which is 28. It was used to convert the bytes recieved from the socket back into a string.

2. What changes would you have to make to create a UDP socket?
    The changes that must be made to create a UDP socket are that the "SOCK_STREAM" parameter on line 24 would have to be changed to "SOCK_DGRAM" when I create the socket. Also instead of using send() and recv() functions I would use sendto() and recvfrom() functions.

3. If you wanted to create a TCP server, what would you have to change?
    I would have to use the socket() function with the AF_INET and SOCK_STREAM for a TCP server. Then after I do that I would need to bind the socket to a specific address and port and use thr listen() call after so that way the socket gets any incoming connections. Finally, need an accept() function to allow the incoming connection.

4. Can your TCP client create or process HTTPS traffic? What happens if you send a request to port 443?
    Yes it can create and process HTTPS traffic and if I send it to port 443 it'll work because that is where data is sent and recieved. 




How the code works:
    I first start off by checking if either "-p" or "-f" is entered. Then, depending on what is entered it'll print out the result or it will make a file named "output.txt" and put the result in there(lines 12-19). 
    Next, I create a TCP socket that will connect to a server in lines 27 and 28. After, I construct and send the HTTP GET request in lines 30 and 31, then it is decoded in line 33, and from lines 35-37 it'll then close the socket then return the result.