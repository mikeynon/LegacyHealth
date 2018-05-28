import datetime
import schedule
import requests
import random
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
usernameStr = 'cliefer'
passwordStr = 'Stewie5!'
browser = webdriver.Chrome()
browser.get(('https://mytimeremote.lhs.org/APIHC/TASS/WebPortal/APIHealthcare/Login.aspx'))
# fill in username and hit the next button
username = browser.find_element_by_id('formContentPlaceholder$_userNameField')
username.send_keys(usernameStr)
password = browser.find_element_by_id('formContentPlaceholder$_passwordField')
password.send_keys(passwordStr)
nextButton = browser.find_element_by_id('formContentPlaceholder_loginApiButton')
nextButton.click()

