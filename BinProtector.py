from tkinter import *
from tkinter import messagebox
import os
import pathlib
from os import path
# creating basic window
window = Tk()
window.geometry("312x198+0+0")  # size of the window width:- 500, height:- 375
window.resizable(0, 0)  # this prevents from resizing the window
window.title(" Bin Protector ")
window.config(bg="#1F1F1F")

# ----------------METHODS-------------------

pathStr = StringVar()


def OnFileSecurity():
    pth = pathFile.get()
    if len(pth) == 0:
        messagebox.showwarning("Bin Protector", "Please Enter Path \U0001F6A7")
    else:
        chkPth = pathlib.Path(pth)
        if chkPth.exists():
            pathStr = "cmd /c ECHO Y| cacls " + pth + " /p everyone:n"
            print(pathStr)
            os.system(pathStr)
            messagebox.showinfo(
                "Bin Protector", "Successfully Protected \U0001F60A")
        else:
            messagebox.showerror("Bin Protector", "Path is Invalid \U0001F614")


def OffFileSecurity():
    pth = pathFile.get()
    if len(pth) == 0:
        messagebox.showwarning("Bin Protector", "Please Enter Path \U0001F6A7")
    else:
        chkPth = pathlib.Path(pth)
        if chkPth.exists():
            pathStr = "cmd /c ECHO Y| cacls " + pth + " /p everyone:f"
            print(pathStr)
            os.system(pathStr)
            messagebox.showinfo(
                "Bin Protector", "Successfully Protected \U0001F60A")
        else:
            messagebox.showerror("Bin Protector", "Path is Invalid \U0001F614")


# ----------------TITLE-------------------
Label(window, text="Secure Your Files", fg="white", bg="#1F1F1F",
      font=("Elephant bold", 20)).place(x=40, y=20)
# ----------------PATH LABEL AND ENTRY-------------------
Label(window, text="Folder Path:", fg="white", bg="#1F1F1F",
      font=("Arial bold", 12), pady=10, anchor="e", width=11).place(x=20, y=65)
pathFile = Entry(window, bg="#1F1F1F", fg="white", bd=2,
                 relief="groove", insertbackground="white")
pathFile.place(x=140, y=76, height=25, width=150)

# -------- On Security --------------
onSecurityBtn = Button(window, text=" ON ", fg="white", bg="black", highlightthickness=2,
                       cursor="hand2", font=("Cooper bold", 12), activebackground="grey", activeforeground="white", justify=CENTER, command=OnFileSecurity)
onSecurityBtn.place(x=70, y=120, width=86, height=30)
# --------Off Security --------------
offSecurityBtn = Button(window, text=" OFF ", fg="white", bg="black", highlightthickness=2,
                        cursor="hand2", font=("Cooper bold", 12), activebackground="grey", activeforeground="white", justify=CENTER, command=OffFileSecurity)
offSecurityBtn.place(x=170, y=120, width=86, height=30)

#----------- Footer --------- #
Label(window, text="ᶑ Developed: by Syed Nokhaiz Al Hassan ", fg="white", bg="#1F1F1F",
      font=("Times New Roman italic", 12)).pack(side="bottom")
window.mainloop()
