from selenium import webdriver
import time
import smtplib





PATH = "C:\Temp\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver.set_window_size(500, 500)
driver.get("http://tfs-prod:8080/tfs/CellcomCollection/CMTeam/_release?_a=releases&view=mine&definitionId=3")
driver.find_element_by_id("__bolt-create-release-command").click()



#
#
# for x in range(10):
#
#
#
#
#
#     driver.find_element_by_id('scheduleForm:tabViewId:ccnum').send_keys("XXXXXXXXXX")
#     driver.find_element_by_id('scheduleForm:tabViewId:dataNascimento_input').send_keys("XXXXXXXXXX")
#     #time.sleep(2)
#     driver.find_element_by_name("scheduleForm:tabViewId:searchIcon").click()
#     time.sleep(4)
#     driver.find_element_by_id("scheduleForm:postcons_label").click()
#     time.sleep(3)
#     driver.find_element_by_xpath("//li[contains(text(),'Secção Consular da Embaixada de Portugal em Telavi')]").click()
#     time.sleep(3)
#     driver.find_element_by_id("__bolt-create-release-command").click()
#     time.sleep(2)
#     driver.find_element_by_xpath("//li[contains(text(),'Documentos de identificação civil')]").click()
#     time.sleep(2)
#     driver.find_element_by_xpath("//span[contains(text(),'Adicionar Ato Consular')]").click()
#     time.sleep(2)
#     driver.find_element_by_xpath("//tbody/tr[1]/td[1]/div[1]/div[1]/div[2]/div[1]/div[2]").click()
#     time.sleep(2)
#     for x in range(10):
#         try:
#             driver.find_element_by_xpath("//tbody/tr[1]/td[1]/button[1]/span[1]").click()
#             time.sleep(2)
#             driver.find_element_by_xpath("//tbody/tr[2]/td[1]/button[1]/span[1]").click()
#             time.sleep(2)
#             # driver.find_element_by_xpath("//tbody/tr[1]/td[1]/button[1]/span[1]").click()
#             # time.sleep(2)
#             # driver.find_element_by_xpath("//tbody/tr[2]/td[1]/button[1]/span[1]").click()
#         except:
#             sender = 'XXXXXXX@XXXXX.com'
#             receivers = ['XXXXXX@XXXXX.co.il']
#             message = """New turn"""
#             smtpObj = smtplib.SMTP('XXXXXXXX')
#             smtpObj.sendmail(sender, receivers, message)
#             print("Successfully sent email")
#     driver.close()
#
