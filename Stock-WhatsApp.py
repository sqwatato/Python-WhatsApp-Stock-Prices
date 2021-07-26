#To get Website
import requests

#To scrape data from Website
from bs4 import BeautifulSoup

#To send message through WhatsApp
#Must be logged into WhatsApp on your computer
import pywhatkit as kit

#To get date (Optional)
from datetime import date



#Search My User Agent in Chrome and copy paste with 'Modzilla...Safari/537.36'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}



#Taking Stock Data From Yahoo Finance
yahoo = 'https://finance.yahoo.com/quote/'



#List of Stocks
#You can use File IO as well
#Add Stock Symbol, not full name
stocks = ['googl','nvda','rblx','aapl','snap']



#Get Today's Date
today = date.today()

#Format the Date
today_date = today.strftime("%B %d, %Y")



#The Message you want to send
message = """"""

#Adding some info
message += 'Jaydens Stock Price WeChat Bot\n'

#Add Date
message += today_date + ' Stock Prices: \n'
message += '\n'



#Get Data for all stocks in stock list
for stock in stocks:

    #Get Specific Website Url for Stock
    #Ex: https://finance.yahoo.com/quote/googl
    url = yahoo + stock

    #Get Website
    r = requests.get(url,headers=headers)

    #Get Html
    soup = BeautifulSoup(r.content,'html.parser')


    #Find Specific Html Element with Class "..."
    #Then find the text in the Element (Which is where the Name or Price text is)
    #All the Data has it's own Html Element with a special class
    #The find Function finds the element with the unique class
    #Then the .text gets the text, or the actual date
     
    #Get Full Name of Stock  
    name = soup.find(class_='D(ib) Fz(18px)').text

    #Get Current Price
    price = soup.find(class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text

    #Get Change in Price and Percent from Yesterday
    change = soup.find(class_='D(ib) Mend(20px)').find_all('span')[1].text

    #Add Data to the Message
    message += name + '\n'
    message += 'Price: ' + price + '\n'
    message += 'Change: ' + change + '\n'
    message += '\n'

#Replace 1 with country code for phone number
#Ex: US number is 1
country_code = '1'

#Replace with Phone Number used for WhatsApp
phone_number = '1234567890'

#Send Message
#Have Chrome open when running the program
#It will open a Chrome Tab and open WhatsApp from there
#You have to be logged in for it to work
#Then it will send the message to the Phone Number
#Make sure to wait 5 seconds

#The 5 right here ------------------------------------------------|
#Is the amount of seconds of delay before sending the message
#Make sure to leave at least 1 second of delay because your computer needs to load
#Feel free to change the 5 to a different number
kit.sendwhatmsg_instantly('+' + country_code+phone_number,message,5)

#Let me know if it doesn't work or if I should change anything
#Yahoo Finance might eventually change their website structure which could mess up the code
#Send me an Email if you have any problems or if it works!
#My Email: sqwatato@gmail.com