import datetime
import time


# print(datetime.datetime.utcnow())


def log(message, dt=datetime.datetime.utcnow()):
    print(dt, message)


# log('uruchomienie systemu')

def logi(*args):
    for command in args:
        log(command)
        time.sleep(2)


logi('uruchomienie systemu', 'logowanie', 'restart', 'wylogowanie', 'zamknięcie systemu')

