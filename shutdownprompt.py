#!/usr/bin/env python
from tkinter import *
from os import system, popen
import re
from sys import exit, argv
logout_cmd = "killall dwm"
if len(argv) >= 2:
    if argv[1].startswith("logoutpid"):
        logout_cmd = "kill " + argv[1][9:]
window = Tk()
window.title("Logout")
output_stream = popen("xrandr")
lines = output_stream.read().split("\n")
pattern = re.compile(r"(\d+)x(\d+)\+(\d+)\+(\d+)")
W = 475
H = 125
X = 0
Y = 0
def logout():
    window.destroy()
    system(logout_cmd)
def restart():
    window.destroy()
    system("bash -c \"sudo reboot\"")
def shutdown():
    window.destroy()
    system("bash -c \"sudo poweroff\"")
for a in lines:
    if " connected primary" in a:
        w, h, x, y = pattern.search(a).groups()
        w = int(w); h = int(h); x = int(x); y = int(y);
        X = int(w/2 - W/2 + x)
        Y = int(h/2 - H/2 + y)
window.geometry(str(W)+"x"+str(H)+"+"+str(X)+"+"+str(Y))
window.resizable(False, False)
window.attributes('-topmost',True)
window.configure(bg="#0a0a0f")
logout_button   = Button(window, text="Log Out",  bg="#0a0a0f", fg="#ffcfff", command=logout)
logout_button   .place( x=25, y=25, width=125, height=75)
restart_button  = Button(window, text="Restart",  bg="#0a0a0f", fg="#ffcfff", command=restart)
restart_button  .place(x=175, y=25, width=125, height=75)
shutdown_button = Button(window, text="Shutdown", bg="#0a0a0f", fg="#ffcfff", command=shutdown)
shutdown_button .place(x=325, y=25, width=125, height=75)
def close(e):
    if e.widget == window:
        window.destroy()
window.bind('<Escape>', close)
#window.bind('<FocusOut>', close)
window.mainloop()
