import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

my_dict = {
    "MT-UAT": {"VAL": "", 'URL': "https://backend.XXXXXX.XXXXXX.com"}, "MT-PROD": {"VAL": "", 'URL': "https://backend.pre-uat.XXXXXX-mt.com"},
    "MI-UAT": {"VAL": "", 'URL': "https://backend.XXXXXX.XXXXXX.com"}, "MI-PROD": {"VAL": "", 'URL': "https://backend.XXXXXX.com"},
    "VAL-UAT": {"VAL": "", 'URL': "https://backend.XXXXXX.XXXXXX.com"}, "VAL-PROD": {"VAL": "", 'URL': "https://backend.uat.XXXXXX.com"},
    "Sazka-UAT": {"VAL": "", 'URL': "https://backend.XXXXXX.XXXXXX.cz"}, "Sazka-PROD": {"VAL": "", 'URL': "https://backend.XXXXXX.cz"},
    "NHL-UAT": {"VAL": "", 'URL': "http://backend.XXXXXX.XXXXXX.com"}, "NHL-PROD": {"VAL": "", 'URL': "https://backend.XXXXXX.com"},
    "NCEL-UAT": {"VAL": "", 'URL': "https://backend.XXXXXX.XXXXXX.XXXXXX.com"}, "NCEL-PROD": {"VAL": "", 'URL': "https://backend.npi.XXXXXX.com"},
    "AGLC-UAT": {"VAL": "", 'URL': "https://backend.XXXXXX.XXXXXX.ca"}, "AGLC-PROD": {"VAL": "", 'URL': "https://backend.XXXXXX.ca"},
    "NG-LOT-UAT": {"VAL": "", 'URL': "https://backend.XXXXXX.XXXXXX-ir.com"}, "NG-LOT-PROD": {"VAL": "", 'URL': "https://XXXXXX.XXXXXX-ir.com"},
    "Croatia-UAT": {"VAL": "", 'URL': "https://backend-XXXXXX.XXXXXX.hr"}, "Croatia-PROD": {"VAL": "", 'URL': "ttps://XXXXXX.XXXXXX.hr"},
    "WH-NJ-GPT": {"VAL": "", 'URL': "https://backend.XXXXXX.nj.us.gpt.XXXXXX-test.com"}, "WH-NJ-Cert": {"VAL": "", 'URL': "https://backend.XXXXXX.nj.XXXXXX.usc.XXXXXX-test.com"}, "WH-NJ-PROD": {"VAL": "", 'URL': "https://backend.nj.XXXXXX.XXXXXX.com"},
    "WH-IN-GPT": {"VAL": "", 'URL': "https://backend.XXXXXX.in.us.gpt.XXXXXX-test.com"}, "WH-IN-Cert": {"VAL": "", 'URL': "https://backend.in.XXXXXX.usc.XXXXXX-test.com"}, "WH-IN-PROD": {"VAL": "", 'URL': "https://backend.in.XXXXXX.XXXXXX.com"},
    "WH-IA-GPT": {"VAL": "", 'URL': "https://backend.XXXXXX.ia.us.gpt.XXXXXX-test.com"}, "WH-IA-Cert": {"VAL": "", 'URL': "https://backend.XXXXXX.XXXXXX.us.usc.XXXXXX-test.com"}, "WH-IA-PROD": {"VAL": "", 'URL': "https://backend.XXXXXX.ia.XXXXXX.XXXXXX.com"},
    "WH-IL-GPT": {"VAL": "", 'URL': "https://backend.XXXXXX.il.us.gpt.XXXXXX-test.com"}, "WH-IL-Cert": {"VAL": "", 'URL': "https://backend.XXXXXX.il.us.usc.XXXXXX-test.com"}, "WH-IL-PROD": {"VAL": "", 'URL': "hypps://"},
    "WH-WV-GPT": {"VAL": "", 'URL': "https://backend.wv.us.gpt.XXXXXX-test.com"}, "WH-WV-Cert": {"VAL": "", 'URL': "https://backend.wv.XXXXXX.usc.XXXXXX-test.com"}, "WH-WV-PROD": {"VAL": "", 'URL': "https://backend.wv.us.williamhill.com"},
    "WH-CO-GPT": {"VAL": "", 'URL': "https://backend.XXXXXX.co.us.XXXXXX.XXXXXX-test.com"}, "WH-CO-Cert": {"VAL": "", 'URL': "https://backend.XXXXXX.co.XXXXXX.usc.XXXXXX-test.com"}, "WH-CO-PROD": {"VAL": "", 'URL': "https://backend.XXXXXX.co.us.XXXXXX.com"},
    "WH-MI-GPT": {"VAL": "", 'URL': "https://backend.XXXXXX.mi.us.XXXXXX.XXXXXX-test.com"}, "WH-MI-Cert": {"VAL": "", 'URL': "https://backend.XXXXXX.mi.XXXXXX.usc.XXXXXX-test.com"}, "WH-MI-PROD": {"VAL": "", 'URL': "https://backend.XXXXXX.mi.us.XXXXXX.com"},
    "WH-TN-GPT": {"VAL": "", 'URL': "https://backend.XXXXXX.tn.us.XXXXXX.XXXXXX-test.com"}, "WH-TN-Cert": {"VAL": "", 'URL': "https://backend.XXXXXX.tn.XXXXXX.usc.XXXXXX-test.com"}, "WH-TN-PROD": {"VAL": "", 'URL': "https://backend.XXXXXX.tn.us.XXXXXX.com"},
    "WH-VA-GPT": {"VAL": "", 'URL': "https://backend.XXXXXX.va.us.XXXXXX.XXXXXX-test.com"}, "WH-VA-Cert": {"VAL": "", 'URL': "https://backend.XXXXXX.va.XXXXXX.usc.XXXXXX-test.com"}, "WH-VA-PROD": {"VAL": "", 'URL': "https://backend.XXXXXX.va.us.XXXXXX.com"},
    "WH-AZ-GPT": {"VAL": "", 'URL': "https://backend.XXXXXX.az.us.XXXXXX.XXXXXX-test.com"}, "WH-AZ-Cert": {"VAL": "", 'URL': "https://backend.XXXXXX.az.XXXXXX.usc.XXXXXX-test.com"}, "WH-AZ-PROD": {"VAL": "", 'URL': "https://backend.XXXXXX.az.us.XXXXXX.com"},
    "WH-LA-GPT": {"VAL": "", 'URL': "https://backend.XXXXXX.la.us.XXXXXX.XXXXXX-test.com"}, "WH-LA-Cert": {"VAL": "", 'URL': "https://backend.XXXXXX.la.XXXXXX.usc.XXXXXX-test.com"}, "WH-LA-PROD": {"VAL": "", 'URL': "https://backend.XXXXXX.la.us.XXXXXX.com"}
}

def main():
    click_me()
def get_me(url):
    user_from_input = ename.get()
    username_from_input = eusername.get()
    email_from_input = eemail.get()
    permissions_from_input = epermission.get()
    Create_User(user_from_input, username_from_input, email_from_input, permissions_from_input, url)

def MyUrl():
    for key, value in my_dict.items():
        if value["VAL"] == 1:
            print(key)
            BURL = my_dict[key]["URL"]
            get_me(BURL)
        else:
            print("key doesn't exist")
#def checkuser(paremissions, url):


def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))


def Create_User(user_wanted, username_wanted, email_wanted, permissions_wanted, url):
    driver = webdriver.Chrome(executable_path='C:/Users/shakedg/Documents/Backends/chromedriver.exe')
    driver.set_window_size(1920, 1080)
    try:
        driver.get(url + '/Operators/OperatorsPermissions.aspx')
        driver.find_element_by_id('txtUsername').send_keys("UserName")
        driver.find_element_by_id('txtPassword').send_keys("@UserPass")
        driver.find_element_by_id('btnLogin').click()
        sleep(2)
        driver.find_element_by_id('txtFullName').send_keys(user_wanted)
        driver.find_element_by_id('txtUserName').send_keys(username_wanted)
        driver.find_element_by_id('txtEmail').send_keys(email_wanted)
        driver.find_element_by_id('btnSave').click()
        sleep(2)
        driver.switch_to.alert.accept()
        sleep(5)
        print("opened user")
    except:
        pass
    try:
        sleep(3)
        select1 = Select(driver.find_element_by_id('ucMatchOperatorsList_lstOperators'))
        select1.select_by_visible_text(permissions_wanted)
        driver.find_element_by_id('btnMatch').click()
        sleep(2)
        driver.switch_to.alert.accept()
        print("done")
    except:
        print("fail")

    driver.close()
# # function to return key for any value
# def get_key(val):
#     for key, value in my_dict.items():
#         if val == 1:
#             return key
#
#     return "key doesn't exist"

# function to use tkinter
def click_me():
    dict1 = var1.get()
    dict2 = var2.get()
    dict3 = var3.get()
    dict4 = var4.get()
    dict5 = var5.get()
    dict6 = var6.get()
    dict7 = var7.get()
    dict8 = var8.get()
    dict9 = var9.get()
    dict10 = var10.get()
    dict11 = var11.get()
    dict12 = var12.get()
    dict13 = var13.get()
    dict14 = var14.get()
    dict15 = var15.get()
    dict16 = var16.get()
    dict17 = var17.get()
    dict18 = var18.get()
    dict19 = var19.get()
    dict20 = var20.get()
    dict21 = var21.get()
    dict22 = var22.get()
    dict23 = var23.get()
    dict24 = var24.get()
    dict25 = var25.get()
    dict26 = var26.get()
    dict27 = var27.get()
    dict28 = var28.get()
    dict29 = var29.get()
    dict30 = var30.get()
    dict31 = var31.get()
    dict32 = var32.get()
    dict33 = var33.get()
    dict34 = var34.get()
    dict35 = var35.get()
    dict36 = var36.get()
    dict37 = var37.get()
    dict38 = var38.get()
    dict39 = var39.get()
    dict40 = var40.get()
    dict41 = var41.get()
    dict42 = var42.get()
    dict43 = var43.get()
    dict44 = var44.get()
    dict45 = var45.get()
    dict46 = var46.get()
    dict47 = var47.get()
    dict48 = var48.get()
    dict49 = var49.get()
    dict50 = var50.get()
    dict51 = var51.get()

    my_dict["MT-UAT"]["VAL"] = dict1
    my_dict["MT-PROD"]["VAL"] = dict2
    my_dict["MI-UAT"]["VAL"] = dict3
    my_dict["MI-PROD"]["VAL"] = dict4
    my_dict["VAL-UAT"]["VAL"] = dict5
    my_dict["VAL-PROD"]["VAL"] = dict6
    my_dict["Sazka-UAT"]["VAL"] = dict7
    my_dict["Sazka-PROD"]["VAL"] = dict8
    my_dict["NHL-UAT"]["VAL"] = dict9
    my_dict["NHL-PROD"]["VAL"] = dict10
    my_dict["NCEL-UAT"]["VAL"] = dict11
    my_dict["NCEL-PROD"]["VAL"] = dict12
    my_dict["AGLC-UAT"]["VAL"] = dict13
    my_dict["AGLC-PROD"]["VAL"] = dict14
    my_dict["NG-LOT-UAT"]["VAL"] = dict15
    my_dict["NG-LOT-PROD"]["VAL"] = dict16
    my_dict["Croatia-UAT"]["VAL"] = dict17
    my_dict["Croatia-PROD"]["VAL"] = dict18
    my_dict["WH-NJ-GPT"]["VAL"] = dict19
    my_dict["WH-NJ-Cert"]["VAL"] = dict20
    my_dict["WH-NJ-PROD"]["VAL"] = dict21
    my_dict["WH-IN-GPT"]["VAL"] = dict22
    my_dict["WH-IN-Cert"]["VAL"] = dict23
    my_dict["WH-IN-PROD"]["VAL"] = dict24
    my_dict["WH-IA-GPT"]["VAL"] = dict25
    my_dict["WH-IA-Cert"]["VAL"] = dict26
    my_dict["WH-IA-PROD"]["VAL"] = dict27
    my_dict["WH-IL-GPT"]["VAL"] = dict28
    my_dict["WH-IL-Cert"]["VAL"] = dict29
    my_dict["WH-IL-PROD"]["VAL"] = dict30
    my_dict["WH-WV-GPT"]["VAL"] = dict31
    my_dict["WH-WV-Cert"]["VAL"] = dict32
    my_dict["WH-WV-PROD"]["VAL"] = dict33
    my_dict["WH-CO-GPT"]["VAL"] = dict34
    my_dict["WH-CO-Cert"]["VAL"] = dict35
    my_dict["WH-CO-PROD"]["VAL"] = dict36
    my_dict["WH-MI-GPT"]["VAL"] = dict37
    my_dict["WH-MI-Cert"]["VAL"] = dict38
    my_dict["WH-MI-PROD"]["VAL"] = dict39
    my_dict["WH-TN-GPT"]["VAL"] = dict40
    my_dict["WH-TN-Cert"]["VAL"] = dict41
    my_dict["WH-TN-PROD"]["VAL"] = dict42
    my_dict["WH-VA-GPT"]["VAL"] = dict43
    my_dict["WH-VA-Cert"]["VAL"] = dict44
    my_dict["WH-VA-PROD"]["VAL"] = dict45
    my_dict["WH-AZ-GPT"]["VAL"] = dict46
    my_dict["WH-AZ-Cert"]["VAL"] = dict47
    my_dict["WH-AZ-PROD"]["VAL"] = dict48
    my_dict["WH-LA-GPT"]["VAL"] = dict49
    my_dict["WH-LA-Cert"]["VAL"] = dict50
    my_dict["WH-LA-PROD"]["VAL"] = dict51
    MyUrl()

root = Tk()
root.title('Neogames Backends')
root.geometry("500x600")

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda ez: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

second_frame = Frame(my_canvas)

my_canvas.create_window((0,0), window=second_frame, anchor="nw")
t1= Label(main_frame, text="Enter Name:")
t1.pack()
ename = Entry(main_frame)
ename.pack()
t2= Label(main_frame, text="Enter Username:")
t2.pack()
eusername = Entry(main_frame)
eusername.pack()
t3= Label(main_frame, text="Enter Email:")
t3.pack()
eemail = Entry(main_frame)
eemail.pack()
t4= Label(main_frame, text="Copy from:")
t4.pack()
epermission = Entry(main_frame)
epermission.pack()




var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()
var29 = IntVar()
var30 = IntVar()
var31 = IntVar()
var32 = IntVar()
var33 = IntVar()
var34 = IntVar()
var35 = IntVar()
var36 = IntVar()
var37 = IntVar()
var38 = IntVar()
var39 = IntVar()
var40 = IntVar()
var41 = IntVar()
var42 = IntVar()
var43 = IntVar()
var44 = IntVar()
var45 = IntVar()
var46 = IntVar()
var47 = IntVar()
var48 = IntVar()
var49 = IntVar()
var50 = IntVar()
var51 = IntVar()


a = Checkbutton(second_frame, text="MT-UAT", variable=var1)
a.pack()

b = Checkbutton(second_frame, text="MT-PROD", variable=var2)
b.pack()

c = Checkbutton(second_frame, text="MI-UAT", variable=var3)
c.pack()

d = Checkbutton(second_frame, text="MI-PROD", variable=var4)
d.pack()

e = Checkbutton(second_frame, text="VAL-UAT", variable=var5)
e.pack()

f = Checkbutton(second_frame, text="VAL-PROD", variable=var6)
f.pack()

g = Checkbutton(second_frame, text="Sazka-UAT", variable=var7)
g.pack()

h = Checkbutton(second_frame, text="Sazka-PROD", variable=var8)
h.pack()

i = Checkbutton(second_frame, text="NHL-UAT", variable=var9)
i.pack()

j = Checkbutton(second_frame, text="NHL-PROD", variable=var10)
j.pack()

k = Checkbutton(second_frame, text="NCEL-UAT", variable=var11)
k.pack()

l = Checkbutton(second_frame, text="NCEL-PROD", variable=var12)
l.pack()

m = Checkbutton(second_frame, text="AGLC-UAT", variable=var13)
m.pack()

n = Checkbutton(second_frame, text="AGLC-PROD", variable=var14)
n.pack()

o = Checkbutton(second_frame, text="NG-LOT-UAT", variable=var15)
o.pack()

p = Checkbutton(second_frame, text="NG-LOT-PROD", variable=var16)
p.pack()

q = Checkbutton(second_frame, text="Croatia-UAT", variable=var17)
q.pack()

r = Checkbutton(second_frame, text="Croatia-PROD", variable=var18)
r.pack()

s = Checkbutton(second_frame, text="WH-NJ-GPT", variable=var19)
s.pack()

t = Checkbutton(second_frame, text="WH-NJ-Cert", variable=var20)
t.pack()

u = Checkbutton(second_frame, text="WH-NJ-PROD", variable=var21)
u.pack()

v = Checkbutton(second_frame, text="WH-IN-GPT", variable=var22)
v.pack()

w = Checkbutton(second_frame, text="WH-IN-Cert", variable=var23)
w.pack()

x = Checkbutton(second_frame, text="WH-IN-PROD", variable=var24)
x.pack()

y = Checkbutton(second_frame, text="WH-IA-GPT", variable=var25)
y.pack()

z = Checkbutton(second_frame, text="WH-IA-Cert", variable=var26)
z.pack()

aa = Checkbutton(second_frame, text="WH-IA-PROD", variable=var27)
aa.pack()

ab = Checkbutton(second_frame, text="WH-IL-GPT", variable=var28)
ab.pack()

ac = Checkbutton(second_frame, text="WH-IL-Cert", variable=var29)
ac.pack()

ad = Checkbutton(second_frame, text="WH-IL-PROD", variable=var30)
ad.pack()

af = Checkbutton(second_frame, text="WH-WV-GPT", variable=var31)
af.pack()

ag = Checkbutton(second_frame, text="WH-WV-Cert", variable=var32)
ag.pack()

ai = Checkbutton(second_frame, text="WH-WV-PROD", variable=var33)
ai.pack()

aj = Checkbutton(second_frame, text="WH-CO-GPT", variable=var34)
aj.pack()

ak = Checkbutton(second_frame, text="WH-CO-Cert", variable=var35)
ak.pack()

al = Checkbutton(second_frame, text="WH-CO-PROD", variable=var36)
al.pack()

am = Checkbutton(second_frame, text="WH-MI-GPT", variable=var37)
am.pack()

an = Checkbutton(second_frame, text="WH-MI-Cert", variable=var38)
an.pack()

ao = Checkbutton(second_frame, text="WH-MI-PROD", variable=var39)
ao.pack()

ap = Checkbutton(second_frame, text="WH-TN-GPT", variable=var40)
ap.pack()

aq = Checkbutton(second_frame, text="WH-TN-Cert", variable=var41)
aq.pack()

ar = Checkbutton(second_frame, text="WH-TN-PROD", variable=var42)
ar.pack()

at = Checkbutton(second_frame, text="WH-VA-GPT", variable=var43)
at.pack()

au = Checkbutton(second_frame, text="WH-VA-Cert", variable=var44)
au.pack()

av = Checkbutton(second_frame, text="WH-VA-PROD", variable=var45)
av.pack()

aw = Checkbutton(second_frame, text="WH-AZ-GPT", variable=var46)
aw.pack()

ax = Checkbutton(second_frame, text="WH-AZ-Cert", variable=var47)
ax.pack()

ay = Checkbutton(second_frame, text="WH-AZ-PROD", variable=var48)
ay.pack()

az = Checkbutton(second_frame, text="WH-LA-GPT", variable=var49)
az.pack()

ba = Checkbutton(second_frame, text="WH-LA-Cert", variable=var50)
ba.pack()

bb = Checkbutton(second_frame, text="WH-LA-PROD", variable=var51)
bb.pack()

click = Button(main_frame, text="Click here", command=click_me)
click.pack()
root.mainloop()

