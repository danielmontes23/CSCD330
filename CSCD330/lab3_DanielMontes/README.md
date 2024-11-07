Questions:
1. Identify the following in the URL: http://localhost:5000/weather/google.com 
• Domain: The domain is Google.com.
• Path: The path is /weather.
• Port: The port is 5000.
• Protocol: The protocol is http.

2. Identify the following in the URL: https://translate.google.com/
• Domain: The domain is google.com as well.
• Subdomain: The subdomain is translate.
• TLD: The TLD is .com.
• Path: The path is /.
• Protocol: The protocol is https.
• Port: The port is 443.

3. What is a Python decorator?
A python decorator is a powerful feature within the language Python which allows you to modify or extend functions without changing code inside their methods to make it print that specifically. It is reusable functionality that will work on multiple methods and functions such as timing, caching, logging, and or authentication. You use the decorator when you need to assign more behaviors to objects inside your code without breaking the objects.

4. Is there any problem with your cache implementation? Would your cache
implementation work in production?
Im sure there probably is an issue whether it is small or big in my cache implementation and it may or may not cause issues if used in production. As of now I do not have any errors as of now my code is not warning me or showing me issues with the caching.





How my code works:
My code works similar to lab 2 because we start off by getting the IP address for the domain and cashing the domain name. Similar to lab 2 we got the IP address then we retrieve the weather data and cache it as well. Next, we move onto retrieving the weather forecast by using the same link we used in the previous lab.

After we retrieve the IP address and the detailed forecast we will move onto getting the physical address including the street, city, state, and zip code. We used the line.split to split the address into the format that is expected. When the address is retrieved we will then try and get the coordinates of the address which is the next method followed by another few methods already included with the lab.

Some differences in this code are lines 13 and 14 I used a cache = {} twice. One for the weather and one for the address they are called in the get_WeatherData method and then in def address method. It will return the regular address and if you refresh the page it'll reprint the same address with "cache:" infront. It is the same thing for the weather, it'll print the forecast then refresh the page and it'll be the same but with "cache:" infront.