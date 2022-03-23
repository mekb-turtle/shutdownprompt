#!/usr/bin/env python
from tkinter import *
from os import system, popen
import re
from sys import exit
window = Tk()
window.title("Logout")
output_stream = popen("xrandr")
lines = output_stream.read().split("\n")
pattern = re.compile(r"(\d+)x(\d+)\+(\d+)\+(\d+)")
W = 700
H = 150
X = 0
Y = 0
def logout():
    system("killall dwm")
def restart():
    system("reboot")
def shutdown():
    system("poweroff")
for a in lines:
    if " connected primary" in a:
        w, h, x, y = pattern.search(a).groups()
        w = int(w); h = int(h); x = int(x); y = int(y);
        X = int(w/2 - W/2 + x)
        Y = int(h/2 - H/2 + y)
screen_width  = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(str(W)+"x"+str(H)+"+"+str(X)+"+"+str(Y))
window.resizable(False, False)
window.attributes('-topmost',True)
window.configure(bg="#121216")
logout_button   = Button(window, width=16, height=4, text="Log Out",  bg="#121216", fg="#ffeeff", command=logout)
logout_button   . grid(column=0, row=0, padx=50, pady=50)
restart_button  = Button(window, width=16, height=4, text="Restart",  bg="#121216", fg="#ffeeff", command=restart)
restart_button  . grid(column=1, row=0, padx=50, pady=50)
shutdown_button = Button(window, width=16, height=4, text="Shutdown", bg="#121216", fg="#ffeeff", command=shutdown)
shutdown_button . grid(column=2, row=0, padx=50, pady=50)
col_count, row_count = window.grid_size()
for i in range(col_count):
    window.grid_columnconfigure(i, weight=1, minsize=50)
for i in range(row_count):
    window.grid_rowconfigure(i, weight=1)
def close(e):
    if e.widget == window:
        window.destroy()
window.bind('<Escape>', close)
window.bind('<FocusOut>', close)
window.mainloop()
