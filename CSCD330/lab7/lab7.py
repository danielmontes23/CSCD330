#!/usr/bin/env python3
# Author: Daniel Montes

from scapy.all import *
from socket import gethostbyname
from subprocess import getstatusoutput
from sys import argv


def main():
    if len(argv) != 3:
        print("Usage: sudo python3 script.py <url> <maxHops>")
        return

    url = argv[1]
    try:
        target_IP = gethostbyname(url)
    except Exception as e:
        print(f"Error finding URL {url}: {e}")
        return

    try:
        maxHops = int(argv[2])
    except ValueError:
        print("Error: maxHops must be an int.")
        return

    print(f"Route to {url} ({target_IP}), {maxHops} hops max")

    as_nums = []
    ttl = 1
    as_number = ""

    while ttl <= maxHops:
        packet = IP(dst=target_IP, ttl=ttl) / ICMP()
        reply = sr1(packet, verbose=0, timeout=3)

        if reply is None:
            print(f"{ttl} - * * *")
            ttl += 1
            continue

        hopIP = reply.src
        print(f"{ttl} ({hopIP})")

        # whois command to lookup and get AS number
        status, output = getstatusoutput(f"whois {hopIP}")
        #as_number = "AS not found"
        for line in output.splitlines():
            if "originAS" in line.lower():
                parts = line.split(':')
                if len(parts) > 1:
                    as_number = parts[1].strip()
                    break

        if as_number != "AS not found" and as_number not in as_nums:
            as_nums.append(as_number)

        if reply.src == target_IP:
            break

        ttl += 1

    # Print the chain of traversed ASs and it should remove any duplicates. Also, will handle an empty case.
    if as_nums:
        print(f"Traversed AS numbers:", " -> ".join(as_nums))
    else:
        print(f"No traversed AS numbers were found for {url}.")


if __name__ == "__main__":
    main()