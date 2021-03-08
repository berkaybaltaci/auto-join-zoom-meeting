'''  
This was only tested on a 1080p windows machine. It will not work for different resolutions since a part of this script uses coordinates to click. 
On small screens or laptops make sure to set scaling to 100%.
If the script doesn't seem to work properly, launching cmd as administrator and running the script in the console might help.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time
import schedule
import pyautogui
import os
import smtplib
import inspect
import random

from dotenv import load_dotenv
load_dotenv()

username = os.getenv('USRNAME')
password = os.getenv('PASSWORD')


def sendMail(current_function_name):
    senderMail = os.getenv('SENDER_MAIL')
    recMail = os.getenv('REC_MAIL')
    senderPass = os.getenv('SENDER_MAIL_PASSWORD')
    message = f'''\
Subject: Auto join failure

Function "{current_function_name}" failed.'''

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(senderMail, senderPass)
    server.sendmail(senderMail, recMail, message)


def getToDerslerim():

    # Kill all chrome processes to prevent any bugs
    os.system("taskkill /im chrome.exe /f")
    time.sleep(5)
    # Kill all zoom processes to prevent any bugs
    os.system("taskkill /im Zoom.exe /f")
    time.sleep(5)

    url = 'https://online.yildiz.edu.tr/'

    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

    time.sleep(2)

    secenekler = driver.find_element_by_xpath('//*[@id="Data_AccountType"]')
    secenekler.send_keys(Keys.ENTER)
    time.sleep(1)
    secenekler.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    secenekler.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    secenekler.send_keys(Keys.ENTER)
    time.sleep(2)

    kullanici_adi = driver.find_element_by_xpath('//*[@id="Data_Mail"]')
    kullanici_adi.send_keys(username)

    time.sleep(1)

    sifre = driver.find_element_by_xpath('//*[@id="Data_Password"]')
    sifre.send_keys(password)

    time.sleep(1)

    giris_butonu = driver.find_element_by_xpath(
        '//*[@id="Information"]/div[4]/div[2]/button')
    giris_butonu.click()

    time.sleep(15)

    derslerim_butonu = driver.find_element_by_xpath(
        '//*[@id="app-container"]/div[4]/div[1]/div/ul/li[2]/a/i')
    derslerim_butonu.click()

    time.sleep(2)

    return driver


def pyClicker():
    time.sleep(15)

    # Had to use pyautogui and absurd amounts of delay with time.sleep() since website is buggy with selenium here
    pyautogui.moveTo(1440, 552)
    time.sleep(2)
    pyautogui.click()

    time.sleep(15)

    # Clicking the same button again in case of any bugs/internet issues
    pyautogui.moveTo(1440, 552)
    time.sleep(2)
    pyautogui.click()

    time.sleep(30)

    pyautogui.moveTo(1050, 220)
    time.sleep(2)
    pyautogui.click()
    time.sleep(10)


def ed1lab_func():
    try:
        driver = getToDerslerim()
        ed1lab_butonu = driver.find_element_by_xpath(
            '//*[@id="app-container"]/div[4]/div[2]/div/ul/li[6]/a/span[2]')
        ed1lab_butonu.click()

        time.sleep(5)

        canli_ders_butonu = driver.find_element_by_xpath(
            '//*[@id="menu-3c7b6e0b-74ec-4d63-b2de-937aeddbe69c"]/ul/li[2]/a/span')
        action = ActionChains(driver)
        action.move_to_element(canli_ders_butonu).click().perform()

        pyClicker()

        driver.quit()
    except:
        print('Fonksiyon calismadi.', datetime.now())
        current_function_name = inspect.currentframe().f_code.co_name
        sendMail(current_function_name)


def emat_func():
    try:
        driver = getToDerslerim()
        emat_butonu = driver.find_element_by_xpath(
            '//*[@id="app-container"]/div[4]/div[2]/div/ul/li[1]/a/span[2]')
        emat_butonu.click()

        time.sleep(5)

        canli_ders_butonu = driver.find_element_by_xpath(
            '//*[@id="menu-342f6561-d04a-49cb-903a-d772cdaafdd8"]/ul/li[2]/a/span')
        action = ActionChains(driver)
        action.move_to_element(canli_ders_butonu).click().perform()

        pyClicker()

        driver.quit()
    except:
        print('Fonksiyon calismadi.', datetime.now())
        current_function_name = inspect.currentframe().f_code.co_name
        sendMail(current_function_name)


def networking_func():
    try:
        driver = getToDerslerim()
        networking_butonu = driver.find_element_by_xpath(
            '//*[@id="app-container"]/div[4]/div[2]/div/ul/li[7]/a/span[2]')
        networking_butonu.click()

        time.sleep(5)

        canli_ders_butonu = driver.find_element_by_xpath(
            '//*[@id="menu-82e5d5ca-9d0e-422b-a110-a7fb77afc051"]/ul/li[2]/a/span')
        action = ActionChains(driver)
        action.move_to_element(canli_ders_butonu).click().perform()

        pyClicker()

        driver.quit()
    except:
        print('Fonksiyon calismadi.', datetime.now())
        current_function_name = inspect.currentframe().f_code.co_name
        sendMail(current_function_name)


def mikrodalga1_func():
    try:
        driver = getToDerslerim()
        mikrodalga1_butonu = driver.find_element_by_xpath(
            '//*[@id="app-container"]/div[4]/div[2]/div/ul/li[4]/a/span[2]')
        mikrodalga1_butonu.click()

        time.sleep(5)

        canli_ders_butonu = driver.find_element_by_xpath(
            '//*[@id="menu-d31dad9d-4299-4782-89f0-0d5ca46dbbb9"]/ul/li[2]/a/span')
        action = ActionChains(driver)
        action.move_to_element(canli_ders_butonu).click().perform()

        pyClicker()

        driver.quit()
    except:
        print('Fonksiyon calismadi.', datetime.now())
        current_function_name = inspect.currentframe().f_code.co_name
        sendMail(current_function_name)


def hab1_func():
    try:
        driver = getToDerslerim()
        hab1_butonu = driver.find_element_by_xpath(
            '//*[@id="app-container"]/div[4]/div[2]/div/ul/li[5]/a/span[2]')
        hab1_butonu.click()

        time.sleep(5)

        canli_ders_butonu = driver.find_element_by_xpath(
            '//*[@id="menu-c00a74a3-7783-462c-b085-f26fac04cba5"]/ul/li[2]/a/span')
        action = ActionChains(driver)
        action.move_to_element(canli_ders_butonu).click().perform()

        pyClicker()

        driver.quit()
    except:
        print('Fonksiyon calismadi.', datetime.now())
        current_function_name = inspect.currentframe().f_code.co_name
        sendMail(current_function_name)


def ed2_func():
    try:
        driver = getToDerslerim()
        ed2_butonu = driver.find_element_by_xpath(
            '//*[@id="app-container"]/div[4]/div[2]/div/ul/li[3]/a/span[2]')
        ed2_butonu.click()

        time.sleep(5)

        canli_ders_butonu = driver.find_element_by_xpath(
            '//*[@id="menu-644bf049-fe5c-4543-a148-c218e5533f82"]/ul/li[2]/a/span')
        action = ActionChains(driver)
        action.move_to_element(canli_ders_butonu).click().perform()

        pyClicker()

        driver.quit()
    except:
        print('Fonksiyon calismadi.', datetime.now())
        current_function_name = inspect.currentframe().f_code.co_name
        sendMail(current_function_name)


def lojik_func():
    try:
        driver = getToDerslerim()
        lojik_butonu = driver.find_element_by_xpath(
            '//*[@id="app-container"]/div[4]/div[2]/div/ul/li[2]/a/span[2]')
        lojik_butonu.click()

        time.sleep(5)

        canli_ders_butonu = driver.find_element_by_xpath(
            '//*[@id="menu-223c1698-4649-492f-8a61-8f6eb80f8535"]/ul/li[2]/a/span')
        action = ActionChains(driver)
        action.move_to_element(canli_ders_butonu).click().perform()

        pyClicker()

        driver.quit()
    except:
        print('Fonksiyon calismadi.', datetime.now())
        current_function_name = inspect.currentframe().f_code.co_name
        sendMail(current_function_name)


def turkce1_func():
    try:
        driver = getToDerslerim()
        turkce1_butonu = driver.find_element_by_xpath(
            '//*[@id="app-container"]/div[4]/div[2]/div/ul/li[9]/a/span[2]')
        turkce1_butonu.click()

        time.sleep(5)

        canli_ders_butonu = driver.find_element_by_xpath(
            '//*[@id="menu-30d3c3c4-d0a0-4e16-9d72-fb49f47eaff1"]/ul/li[2]/a/span')
        action = ActionChains(driver)
        action.move_to_element(canli_ders_butonu).click().perform()

        pyClicker()

        driver.quit()
    except:
        print('Fonksiyon calismadi.', datetime.now())
        current_function_name = inspect.currentframe().f_code.co_name
        sendMail(current_function_name)


# randomize join time and schedule attendance
def randomizeJoinTime(baseTime):
    return baseTime + str(random.randint(4, 9))

joinTime = randomizeJoinTime("10:0")
schedule.every().monday.at(joinTime).do(ed2_func)

joinTime = randomizeJoinTime("09:0")
schedule.every().wednesday.at(joinTime).do(ed2_func)

joinTime = randomizeJoinTime("13:0")
schedule.every().monday.at(joinTime).do(hab1_func)

joinTime = randomizeJoinTime("15:0")
schedule.every().thursday.at(joinTime).do(networking_func)

joinTime = randomizeJoinTime("14:0")
schedule.every().friday.at(joinTime).do(mikrodalga1_func)

joinTime = randomizeJoinTime("12:0")
schedule.every().tuesday.at(joinTime).do(emat_func)


print('*** OLCEGI %100 YAPMAYI UNUTMA ***')
print('*** OLCEGI %100 YAPMAYI UNUTMA ***')
print('*** YONETICI OLARAK CALISTIRMAYI UNUTMA ***')
print('*** YONETICI OLARAK CALISTIRMAYI UNUTMA ***')


while True:
    schedule.run_pending()
    time.sleep(5)
