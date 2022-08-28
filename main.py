from selenium import webdriver
from selenium.webdriver.common.by import By

CHROMEDRIVER_PATH=r"C:\Users\intel\Documents\tinal_ticket project\chromedriver"
driver=webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
driver.get("https://indianexpress.com/article/india/adhir-ranjan-chowdhury-apology-president-droupadi-murmu-rashtrapatni-remark-8059550/")

title=driver.find_element(By.CLASS,"native_story_title")
print(title)