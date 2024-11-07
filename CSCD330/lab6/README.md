Questions:
1. In lab 4 you sent a GET request using the sockets library. What did the sockets library do for you?
    In lab 4 the sockets library helped me create a TCP socket and connected it to the server. Then it constructed and sent the HTTP GET request, then decoded it and returned the results of the message.

2. Before you submit this lab, you should check that your pcap contains the correct traffic. What program should you use to analyze your pcap? In your pcap, did the server send you the complete HTML for the website or just a portion of the HTML? (Does the response end with a </html> tag?)
    Wireshark is the program used to analyze my pcap file. The server will send multiple portions until we stop recieving or recieve all of the portions of the HTML.

3. Is your program guaranteed to receive a complete HTML response from the website? Why or why not.
    The code will not receive a complete HTML response because of packet loss the threeway handshake is initiated. If the server takes to long to respond the program may quit before it recieves the response.

4. Can you merge the final ACK of the three-way handshake with the GET request?     
That is, can you merge the two packets into one? If yes, explain how such an option might be beneficial.
    It is possible to merge the final ACK of the 3 way handshake with the GET request. It could help transfer data faster because it reduces the time. Which is key for performance so they all tie together but are benefical possibilities of merging the two packets.

5. Can scapy be used to send other types of packets? If yes, give an example.
    Yes, scapy can be used to send other types of packets. It is able to construct a packet/s from nothing. You can send ethernet frames, IPv4 and IPv6 packets, TCP, UDP, etc. The thing is it must be defined in the code for it to be able to send the typeof packet you want.

How my code works: (EXTRA CREDIT ATTEMPTED)
    My code starts off by disabling IPv6 on line 10. Then, it moves onto performing the three way handshake from lines 12-32. It'll ask for a sequence number. 

    Next, it generated a random source port then after created the SYN packet. It extracts the sequence number and then creates the ACK packet. 

    After, it will send a get request first builds it, creates the TCP packet, and then prints the HTTP response. Next on lines 46-48 is where it is suppose to close the connection. Finally, it'll perform the handshake and then send the get request from lines 61-65.

    Lines 45-47 is where I tried to close the connection.