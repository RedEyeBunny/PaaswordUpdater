import mysql.connector as sqltor
import tkinter as tk
from tkinter import messagebox
db = sqltor.connect(
    host='localhost',
    user='frost-ASUS-Gaming',
    password='H@rsh#2003',
    database='sec'
)
cursor = db.cursor()
root = tk.Tk()
root.title("AutoPass")
root.geometry("200x200")
root.minsize(200, 200)
root.maxsize(200, 200)
def AddWindow():
    addWindow = tk.Toplevel(root)
    addWindow.title("Add Details")
    addWindow.geometry('400x250')
    addWindow.minsize(400, 250)
    addWindow.maxsize(400, 250)
    tk.Label(addWindow, text="Website Name").place(x=20, y=20)
    website_name = tk.Entry(addWindow)
    website_name.place(x=150, y=20)
    tk.Label(addWindow, text="Website URL").place(x=20, y=50)
    website_url = tk.Entry(addWindow)
    website_url.place(x=150, y=50)
    tk.Label(addWindow, text="Login/Mail-Id").place(x=20, y=80)
    login = tk.Entry(addWindow)
    login.place(x=150, y=80)
    tk.Label(addWindow, text="Password").place(x=20, y=110)
    password = tk.Entry(addWindow)
    password.place(x=150, y=110)
    tk.Label(addWindow, text="Pin").place(x=20, y=140)
    pin = tk.Entry(addWindow)
    pin.place(x=150, y=140)
    tk.Label(addWindow, text="Email").place(x=20, y=170)
    email = tk.Entry(addWindow)
    email.place(x=150, y=170)
    def addPassword():
        value1 = website_name.get()
        value2 = website_url.get()
        value3 = login.get()
        value4 = password.get()
        value5 = pin.get()
        value6 = email.get()
        if value1 == "" or value2 == "" or value3 == "" or value4 == "" or value5 == "" or value6 == "":
            messagebox.showwarning("!Warning!", "Fill All fields")
        else:
            query = f"INSERT INTO info VALUES ('{value1}', '{value2}', '{value3}', '{value4}', '{value5}', '{value6}')"
            cursor.execute(query)
            db.commit()
            messagebox.showinfo("Success", "Values updated")
    tk.Button(addWindow, text="Add", command=addPassword).place(x=200, y=210)
def LookUpWindow():
    LookupWindow = tk.Toplevel(root)
    LookupWindow.title("LookUp Details")
    LookupWindow.geometry('200x200')
    LookupWindow.minsize(200, 200)
    LookupWindow.maxsize(200, 200)
    tk.Label(LookupWindow, text="Website Name").pack(pady=10)
    website_name = tk.Entry(LookupWindow)
    website_name.pack(pady=10)
    def LookUpResultWindow():
        site = website_name.get()
        if site == "":
            messagebox.showwarning("Error", "Enter a value")
        else:
            cursor.execute(f"select * from info where Information = '{site}'")
            res = cursor.fetchall()
            v1 = res[0][0]
            v2 = res[0][1]
            v3 = res[0][2]
            v4 = res[0][3]
            v5 = res[0][4]
            v6 = res[0][5]
            ResultWindow = tk.Toplevel(root)
            ResultWindow.title("LookUp Details")
            ResultWindow.geometry('400x250')
            ResultWindow.minsize(400, 250)
            ResultWindow.maxsize(400, 250)
            tk.Label(ResultWindow, text="Website Name").place(x=20, y=20)
            wn = tk.Text(ResultWindow, height=1, width=20)
            wn.place(x=150, y=20)
            wn.insert(tk.END, v1)
            tk.Label(ResultWindow, text="Website URL").place(x=20, y=50)
            wurl = tk.Text(ResultWindow, height=1, width=20)
            wurl.place(x=150, y=50)
            wurl.insert(tk.END, v2)
            tk.Label(ResultWindow, text="Login/Mail-Id").place(x=20, y=80)
            lmid = tk.Text(ResultWindow, height=1, width=20)
            lmid.place(x=150, y=80)
            lmid.insert(tk.END, v3)
            tk.Label(ResultWindow, text="Password").place(x=20, y=110)
            pw = tk.Text(ResultWindow, height=1, width=20)
            pw.place(x=150, y=110)
            pw.insert(tk.END, v4)
            tk.Label(ResultWindow, text="Pin").place(x=20, y=140)
            pi = tk.Text(ResultWindow, height=1, width=20)
            pi.place(x=150, y=140)
            pi.insert(tk.END, v5)
            tk.Label(ResultWindow, text="Email").place(x=20, y=170)
            em = tk.Text(ResultWindow, height=1, width=20)
            em.place(x=150, y=170)
            em.insert(tk.END, v6)
    tk.Button(LookupWindow, text="See Details", command=LookUpResultWindow).pack(pady=10)
tk.Button(root, text="Add Details", command=AddWindow).pack(pady=30)
tk.Button(root, text="LookUp Details", command=LookUpWindow).pack(pady=20)
root.mainloop()