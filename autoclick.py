import pyautogui as pag
import time
import keyboard
import mss
import cv2
import numpy as np

unit = [[(640,1240),(880,1420)],   
[(980,1240),(1200,1420)],
[(1300,1240),(1540,1420)],
[(1630,1240),(1860,1420)],
[(1960,1240),(2200,1420)],
[(640,1490),(880,1660)],
[(980,1490),(1200,1660)],
[(1300,1490),(1540,1660)],
[(1630,1490),(1860,1660)],
[(1960,1490),(2200,1660)]]

gameover = [(1000,1536),(1870,1643)]
gameover_rect = {'left':1000,'top':1536,'width':870,'height':107}

def gamebreak():
    with mss.mss() as sct:
        rgb = np.mean(np.array(sct.grab(gameover_rect))[:,:,:3],axis = (0,1))
        if 14<rgb[0]<15 and 166<rgb[1]<167 and 217<rgb[2]<218:
            pag.click((gameover[0][0]+gameover[1][0])//2,(gameover[0][1]+gameover[1][1])//2)
            return False

running = True
while running:
    if keyboard.is_pressed('p'):
        break

    for i in range(10):
        if gamebreak() == False:
            running = False
            break
        time.sleep(0.12)
        pag.click((unit[i][0][0]+unit[i][1][0])//2,(unit[i][0][1]+unit[i][1][1])//2)

