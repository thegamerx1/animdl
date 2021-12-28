from pypresence import Presence
from time import time
from ...__version__ import __core__

RPC = Presence(925463604923338832)
start_time = time()
anime = ""


def start(text):
    global anime
    anime = text or "Fix ltr"
    RPC.connect()


def episode(ep, max):
    if anime == "":
        return
    RPC.update(start=start_time, large_image='icon', large_text='AnimDL {}'.format(
        __core__), small_image='play', small_text='Playing', state='Episode {} of {}'.format(ep, max), details="Watching {}".format(anime))
