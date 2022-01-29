from pypresence import Presence
from time import time
from ...__version__ import __core__
from threading import Thread

failed = False
try:
    RPC = Presence(925463604923338832)
except:
    failed = True
    print("Discord presence failed")

start_time = time()
anime = ""


def start_connection():
    if failed:
        return
    RPC.connect()


def start(text):
    global anime
    anime = text
    thread = Thread(target=start_connection)
    thread.start()


def episode(ep):
    global failed
    if failed:
        return

    if anime == "":
        return
    RPC.update(start=start_time, large_image='icon', large_text='AnimDL {}'.format(
        __core__), small_image='play', small_text='Playing', state='Episode {}'.format(ep), details=anime)
