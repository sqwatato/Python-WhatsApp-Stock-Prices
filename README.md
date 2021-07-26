# WhatsApp-Stock-Prices
A Python program that sends stock prices to given WhatsApp account. 

# How it Works 
It's pretty simple.  
PS: Sorry about the English, I don't exactly know how to explain it well.  

It first loops through the list of stocks and for every stock, it gets the Yahoo finance website for that stock using requests. 
Then it uses BeautifulSoup to scrape the stock data by searching for the element containing the data and then grabbing the data and storing it in a variable.  
After that, it adds the data to a message.
It does it for every stock.  
After it finishes, it sends a message to the given phone number of the stock data.  

Make sure you have the Libraries(or Modules idk what they are) downloaded before you run it.  
I used pipenv but you can do whatever you want.  

Please email me if you have anything questions/suggestions or if the program ran smoothly! Anything is Appreciated.  
Email: sqwatato@gmail.com

