from tkinter import *
import subprocess
import os
import socket

def get_ip_from_fqdn(fqdn):
    try:
        return socket.gethostbyname(fqdn)
    except socket.gaierror:
        return "N/A"

def click_me():
    Domains = [".XXXXX.XXX.XX", ".XXXXX.XXX.XX", ".XXXXX.XXX.XX", ".XXXXX.XXX.XX", ".XXXXX.XXX.XX", ".XXXXX.XXX.XX",
               ".XXXXX.XXX.XX", ".XXXXX.XXX.XX", ".XXXXX.XXX.XX",
               ".XXXXX.XXX.XX", ".XXXXX.XXX.XX"]


    Machine_Name = e.get().strip()
    result_text.delete("1.0", END)  # Clear the Text widget before displaying new results
    for domain in Domains:
        name = Machine_Name + domain
        print(name)
        command = ['ping', '-n', '1', name]
        FNULL = open(os.devnull, 'w')
        response = subprocess.call(command, stdout=FNULL)



        # print(response)
        if response == 0:
            print('The FQDN is: ' + name)
            ip_address = get_ip_from_fqdn(name)
            print('The IP address is: ' + ip_address)
            result_text.insert(END, "The FQDN is: " + name + "\nIP Address: " + ip_address + "\n\n")
            # return name
    else:
        pass

root = Tk()
root.title('FQDN_Check')
root.geometry("400x200")

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

e = Entry(main_frame, width=50, borderwidth=5)
e.pack(pady=10)

click = Button(main_frame, text="Go", command=click_me)
click.pack(pady=5)

result_text = Text(main_frame, wrap=WORD, font=("Helvetica", 12))
result_text.pack(pady=10)

root.mainloop()
