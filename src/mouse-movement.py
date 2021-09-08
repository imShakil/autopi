#!/usr/bin/python3

import time
import random
import pyautogui as pyg
from tkinter import *
from tkinter import ttk

app = Tk()
app.geometry("750x300")
app.minsize(750, 300)
app.title('Play Auto Movement Game')

running = False


def on_start():
    global running
    running = True
    print('Be Ready, The program started soon')
    app.after(1000, auto_py)


def on_stop():
    global running
    running = False
    print("Program stopped.")


def on_destroy():
    app.destroy()


def switch_tab():
    pyg.hotkey('ctrl', 'tab')


def refresh_window():
    pyg.hotkey('f5')


def move_mouse(s_time):
    px, py = pyg.position()
    if time.time() - s_time >= 40:
        return

    px = (px + random.randint(0, 1920)) % 1920
    py = (py + random.randint(0, 1080)) % 1080
    pyg.moveTo(px, py, 1)
    move_mouse(s_time)


def auto_py():
    if running:
        for _ in range(3):
            for i in range(3):
                sys.stdout.write('\rLoading{}'.format('.' * (i + 1)))
                sys.stdout.flush()
                time.sleep(1)
        print('\nProgram started.')
        time.sleep(3)
        switch_tab()
        time.sleep(3)
        refresh_window()
        time.sleep(3)
        pyg.scroll(10)
        time.sleep(3)
        pyg.scroll(-10)
        time.sleep(3)
        move_mouse(time.time())
        print('Looping...')
        time.sleep(10)
        app.after(1000, auto_py)


start = ttk.Button(app, text="start", command=on_start)
start.pack(padx=10, pady=10)

stop = ttk.Button(app, text="stop", command=on_stop)
stop.pack(padx=30, pady=10)

destroy = ttk.Button(app, text="Exit", command=on_destroy)
destroy.pack(padx=50, pady=10)

# Run a function to print text in window
app.after(1000, auto_py)
app.mainloop()
