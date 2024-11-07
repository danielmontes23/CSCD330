Questions:

1. What is an API?
API stands for "Application Programming Interface", which are a set of rules and protocols that the software uses in order to communicate with each other. It also enables different software applications and systems to work together even if they were built separately with different technology. APIs are also used by developers so that they can build systems without struggling as much because they are able to look at the API as a guide or for more information how to write certain methods.

2. What is a RESTful API? Were the APIs we used RESTful? 
A RESTful API stands for a Representation State Transfer which is an architectural style used for the API. We did in fact use RESTful APIs because a RESTful API is commonly used for web services. We used two URLs in our code help get the data of the weather, then used JSON after the data was retrieved to format the output.

3. What is JSON? Did these APIs use JSON?
JSON stands for JavaScript Object notation and it is used to interchange formatting making it easier for people to read, write, and easier for machines to parse. It is also used to transfer data between a server and a client or from a website application. Yes we did use JSON in these APIs it was also imported to our code because it was needed to help run and compile the code.

4. What is Bash? Have you ever used Bash?
I have never personally used Bash while coding but I have heard of it when I took C and Unix during Winter 2022. The word bash stands for "Bourne Again Shell" which is a unix command used to line shell and script language. It can be used for system administrations, software development, and automation tasks. The bash command has lots of support and is flexible for scripting and command execution.

Code Logic:

In the first part of the code it retrieves the IP address from the domain and prints the IP, then we move onto retrieving the physical address by using the WHOIS command and the IP address. If it cannot retrieve the IP it'll print out saying failure to execute the whois command but it does it'll print out WHOIS out for IP. Next, in my code I use the WHOIS output to find the physical address and splitting it up by street, city, state, and zip code. After, it splits it up and goes through the lines in the output it prints out the street, city, state, and zip code in that exact order every time. 

Then, we had to get the coordinates of the places being geolocated and print them out as well. With that I also retrieved the weather data for the coordinates retrieved. When every piece of information is pulled it will first print out the IP address and then the physical address in a certain format and the final lines will include the URL that was looked up, the coordinates of the address, and the forecast for the area around those coordinates. 

At the end of the code I had my main where it will print out failed to retrieve physical address if the code is not allowed to get it and after that it will print out in a certain format the detailed forecast of the area.

I also include little comments in my code to try and help the user or myself understand what is happening at certain parts in the code. I tried keeping the comments short to help it look better/organization and so I do not get confused if I see a chunk of words above my code.