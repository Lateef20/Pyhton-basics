
from bs4 import BeautifulSoup as bs # travels html text
#form urllib3.request import urlopen  dont know why this does not work. this code does not import all of urllib beucse we dont needed the whole packege, th ecode specifes what part of pakcage we need
import urllib3
import requests #can use either request or urlib
import csv
from selenium import webdriver

#with open ("C:\\Apps\\html\\index.html", "r") as html_file:
#    content = html_file.read()
#    print(content)
#for locally stored html

driver = webdriver.Chrome()
url='https://www.zalando.co.uk/mens-shoes-trainers/?order=sale'
driver.get(url)

html_text = requests.get('https://uk.indeed.com/Computer-Science-Graduate-jobs-in-London')
#html_text = requests.get('https://www.zalando.co.uk/mens-shoes-trainers/?order=sale')
soup = bs(html_text.content,'html.parser')
food= soup.find_all(class_="salaryText")
foods= soup.find_all(style="margin-bottom:0px;")
print(food)
print(foods)
