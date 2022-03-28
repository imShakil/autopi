#!/usr/bin/python3

import random
import subprocess
import sys
import time

if sys.version_info.major < 3:
    print("This script runs under python3")
    sys.exit()

missing_packages = ['scrot', 'python3-tk', 'python3-dev']


def packages():
    try:
        for package in missing_packages:
            subprocess.check_call(['apt-get', 'install', '-y', package])
    except IOError:
        print(IOError)
        sys.exit()


try:
    from tkinter import *
    from tkinter import ttk
    import pyautogui
except ImportError as e:
    packages()
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyautogui'])

from tkinter import *
from tkinter import ttk
import pyautogui as pyg

app = Tk()
app.geometry("400x300")
app.minsize(400, 300)
app.title('Play Auto Movement Game')
text_box = Text(app, height=30, width=300)
running = False


def popup(msg):
    text_box.pack()
    text_box.delete("1.0", "end")
    text_box.insert('end', msg)
    text_box.update()
    time.sleep(1)


def on_start():
    global running
    running = True
    popup("Program will be started soon.")
    app.after(1000, auto_py)


def on_stop():
    global running
    running = False
    popup("Program has stopped.\nPress [START] to run again.")


def on_destroy():
    app.destroy()


def switch_tab():
    pyg.sleep(5)
    pyg.hotkey('ctrl', 'tab')


def refresh_window():
    pyg.sleep(5)
    pyg.hotkey('f5')


def move_mouse(s_time):
    px, py = pyg.position()
    if time.time() - s_time >= 20:
        return

    px = (px + random.randint(0, 1920)) % 1920
    py = (py + random.randint(0, 1080)) % 1080
    pyg.moveTo(px, py, 1)
    move_mouse(s_time)


def auto_py():
    if running:
        popup("Program is running.")
        switch_tab()
        refresh_window()
        pyg.scroll(5000, 10)
        pyg.scroll(5000, -10)
        move_mouse(time.time())
        popup('Looping...\nProgram will run again after 30 seconds.\nPress [STOP] to stop the program.')
        app.after(30000, auto_py)


start = ttk.Button(app, text="start", command=on_start)
start.pack(padx=10, pady=10)

stop = ttk.Button(app, text="stop", command=on_stop)
stop.pack(padx=30, pady=10)

destroy = ttk.Button(app, text="Exit", command=on_destroy)
destroy.pack(padx=50, pady=10)


app.after(1000, auto_py)
app.mainloop()
