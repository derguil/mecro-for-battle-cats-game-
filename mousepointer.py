import pyautogui as pag
import time
import keyboard

while True:
    if keyboard.is_pressed('p'):
        print('quit')
        break
    x,y = pag.position()
    print('x: %d y: %d'%(x,y))