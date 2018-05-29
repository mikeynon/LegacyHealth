import schedule, time, requests, random, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'XXX'
passwordStr = 'XXX'

def job():
    print("Starting Scheduler...")
    browser = webdriver.Chrome()
    browser.get(('https://mytimeremote.lhs.org/APIHC/TASS/WebPortal/APIHealthcare/Login.aspx'))
    # fill in username and hit the next button
    username = browser.find_element_by_id('formContentPlaceholder$_userNameField')
    username.send_keys(usernameStr)
    password = browser.find_element_by_id('formContentPlaceholder$_passwordField')
    password.send_keys(passwordStr)
    nextButton = browser.find_element_by_id('formContentPlaceholder_loginApiButton')
    nextButton.click()
    print("Logging in...")
    # wait for transition then continue to fill items
    sectionButton = WebDriverWait(browser, 35).until(
        EC.presence_of_element_located((By.ID, 'sections.employee')))
    selfSectionButton = browser.find_element_by_id('sections.employee')
    selfSectionButton.click()
    print("Entering Employee Section...")

    selfSched = WebDriverWait(browser, 35).until(
        EC.presence_of_element_located((By.ID, 'formContentPlaceholder_selfScheduleApiButton')))
    selfSchedButton = browser.find_element_by_id('formContentPlaceholder_selfScheduleApiButton')
    selfSchedButton.click()
    print("Entering Self-Scheduler...")


schedule.every(6).sunday.at("00:01").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
