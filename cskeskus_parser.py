import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random


def start_driver():
    main_page = 'https://www.cvkeskus.ee/toopakkumised'
    chrome_driver_path = './chromedriver_mac64/chromedriver'
    service = Service(executable_path=chrome_driver_path)

    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(main_page)
    return driver


def removing_duplicates_list(x):
    return list(dict.fromkeys(x))


def collect_links(driver):
    elements = driver.find_elements(By.CLASS_NAME, 'f_job_title')
    links = []
    for i in elements:
        links.append(i.get_attribute('href'))
    links = removing_duplicates_list(links)
    return links


def collect_job_description(links):
    description = []
    for page in links:
        driver.get(page)
        elements = driver.find_element(By.CLASS_NAME, 'job-offer')
        description.append({'job_description': elements.text})
        time.sleep(random.randint(0, 5))

    driver.quit()

    job_description = pd.DataFrame(description)
    return job_description


driver = start_driver()
links = collect_links(driver)
job_description = collect_job_description(links)