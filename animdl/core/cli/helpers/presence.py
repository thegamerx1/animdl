from pypresence import Presence
from time import time, sleep
from ...__version__ import __core__
from threading import Thread
import asyncio
from ..http_client import client

loop = asyncio.new_event_loop()
RPC = ""
connected = False
failed = True
start_time = time()
anime = ""
ep = 0

query = """{{
    Media(search: "{}") {{
        title {{
            romaji
            english
        }}
    }}
}}"""


def start_connection():
    global failed, connected, RPC, ep
    asyncio.set_event_loop(loop)
    # if rpc not connected retry infinitely
    while True:
        if failed:
            try:
                RPC = Presence(925463604923338832)
                failed = False
            except:
                failed = True
                print("Discord presence failed")
        else:
            if not connected:
                try:
                    RPC.connect()
                    connected = True
                except Exception as e:
                    connected = False
                    failed = True
                    print(e)

        if connected:
            update()

        sleep(15)


def start(text):
    global anime, query
    response = client.post("https://graphql.anilist.co", json={
        "query": query.format(text)
    })
    anime = response.json()['data']['Media']['title']['english']
    if anime == None:
        anime = text
    thread = Thread(target=start_connection)
    thread.start()


def update():
    global connected, RPC, ep
    if connected:
        try:
            RPC.update(start=start_time, large_image='icon', large_text='AnimDL {}'.format(
                __core__), small_image='play', small_text='Playing', state='Episode {}'.format(ep), details=anime)
        except Exception as e:
            connected = False


def episode(eps):
    global ep
    ep = eps
    update()
