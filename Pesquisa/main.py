import pyautogui
print(pyautogui.position())

from random import randint
from time import sleep

lines = []
with open('palavras.txt') as f:
    lines = f.readlines()

for n in range(0, 10):
    pyautogui.click(379, 21, duration=1)

    query = lines[randint(1, 24903)].replace('\n', '').lower()

    pyautogui.click(894, 599, duration=1)
    pyautogui.typewrite(query, interval=0.3)

    pyautogui.hotkey('enter')
    pyautogui.click(94, 532, duration=1)
    for c in range(0, randint(2, 10)):
        pyautogui.scroll(-100)
        sleep(0.5)
    
    pyautogui.click(641, 13, duration=1)
    sleep(randint(0, 2))
