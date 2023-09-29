from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from threading import Event
import csv


# options for our web scraper
chrome_options = Options()
chrome_options.add_argument("--headless")

# the driver for our web scraper
DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=chrome_options)
driver.get('https://mycurrentlocation.net/')

Event().wait(3)
driver.find_element(
    By.CSS_SELECTOR, ".btn.btn-warning.mt-3.main-button").click()
Event().wait(1)
latitude = driver.find_element(By.ID, "detail-latitude").text
longitude = driver.find_element(By.ID, "detail-longitude").text

print(latitude, longitude)


latitude = str(latitude).replace('.', ',')
longitude = str(longitude).replace('.', ',')


URL = 'https://www.pogomap.info/location/' + latitude + '/' + longitude+'/16'
print(URL)
driver.get(URL)

# opens a csv file to write to
file = open("pokeStops.csv", 'w')
writer = csv.writer(file)
writer.writerow(["START", latitude + ',' + longitude])

# list to store relevant datum
stops = []

# initializes the pogo website with location list extended
Event().wait(1)
driver.find_element(By.CSS_SELECTOR, '.closeIcon').click()
driver.find_element(By.CSS_SELECTOR, '[title="Location List"]').click()
stops = driver.find_elements(
    By.CSS_SELECTOR, '.loclistitem-hold.tooltipstered')

# iterates through each element of the list and stores the relevant datum
for i in stops:
    i.click()
    stopName = i.text
    Event().wait(1)
    driver.find_element(By.CSS_SELECTOR, ".fa.fa-info-circle").click()
    Event().wait(1)
    stopCoordinates = driver.find_elements(
        By.CSS_SELECTOR, "[style='margin-top:2px;']")[1].text
    driver.find_element(By.CSS_SELECTOR, '.closeIcon').click()
    driver.find_elements(By.CSS_SELECTOR, ".fa.fa-times")[2].click()
    writer.writerow([stopName, stopCoordinates])

print("done scraping!")
