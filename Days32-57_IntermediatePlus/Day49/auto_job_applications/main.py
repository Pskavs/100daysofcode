#Importing packages and setting up selenium.
import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#Sets email and password
load_dotenv()
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4131555202&distance=25.0&f_E=1%2C2&f_TPR=r604800&f_WT=2&geoId=103644278&keywords=data%20intern&origin=JOB_SEARCH_PAGE_JOB_FILTER")
sleep(2)

# Clicks sign in link.

def sign_in():
    """Uses Selenium to login to LinkedIn and go to my job postings"""
    driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button').click()
    sleep(1)
    #Signs in with Username and Password
    driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_key"]').send_keys(EMAIL)
    driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_password"]').send_keys(PASSWORD)
    driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button').click()
    sleep(1)

def create_job_list():
    """Looks at the side bar to create a list of jobs, it then calls a function to call each job."""
    jobs_list = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/ul')
    jobs = jobs_list.find_elements(By.CSS_SELECTOR, 'li')
    click_jobs(jobs)
def click_jobs(jobs):
    """Goes through the list of jobs, making sure the page scrolls to each element before trying to click it."""
    for job in jobs:
        try:
            driver.execute_script("arguments[0].scrollIntoView();", job)
            job.click()
            sleep(0.5)
            save_job(jobs)
        except NoSuchElementException:
            pass
def save_job(jobs):
    """Saves the jobs in my list, so I can apply for them later."""
    save_button = driver.find_element(By.XPATH,'//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/button')
    if 'saved' in save_button.text.lower():
        print('Already saved')
    else:
        print('Saving')
        save_button.click()
    return jobs
sign_in()
create_job_list()
