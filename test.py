from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os


website = "https://www.adamchoi.co.uk/corners/detailed"

driver = webdriver.Chrome()
driver.get(website)


all_matches_button = driver.find_element('xpath', '//label[@analytics-event="All matches"]')
all_matches_button.click()

box = driver.find_element("xpath", "//option[@label='Germany']")
box.click()

time.sleep(5)

Matches = driver.find_elements(By.TAG_NAME, "tr")

date = []
home_team = []
away_team = []
score = []

for match in Matches:
    date.append(match.find_element(By.XPATH, "./td[1]").text)
    home_team.append(match.find_element(By.XPATH, "./td[2]").text)
    away_team.append(match.find_element(By.XPATH, "./td[4]").text)
    score.append(match.find_element(By.XPATH, "./td[3]").text)


# print(date)

driver.quit()

df = pd.DataFrame({'date': date,'home_team': home_team,'away_team': away_team,'score': score})
print(df)
df.to_csv('tutorial.csv', index=False)