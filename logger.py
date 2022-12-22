import locale
import time
from datetime import datetime

log_file = 'image.log'

def log(msg):
    """
        Insère un message avec une date d'execution dans le image.log
        :param msg: Un message
        Elle ne renvoie rien
    """

    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:%M:%S')
    formatted = f'{timestamp} - {msg}'

    #'a' = ajouter and 'w' = ecraser
    with open(log_file, 'a') as p:
        p.write(formatted + "\n")

def dump_log():
    """
        Sert à afficher dans le terminal le contenu de image.log
        Elle ne prend aucun paramètre et ne renvoie rien
    """

    with open(log_file, 'r') as p:
        print(p.read())
