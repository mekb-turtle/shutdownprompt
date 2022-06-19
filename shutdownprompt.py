#!/usr/bin/env python
from tkinter import *
from os import system, popen
import re
from sys import exit, argv
logout_cmd = ""
if len(argv) >= 2:
    if argv[1].startswith("logoutpid"):
        logout_cmd = "kill " + argv[1][9:]
window = Tk()
window.title("Logout")
output_stream = popen("xrandr")
lines = output_stream.read().split("\n")
pattern = re.compile(r"(\d+)x(\d+)\+(\d+)\+(\d+)")
W = 475
H = 225
X = 0
Y = 0
def restart():
    window.destroy()
    system("bash -c \"sudo /usr/sbin/do restart\"")
def shutdown():
    window.destroy()
    system("bash -c \"sudo /usr/bin/do shutdown\"")
def suspend():
    window.destroy()
    system("slock")
    system("bash -c \"sudo /usr/bin/do suspend\"")
def logout():
    window.destroy()
    system(logout_cmd)
def lock():
    window.destroy()
    system("slock")
for a in lines:
    if " connected primary" in a:
        w, h, x, y = pattern.search(a).groups()
        w = int(w); h = int(h); x = int(x); y = int(y);
        X = int(w/2 - W/2 + x)
        Y = int(h/2 - H/2 + y)
window.geometry(str(W)+"x"+str(H)+"+"+str(X)+"+"+str(Y))
window.resizable(False, False)
window.attributes('-topmost', True)
bg = "#0a0a0f"
fg = "#ffaaff"
bd = 0
activebg = "#8f17d7"
activefg = "#ffcfff"
highlightcolor = "#8f17d7"
window.configure(bg="#0a0a0f")
restart_button  = Button(window, text="Restart",  bg=bg, fg=fg, bd=bd, activebackground=activebg, activeforeground=activefg, highlightcolor=highlightcolor, command=restart)
restart_button    .place( x=25, y=25,  width=125, height=75)
shutdown_button = Button(window, text="Shutdown", bg=bg, fg=fg, bd=bd, activebackground=activebg, activeforeground=activefg, highlightcolor=highlightcolor, command=shutdown)
shutdown_button   .place(x=175, y=25,  width=125, height=75)
suspend_button  = Button(window, text="Suspend",  bg=bg, fg=fg, bd=bd, activebackground=activebg, activeforeground=activefg, highlightcolor=highlightcolor, command=suspend)
suspend_button    .place(x=325, y=25,  width=125, height=75)
logout_button   = Button(window, text="Log Out",  bg=bg, fg=fg, bd=bd, activebackground=activebg, activeforeground=activefg, highlightcolor=highlightcolor, command=logout)
logout_button     .place( x=25, y=125, width=125, height=75)
lock_button     = Button(window, text="Lock",     bg=bg, fg=fg, bd=bd, activebackground=activebg, activeforeground=activefg, highlightcolor=highlightcolor, command=lock)
lock_button       .place(x=175, y=125, width=125, height=75)
def close(e):
    if e.widget == window:
        window.destroy()
window.bind('<Escape>', close)
#window.bind('<FocusOut>', close)
window.mainloop()
