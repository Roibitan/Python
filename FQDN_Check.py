from tkinter import *
import time
import subprocess



def click_me():
    Domains = [".domain.1", ".domain.2", ".domain.3", ".domain.4", ".domain.5",
               ".domain.6", ".domain.7", ".domain.8",
               ".domain.9", ".domain.10", ".domain.11", ".domain.12",
               ".domain.13"]
    Machine_Name = e.get()
    for domain in Domains:
        name = Machine_Name + domain
        command = ['ping', '-n', '1', name]
        FNULL = open(os.devnull, 'w')
        response = subprocess.call(command, stdout=FNULL)
        # print(response)
        if response == 0:
            print('The FQDN is: ' + name)
            answer = Label(root, text=name)
            answer.pack()
            # return name
        else:
            pass




root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()
#e.insert(0, "Enter Machine Name:")



root.title('FQDN_Check')
root.geometry("400x150")

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

click = Button(main_frame, text="Go", command=click_me)
click.pack()

root.mainloop()
