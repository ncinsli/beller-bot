import os
from telebot import *
from termcolor import colored

duration = 3000 #Config
port = 10

def init():
    os.system(f'echo {port} > /sys/class/gpio/export')
    os.system(f'echo out > /sys/class/gpio/gpio{port}/direction')

def start_ring():
    print(colored('🔔 [DAEMON] RING!', 'blue'))
    os.system(f'echo 1 > /sys/class/gpio/gpio{port}/value')

def start_pre_ring():
    print(colored('🔔 [DAEMON] PRE RING!', 'green'))
    os.system(f'echo 1 > /sys/class/gpio/gpio{port}/value')

def stop_ring():
    print(colored('🔔  [DAEMON] STOP RING', 'blue'))
    os.system(f'echo 0 > /sys/class/gpio/gpio{port}/value')
