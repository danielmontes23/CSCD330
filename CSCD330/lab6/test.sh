#!/bin/bash
sudo iptables -I OUTPUT -p tcp --tcp-flags ALL RST -j DROP
sudo tcpdump -i any -w test.pcap & TCPDUMP_PID=$!

sudo python3 lab6.py http://httpforever.com/
echo
python3 lab6.py http://www.cs.sjsu.edu/~pearce/modules/lectures/web/html/HTTP.htm
echo
python3 lab6.py http://amazon.com/
sudo kill $TCPDUMP_PID
sudo iptables -D OUTPUT -p tcp --tcp-flags ALL RST -j DROP
