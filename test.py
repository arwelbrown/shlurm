from selenium import webdriver
import time

driver = webdriver.Chrome()

def loop():
    while True:
        driver.get("https://shlurm.herokuapp.com/")
        time.sleep(300)

loop()