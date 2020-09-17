from selenium import webdriver
import time
link=str(input("Enter the link of your youtube video\n"))
views=int(input("Enter the amount of views that you want to fake\n"))

viewtime=float(input("Enter the duration time for each view\n"))

browser=webdriver.Firefox() 

for i in range(views):
    browser.get(link)
    time.sleep(viewtime)
    
browser.close()

