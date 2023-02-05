from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from threading import Event

chrome_options = Options()
#chrome_options.add_argument("--headless")

DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH,options=chrome_options)
driver.get('https://www.pogomap.info/location/42,250186/-83,610131/16')

stops = []
stopCoordinates = []
stopNames = []

Event().wait(1)
driver.find_element(By.CSS_SELECTOR, '.closeIcon').click()
driver.find_element(By.CSS_SELECTOR, '[title="Location List"]').click()
stops = driver.find_elements(By.CSS_SELECTOR, '.loclistitem-hold.tooltipstered')

for i in stops : 
    i.click()
    stopNames.append(i.text)
    Event().wait(1)
    driver.find_element(By.CSS_SELECTOR, ".fa.fa-info-circle").click()
    Event().wait(1)
    stopCoordinates.append(driver.find_elements(By.CSS_SELECTOR, "[style='margin-top:2px;']")[1].text)
    driver.find_element(By.CSS_SELECTOR, '.closeIcon').click()

for i in range(0, len(stopNames)) :
    print(stopNames[i])
    print(stopCoordinates[i])