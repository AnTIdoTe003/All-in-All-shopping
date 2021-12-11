from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("Welcome to the shopping webapp ")
print("Enter the choice of your website ")
print("1. Amazon\n2. Flipkart ")
choice=int(input())

if(choice==1):
    print("What do you want to search for ")
    search_amazon=input()
    PATH = "ENTER THE PATH WHERE YOU HAVE DOWNLOADED THE RESPECTIVE CHROME DRIVER"
    driver = webdriver.Chrome(PATH)
    driver.get("https://amazon.in")
    search =driver.find_element_by_id("twotabsearchtextbox")
    search.send_keys(search_amazon)
    search.send_keys(Keys.RETURN)
elif(choice == 2):
    print("What do you want to search for ")
    search_flipkart=input()
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://flipkart.com")
    search =driver.find_element_by_name("q")
    search.send_keys(search_flipkart)
    search.send_keys(Keys.RETURN)
else:
    print("Invalid Choice")









