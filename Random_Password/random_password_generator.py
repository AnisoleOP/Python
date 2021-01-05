import tkinter as tk
import pyperclip
import random
l = []
def string_to_int(k):
    if k == '1':
        return 1
    elif k == '2':
        return 2
    elif k == '3':
        return 3
    elif k == '4':
        return 4
    elif k == '5':
        return 5
    elif k == '6':
        return 6
    elif k == '7':
        return 7
    elif k == '8':
        return 8
    else:
        return 9
def set_password(n):
    for i in range(n):
        k = random.randint(1,9)
        l.append(k)
def list_to_string(l):
    s = ""
    for i in l:
        k = str(i)
        s += k
    return s
def copy(s):
    pyperclip.copy(s)
root = tk.Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("DataFlair - PASSWORD GENERATOR")
lab = tk.Label(root, text = "PASSWORD LENGTH:9", width = 25)
lab.pack()
e = tk.Entry(root, width = 0)
e.pack()
k = e.get()
n = string_to_int(k)
set_password(n)
s = list_to_string(l)
lbl = tk.Label(root, text = s, width = 25)
lbl.pack()
but = tk.Button(root, text = "COPY", width = 25)
but.pack()
copy(s)
root.mainloop() 