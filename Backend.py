from tkinter import simpledialog
from selenium import webdriver
from tkinter import *
from time import sleep


master = Tk()


def get_me():
    user_from_input = simpledialog.askstring("input string", "please enter name")
    disable_user_in_all_backend(user_from_input)


def disable_user_in_all_backend(user_wanted):
    f = open("/Users/roib/Desktop/AutoPython/BackEnd.txt")
    list_of_lines = f.readlines()
    for url in list_of_lines:
        disable_user(user_wanted, url)


def disable_user(user_wanted, url):
    driver = webdriver.Chrome(executable_path='C:/Users/roib/Desktop/AutoPython/chromedriver.exe')
    driver.set_window_size(1920, 1080)
    try:
        driver.get('https://' + url + '/Operators/OperatorsManagement.aspx')
        driver.find_element_by_id('txtUsername').send_keys("roib")
        driver.find_element_by_id('txtPassword').send_keys("Rr123123!")
        driver.find_element_by_id('btnLogin').click()
        sleep(2)
        driver.find_element_by_id('rdbStatus_2').click()
        driver.find_element_by_id('btnShow').click()

        sleep(5)
    except:
        pass
    try:
        table = driver.find_element_by_id('gvOperators')
        rows = table.find_elements_by_tag_name('tr')
        for row in rows:
            info = row.find_elements_by_tag_name('td')
            if len(info) > 1:
                UserID = info[0].text
                Username = info[1].text
                if Username.lower() == user_wanted.lower():
                    print(Username.lower(), user_wanted.lower())
                    driver.get(("https://" + url + "/Operators/OperatorsPermissions.aspx?OperatorID=" + UserID + "&637128769732565579"))
                    select=driver.find_element_by_id('chkEnabled').is_selected()
                    if(select):
                        done_backend = print(url, "Done.")
                        driver.find_element_by_id('chkEnabled').click()
                        driver.find_element_by_id('btnSave').click()
                        sleep(2)
                        driver.switch_to.alert.accept()
                        sleep(2)
                        driver.switch_to.alert.accept()
                        sleep(5)
                        print(done_backend)
    except Exception as e:
        print(e)
    driver.close()

button = Button(master, text="Insert Name", command=get_me)
button.pack()
master.title("Disable users")
master.geometry('300x200')
mainloop()
