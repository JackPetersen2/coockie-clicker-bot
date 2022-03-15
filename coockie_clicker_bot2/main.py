import cv2
import os
import time
import threading
import keyboard
import pyautogui
from pyautogui import *
import win32api, win32con
from pynput import keyboard
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, Key, KeyCode


delay = 0.0000000000000000001
button = Button.left
image='farm.png'
goldcookie='goldcookie.png'
start_stop_key = KeyCode(char='q')
start_stop_key2 = KeyCode(char='ø')
exit_key = KeyCode(char='e')






class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        self.factory=True

    def start_click(self):
        self.running = True
        print(f"start click",self.running)


    def stop_clicking(self):
        self.running = False
        print(f'stop click',self.running)



    def exit(self):
        self.stop_clicking()
        self.program_running = True

    def run(self):
        while self.program_running:
            while self.running:
                for i in range(0,1, 10000000):
                    mouse.click(self.button)
                    time.sleep(self.delay)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

class FindPhoto(threading.Thread):
    def __init__(self,delay,button,keyboard,image,goldcookie):
        super().__init__()
        self.delay = delay
        self.button = button
        self.keyboard = keyboard
        self.goldcookie = goldcookie
        self.image = image
        self.running1 = True
        self.images=(
            'goldcookie.png',
            'goldcookie2.png',
            'goldcookie3.png',
        )
        self.program_running = True

    def kill_switch(self):
        self.running1 = False
        print(f'kill switch',self.running1)
    def start_switch(self):
        self.running1 = True
        print(f'start switch',self.running1)
    def exit(self):
        self.running1 = False
        self.program_running = False

    def scroll(self,x,y):
        win32api.SetCursorPos((x,y))

        self.kill_switch()
        pyautogui.scroll(800,2)
        pyautogui.scroll(-800,2)

        self.start_switch()
        win32api.SetCursorPos((1108,532))

        time.sleep(10)
        self.running1 = False
        self.program_running = False
    def movemouse(self,x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.001)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.001)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    def run(self):

        while self.program_running:
            while self.running1:
                for i in range(0,1,100):
                    pic = pyautogui.screenshot(region=(970, 213, 400, 800))
                    width,height=pic.size
                    for x in range(0,width,1):
                        for y in range(0, height, 1):

                            r, g, b = pic.getpixel((x, y))
                            if r==range(200):

                                click(x + 970, y + 213)
                                print('goldencookie found')
                                time.sleep(.01)


                            else:
                                self.movemouse(1108,532)
                                click_thread.start_click()
                    self.scroll(1653,624)




findphoto = FindPhoto(delay, button,keyboard,image,goldcookie)
findphoto.start()








def on_press(key):
    if key == start_stop_key:
        if findphoto.running1:
            findphoto.kill_switch()

            print('--stop--')
            time.sleep(1.1)
            click_thread.stop_clicking()


        else:
            findphoto.start_switch()
            click_thread.stop_clicking()

            print('--start--')


    elif key == exit_key:
        click_thread.exit()
        findphoto.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
