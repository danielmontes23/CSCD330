Questions:
1. Besides TCP, what other protocols can be used for a traceroute tool?
    An Internet Control Message Protocol(ICMP) in layer 3 can also be used as a traceroute tool because a traceroute works by sending ICMP packets and routers involved in transferring data. Also, a UDP in layer 4 can be a traceroute tool.

2. When traversing to a website, does the path remain constant every time?
    When traversing a website the path DOES NOT remain the same. It is because of the way the website was built and when navigating through the website you can see the URL change whenever you move around different sections of the website.

3. If a packet dies before reaching the target website, what type of packet is
returned?
    If the packet dies or is discarded then it should send an ICMP time exceeded message to the person to let them know it timed out trying to receive the packet.

4. Can the whois command be used to discover the owner of an AS number?
    The WHOIS command can be used to help discover the owner of an AS number because it is used to do domain lookups. You could use the command "WHOIS " + ASN number and it should be able to tell you the owner, location, etc. of the ASN.






How my code works:
    My code starts off by telling you how to run the code. Then, it gets the host name using the URL and max hops. Once it does that it'll print and return "Route to {url} (IP address), {maxHops} hops max." 

    After, it will run the whois command and get the AS number, if not found the code will let you know. Then, it will finally print and return the traversed AS numbers like this "Traversed AS numbers: " and if none are found it will print like this "No traversed AS numbers were found for {url}."