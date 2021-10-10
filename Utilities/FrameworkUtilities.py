import os
from selenium import webdriver

cwd = os.getcwd()

def launchBrowser(browsername):
    if browsername == "Chrome":
        driver = webdriver.Chrome(cwd+"Resources/ChromeDriver.exe")
        return driver
    #elif browsername == "Firefox":
     #   driver = webdriver.Firefox(cwd/Resources/geckodriver.exe)


