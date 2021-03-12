import inspect
import os
import smtplib
import time
from datetime import datetime

import pyautogui
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

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


def coordinateClicker():
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


def generateSubjectFunc(ders_butonu_path, canli_ders_butonu_path):

    def subjectFunction():
        try:
            driver = getToDerslerim()
            ders_butonu = driver.find_element_by_xpath(ders_butonu_path)
            ders_butonu.click()

            time.sleep(5)

            canli_ders_butonu = driver.find_element_by_xpath(canli_ders_butonu_path)
            action = ActionChains(driver)
            action.move_to_element(canli_ders_butonu).click().perform()

            coordinateClicker()

            driver.quit()
        except:
            print('Fonksiyon calismadi.', datetime.now())
            current_function_name = inspect.currentframe().f_code.co_name
            sendMail(current_function_name)

    return subjectFunction
