#!/usr/bin/env python3
# Author: Daniel Montes

from urllib.parse import urlparse
from scapy.all import *
from socket import gethostbyname
from sys import argv

def perform_three_way_handshake(target_host, target_port):
    # Get user's first name for initial seq number
    first_name = "Daniel"
    seq_num = len(first_name)

    # Generate a random source port
    src_port = RandShort()

    # Create SYN packet
    syn_packet = IP(dst=target_host) / TCP(dport=target_port, sport=src_port, flags='S', seq=seq_num)
    syn_ack_packet = sr1(syn_packet)

    # Extract seq and ack numbers
    ack_num = syn_ack_packet[TCP].seq + 1
    my_seq_num = syn_ack_packet.ack

    # Create ACK packet
    ack_packet = IP(dst=target_host) / TCP(dport=target_port, sport=src_port, flags='A', seq=my_seq_num, ack=ack_num)
    send(ack_packet)

    return src_port, my_seq_num, ack_num
def send_get_request(target_host, target_port, target_path, src_port, my_seq_num, ack_num):
    # Build GET request string
    get_request = f"GET {target_path} HTTP/1.1\r\nHost: {target_host}\r\n\r\n"

    # EXTRA CREDIT
    # fin = IP(dst=target_host) / TCP(sport=src_port, dport=target_port, flags='FA', seq=ack_num + len(get_request), ack=ack_num + 1)
    # fin_ack = sr1(fin, timeout=5)
    # last_ack = IP(dst=target_host) / TCP(sport=src_port, dport=target_port, flags='A', seq=fin_ack.ack, ack=fin_ack.seq + 1)
    # send(last_ack)

def main():
    if len(argv) != 2:
        print("Usage: sudo python3 script.py <url>")
        return

    target_url = argv[1]
    target_parsed = urlparse(target_url)
    target_host = gethostbyname(target_parsed.hostname)
    target_port = 80
    target_path = target_parsed.path or "/"

    # Perform three-way handshake
    src_port, my_seq_num, ack_num = perform_three_way_handshake(target_host, target_port)

    # Send GET request
    send_get_request(target_host, target_port, target_path, src_port, my_seq_num, ack_num)


if __name__ == "__main__":
    main()

