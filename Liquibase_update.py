from selenium import webdriver
import time
import smtplib





PATH = "C:\Temp\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver.set_window_size(500, 500)
driver.get("http://tfs-prod:8080/tfs/CellcomCollection/CMTeam/_release?_a=releases&view=mine&definitionId=3")
driver.find_element_by_id("__bolt-create-release-command").click()
driver.find_element_by_xpath("//body/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/button[1]").click()

#//body/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/button[1]