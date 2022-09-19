from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome('/media/zft/HDD1T/projects/Zr413/Zr413/chromedriver')
driver.get('https://ya.ru')
(driver.find_element(By.XPATH, '/html/body/main/div[4]/img')).click()
sleep(3)
# driver.save_screenshot('sf.png')
driver.quit()
