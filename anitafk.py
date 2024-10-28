from time import sleep
from PIL import Image

import random
import pyautogui as pg
import os
import keyboard
import threading
import multiprocessing
import pystray
import sys

exit_Process = None # Тут будем хранить объект multiprocessing.Process

# Функция для убийства приложения
def hook_exit():
    keyboard.wait('esc')
    print("!!!")
    exit_Process.terminate() # Перед закрытием программы завершаем процесс moveTo_pressF5
    os._exit(1)

# Функция для случайных движений мышкой и перезагрузки страницы
def antiafk():
    while True:
        a, b, c = random.randint(500,1000), random.randint(300,600), random.randint(1, 5)
        sleep(60)
        pg.moveTo(a, b, c)

# пока не работает
def create_tray_icon():
    icon = pystray.Icon("name", Image.open("troll.ico"), "Трей-иконка")
    icon.menu = pystray.Menu(
        pystray.MenuItem("Выйти", icon.stop, action=exit)
    )
    icon.run()

# Функция для закрытия
def exit():
    sys.exit()


if __name__ == '__main__':
    create_tray_icon()    
    # Создаем поток для выхода из программы по нажатию сочетания клавиш
    hook_exit_thread = threading.Thread(target=hook_exit)
    hook_exit_thread.start() # Запускаем поток
   
    while True:
        # Создаем Process для движении мыши и обновления страницы
        moveTo_pressF5_Process = multiprocessing.Process(target=antiafk)
        exit_Process = moveTo_pressF5_Process
        moveTo_pressF5_Process.start() # Запускаем Process

        os.system('cls' if os.name == 'nt' else 'clear')

        print("Running... \n\n")
        print("Нажмите 'Esc' для выхода \n\n")
        print('Нажмите ctrl + shift + alt + p что бы поставить скрипт на паузу')

        keyboard.wait("ctrl + shift + alt + p")
        moveTo_pressF5_Process.terminate()
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Нажмите 'Esc' для выхода \n\n")
        print('Скрипт приостановлен, нажмите ctrl + alt + p для продолжения')  
        
        keyboard.wait('ctrl + alt + p')