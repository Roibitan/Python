import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from time import sleep
import socket  # Socket module to check if the system's pors is open or not?
import time, datetime
from datetime import date
import os
import subprocess




my_dict = {
    "eaiws1": {"VAL": "", 'Address': "XXXXXXX.corp.co.il", "port": 80},
    "eaiws2": {"VAL": "", 'Address': "XXXXXXX.corp.co.il", "port": 80},
    "mqsapams": {"VAL": "", 'Address': "XXXXXXX.corp.co.il", "port": 3200},
    "BT10PRDAPP1": {"VAL": "", 'Address': "XXXXXXX.corp.co.il", "port": 4500},
    "sap6dev": {"VAL": "", 'Address': "XXXXXXX.dev.corp.co.il", "port": 3242},
    "saptstci": {"VAL": "", 'Address': "XXXXXXX.dev.corp.co.il", "port": 3200},
    "OSBQA1": {"VAL": "", 'Address': "XXXXXXX.corp.co.il", "port": 7005},
    "OSBINT1": {"VAL": "", 'Address': "XXXXXXX.corp.co.il", "port": 7005},
    "bwprd03": {"VAL": "", 'Address': "XXXXXXX.corp.co.il", "port": 50000},
}


def MyUrl():
    for key, value in my_dict.items():
        if value["VAL"] == 1:
            #print(key)
            BURL = my_dict[key]["Address"]
            pport = my_dict[key]["port"]
            a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            location = (BURL, pport)
            result_of_check = a_socket.connect_ex(location)
            if result_of_check == 0:
                answer_open = (key, "Port is open")
                myLablel = Label(root, text=answer_open)
                myLablel.pack()
                #print(key, "Port is open")
            else:
                answer_close = (key, "Port is not open")
                myLablel = Label(root, text=answer_close)
                myLablel.pack()
                #print(key, "Port is not open")
        else:
            continue

def on_configure(event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
    canvas.configure(scrollregion=canvas.bbox('all'))


# def Create_User(val):
#

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

    my_dict["eaiws1"]["VAL"] = dict1
    my_dict["eaiws2"]["VAL"] = dict2
    my_dict["mqsapams"]["VAL"] = dict3
    my_dict["BT10PRDAPP1"]["VAL"] = dict4
    my_dict["sap6dev"]["VAL"] = dict5
    my_dict["saptstci"]["VAL"] = dict6
    my_dict["OSBQA1"]["VAL"] = dict7
    my_dict["OSBINT1"]["VAL"] = dict8
    my_dict["bwprd03"]["VAL"] = dict9
    MyUrl()


root = Tk()
root.title('Cellcom Hcheack')
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


a = Checkbutton(second_frame, text="eaiws1", variable=var1)
a.pack()

b = Checkbutton(second_frame, text="eaiws2", variable=var2)
b.pack()

c = Checkbutton(second_frame, text="mqsapams", variable=var3)
c.pack()

d = Checkbutton(second_frame, text="BT10PRDAPP1", variable=var4)
d.pack()

a = Checkbutton(second_frame, text="sap6dev", variable=var5)
a.pack()

a = Checkbutton(second_frame, text="saptstci", variable=var6)
a.pack()

a = Checkbutton(second_frame, text="OSBQA1", variable=var7)
a.pack()

a = Checkbutton(second_frame, text="OSBINT1", variable=var8)
a.pack()

a = Checkbutton(second_frame, text="bwprd03", variable=var9)
a.pack()



click = Button(main_frame, text="Click here", command=click_me)
click.pack()

root.mainloop()