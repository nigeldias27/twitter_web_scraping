from selenium import webdriver
import time
from bs4 import BeautifulSoup
from datetime import date
import openpyxl 

browser=webdriver.Chrome()
wb = openpyxl.load_workbook("nooftweets.xlsx") 
sheet = wb.active 
f=open("users.txt",'r')
today_date = date.today()
data=[]
for x in f.readlines():
    browser.get("https://twitter.com/"+x)
    scroll_loop=True
    i=0
    l=[]
    while (scroll_loop):
        time.sleep(10)
        html = browser.page_source
        soup = BeautifulSoup(html,'html.parser')
        mytime = soup.find_all('time')
        for times in mytime:
            if(times['datetime'][0:10]!=today_date):
                scroll_loop=False
                data.append((x,today_date,len(l)))
                break
            else:
                if(times not in l):
                    l.append(times)
        i=i+50
        browser.execute_script("window.scrollBy(0,"+str(i)+")")
f.close()
browser.close()
for row in data:
    sheet.append(row)
  
wb.save('nooftweets.xlsx')

#saanvikumar1311