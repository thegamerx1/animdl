"""
Fun helpers for the cli.

Credits for the functions:
    create_random_titles: (https://www.ruggenberg.nl/titels.html)
"""

import os

import logging
import regex
import yarl
from random import choice

from ...__version__ import __core__
from ..http_client import client

def line_chop(string: str, max_length, separators=[' ', '\n']):
    if not string:
        return

    if len(string) <= max_length:
        yield string
        return

    sep, sep_index = max(((_, string[:max_length].rfind(_)) for _ in separators), key=lambda x: x[1])

    if sep_index == -1:
        sep, sep_index = '', max_length

    yield string[:sep_index]
    yield from line_chop(string[sep_index + len(sep):], max_length, separators=separators)


def terminal_center(string: str, *, columns=os.get_terminal_size().columns):
    def genexp():
        for line in string.splitlines():
            for piece in line_chop(line, columns):
                yield piece.center(columns)
    return '\n'.join(genexp())

package_banner = terminal_center("""\
justfoolingaround/animdl - v{}
A highly efficient anime downloader and streamer\
""".format(__core__))


update_banner = terminal_center("""\
Version mismatch with upstream [↑ {}, ↓ {}]

Please consider updating to the latest version for ensuring bug fixes, code optimizations and new features. This can be done by using:

pip install git+https://github.com/justfoolingaround/animdl.git

Or,

py -m pip install git+https://github.com/justfoolingaround/animdl.git

(OCD? Yeah, can't fix that.)
""")


LANGUAGE = {
    'adjective': [
        'third',
        'obsessed',
        'seventh',
        'silent',
        'blue',
        'purple',
        'sacred',
        'hot',
        'lovely',
        'captured',
        'trembling',
        'burning',
        'professional',
        'first',
        'luscious',
        'black',
        'diamond',
        'misty',
        'next',
        'willing',
        'all',
        'lonely',
        'swollen',
        'forgotten',
        'no',
        'elemental',
        'what',
        'silver',
        'red',
        'living',
        'last',
        'sleeping',
        'bloody',
        'lost',
        'invisible',
        'whispering',
        'dark',
        'white',
        'naked',
        'which',
        'bare',
        'hidden',
        'fallen',
        'dangerous',
        'sucking',
        'wild',
        'ragged',
        'licking',
        'devoted',
        'kissing',
        'grey',
        'prized',
        'green',
        'missing',
        'silky',
        'growing',
        'darkest',
        'wet',
        'rough',
        'cracked',
        'bold',
        'bound',
        'slithering',
        'unwilling',
        'vacant',
        'delicious',
        'dying',
        'only',
        'erect',
        'some',
        'smooth',
        'absent',
        'eager',
        'playful',
        'silken',
        'falling',
        'laughing',
        'broken',
        'entwined',
        'rising',
        'hard',
        'sharp',
        'dwindling',
        'each',
        'splintered',
        'silvery',
        'stolen',
        'wanton',
        'final',
        'twinkling',
        'cold',
        'weeping',
        'stripped',
        'magnificent',
        'ravaged',
        'deep',
        'frozen',
        'shadowy',
        'emerald',
        'azure',
        'every'],
    'noun': [
        'dream',
        'dreamer',
        'dreams',
        'waves',
        'sword',
        'kiss',
        'sex',
        'lover',
        'slave',
        'slaves',
        'pleasure',
        'servant',
        'servants',
        'snake',
        'soul',
        'touch',
        'men',
        'women',
        'gift',
        'scent',
        'ice',
        'snow',
        'night',
        'silk',
        'secret',
        'secrets',
        'game',
        'fire',
        'flame',
        'flames',
        'husband',
        'wife',
        'man',
        'woman',
        'boy',
        'girl',
        'truth',
        'edge',
        'boyfriend',
        'girlfriend',
        'body',
        'captive',
        'male',
        'wave',
        'predator',
        'female',
        'healer',
        'trainer',
        'teacher',
        'hunter',
        'obsession',
        'hustler',
        'consort',
        'dream',
        'dreamer',
        'dreams',
        'rainbow',
        'dreaming',
        'flight',
        'flying',
        'soaring',
        'wings',
        'mist',
        'sky',
        'wind',
        'winter',
        'misty',
        'river',
        'door',
        'gate',
        'cloud',
        'fairy',
        'dragon',
        'end',
        'blade',
        'beginning',
        'tale',
        'tales',
        'emperor',
        'prince',
        'princess',
        'willow',
        'birch',
        'petals',
        'destiny',
        'theft',
        'thief',
        'legend',
        'prophecy',
        'spark',
        'sparks',
        'stream',
        'streams',
        'waves',
        'sword',
        'darkness',
        'swords',
        'silence',
        'kiss',
        'butterfly',
        'shadow',
        'ring',
        'rings',
        'emerald',
        'storm',
        'storms',
        'mists',
        'world',
        'worlds',
        'alien',
        'lord',
        'lords',
        'ship',
        'ships',
        'star',
        'stars',
        'force',
        'visions',
        'vision',
        'magic',
        'wizards',
        'wizard',
        'heart',
        'heat',
        'twins',
        'twilight',
        'moon',
        'moons',
        'planet',
        'shores',
        'pirates',
        'courage',
        'time',
        'academy',
        'school',
        'rose',
        'roses',
        'stone',
        'stones',
        'sorcerer',
        'shard',
        'shards',
        'slave',
        'slaves',
        'servant',
        'servants',
        'serpent',
        'serpents',
        'snake',
        'soul',
        'souls',
        'savior',
        'spirit',
        'spirits',
        'voyage',
        'voyages',
        'voyager',
        'voyagers',
        'return',
        'legacy',
        'birth',
        'healer',
        'healing',
        'year',
        'years',
        'death',
        'dying',
        'luck',
        'elves',
        'tears',
        'touch',
        'son',
        'sons',
        'child',
        'children',
        'illusion',
        'sliver',
        'destruction',
        'crying',
        'weeping',
        'gift',
        'word',
        'words',
        'thought',
        'thoughts',
        'scent',
        'ice',
        'snow',
        'night',
        'silk',
        'guardian',
        'angel',
        'angels',
        'secret',
        'secrets',
        'search',
        'eye',
        'eyes',
        'danger',
        'game',
        'fire',
        'flame',
        'flames',
        'bride',
        'husband',
        'wife',
        'time',
        'flower',
        'flowers',
        'light',
        'lights',
        'door',
        'doors',
        'window',
        'windows',
        'bridge',
        'bridges',
        'ashes',
        'memory',
        'thorn',
        'thorns',
        'name',
        'names',
        'future',
        'past',
        'history',
        'something',
        'nothing',
        'someone',
        'nobody',
        'person',
        'man',
        'woman',
        'boy',
        'girl',
        'way',
        'mage',
        'witch',
        'witches',
        'lover',
        'tower',
        'valley',
        'abyss',
        'hunter',
        'truth',
        'edge'],
}

LABELS = {
    'storage.googleapis.com': "Google API Storage",
    'v.vrv.co': 'VRV',
    'pl.crunchyroll.com': 'Crunchyroll' 
}


def create_random_titles():

    adjs = LANGUAGE.get('adjective')
    noun = LANGUAGE.get('noun')

    return [
        "{}-{}".format(choice(adjs), choice(noun)),
        "the-{}-{}".format(choice(adjs), choice(noun)),
        "{}-{}".format(choice(noun), choice(noun)),
        "the-{}'s-{}".format(choice(noun), choice(noun)),
        "the-{}-of-the-{}".format(choice(noun), choice(noun)),
        "{}-in-the-{}".format(choice(noun), choice(noun)),
    ]


def to_stdout(message, caller='animdl', *, color_index=36):
    if caller:
        message = "[\x1b[{}m{}\x1b[39m] ".format(color_index, caller) + message
    return print(message)


def stream_judiciary(url):

    try:
        url = yarl.URL(url)
    except Exception as e:
        return "Unknown [URL Parsing error.]"

    return "{!r} from {}".format(url.name or "Unknown", LABELS.get(url.host, url.host))


def check_for_update(*, current=__core__, git_version_url="https://raw.githubusercontent.com/justfoolingaround/animdl/master/animdl/core/__version__.py"):
    upstream_version = regex.search( r'__core__ = "(.*?)"', client.get(git_version_url).text).group(1)
    return upstream_version == current, upstream_version

def bannerify(f):
    def internal(*args, **kwargs):
        quiet_state = kwargs.get('log_level')
        if quiet_state is not None:
            if quiet_state <= 20:
                print("\x1b[35m{}\x1b[39m".format(package_banner))
                latest, version = check_for_update()
                if not latest:
                    print("\x1b[31m{}\x1b[39m".format(update_banner.format(version, __core__)))
            logging.basicConfig(
                level=quiet_state,
                format="[\x1b[35m%(filename)s:%(lineno)d\x1b[39m - %(asctime)s - %(name)s: %(levelname)s] %(message)s")
        return f(*args, **kwargs)

    return internal
