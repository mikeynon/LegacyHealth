from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
usernameStr = 'putYourUsernameHere'
passwordStr = 'putYourPasswordHere'import datetime
import schedule
import requests
import random
from bs4 import BeautifulSoup

today = datetime.datetime.now().strftime("%m/%d/%y")
shift = "0700-12"
soup = requests.get(url)
data = BeautifulSoup(soup, 'html.parser')
if TypeError:
    print()
else:
    print(data)
