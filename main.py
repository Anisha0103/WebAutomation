import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")
time.sleep(5)

FirstName = driver.find_element(By.XPATH, "//input[@id='fname']")
FirstName.send_keys("Anisha")
time.sleep(3)

LastName = driver.find_element(By.XPATH, "//input[@name='Last Name']")
LastName.send_keys("Dhanwada")
time.sleep(3)

Dateofbirth = driver.find_element(By.XPATH, "//input[@name='Date of Birth']")
Dateofbirth.send_keys("2003-05-01")
time.sleep(3)

Mobilenumber = driver.find_element(By.XPATH, "//input[@id='mobile']")
Mobilenumber.send_keys("9876543210")
time.sleep(3)

Email = driver.find_element(By.XPATH, "//input[@id='email']")
Email.send_keys("anishadhanwada@gmail.com")
time.sleep(3)

Country = driver.find_element(By.XPATH, "//input[@id='country']")
Country.send_keys("India")
time.sleep(3)

#Switching to frame 1
driver.switch_to.frame(1)

FirstName = driver.find_element(By.XPATH, "//input[@id='fname']")
FirstName.send_keys("Anisha")
time.sleep(3)

LastName = driver.find_element(By.XPATH, "//input[@name='Last Name']")
LastName.send_keys("Dhanwada")
time.sleep(3)

Dateofbirth = driver.find_element(By.XPATH, "//input[@name='Date of Birth']")
Dateofbirth.send_keys("2003-05-01")
time.sleep(3)

Mobilenumber = driver.find_element(By.XPATH, "//input[@id='mobile']")
Mobilenumber.send_keys("9876543210")
time.sleep(3)

Email = driver.find_element(By.XPATH, "//input[@id='email']")
Email.send_keys("anishadhanwada@gmail.com")
time.sleep(3)

#Switching to frame 2
driver.switch_to.default_content()
driver.switch_to.frame(2)

FirstName = driver.find_element(By.XPATH, "//input[@id='fname']")
FirstName.send_keys("Anisha")
time.sleep(3)

LastName = driver.find_element(By.XPATH, "//input[@name='Last Name']")
LastName.send_keys("Dhanwada")
time.sleep(3)

Dateofbirth = driver.find_element(By.XPATH, "//input[@name='Date of Birth']")
Dateofbirth.send_keys("2003-05-01")
time.sleep(3)

Mobilenumber = driver.find_element(By.XPATH, "//input[@id='mobile']")
Mobilenumber.send_keys("9876543210")
time.sleep(3)

Email = driver.find_element(By.XPATH, "//input[@id='email']")
Email.send_keys("anishadhanwada@gmail.com")
time.sleep(3)
driver.close()