import regex
from functools import partial
import lxml.html as htmlparser
from ....config import ANIMEFENIX
from ...helper import construct_site_based_regex

REGEX = construct_site_based_regex(
    ANIMEFENIX, extra_regex=r'/(?:ver/(?P<episodeslug>.+?)-\d+|(?P<slug>[^&/#?]+))')

IFRAME_EXTRACT = regex.compile(rb"iframe.*src=['\"](?P<url>.+?)['\"]")


def extract_urls(session, episode_page):
    episode_page_content = session.get(episode_page)
    scriptag = htmlparser.tostring(htmlparser.fromstring(
        episode_page_content.text).cssselect(".player-container script")[0])
    links = (_.group("url").replace(b"&amp;", b"&")
             for _ in regex.finditer(IFRAME_EXTRACT, scriptag))

    embeds = []
    for link in links:
        redirect = session.get(link.decode())
        url = regex.findall(IFRAME_EXTRACT, redirect.text.encode())[0].decode()
        # if url is a relative url "../" or "/"
        # replace with animefenix.com
        if url.startswith("../"):
            url = url.replace("../", ANIMEFENIX)
        elif url.startswith("/"):
            url = url.replace("/", ANIMEFENIX, 1)

        if "mega.nz" in url:
            continue

        embeds.append({"stream_url": url, "referer": ANIMEFENIX})

    return embeds


def fetcher(session, url, check, match):
    url = match.group(0)

    episode_list_page = session.get(url)
    html = htmlparser.tostring(htmlparser.fromstring(episode_list_page.text).xpath(
        "/html/body/div[2]/section[2]/div[2]/div/div[2]/ul/li[3]")[0])
    count = int(regex.findall(regex.compile(rb'(\d+)</li>'), html)[0])

    for episode in range(1, count + 1):
        if check(episode):
            # yield partial((lambda e: [*get_stream_urls(e)]), episode_data), episode_number
            # yield partial(lambda c: [*extract_urls(session, c)], "https://animefenix.com/ver/{:s}-{:d}".format(match.group("slug"), episode)), episode
            yield partial(lambda c: [*extract_urls(session, c)], "https://animefenix.com/ver/{:s}-{:d}".format(match.group("slug"), episode)), episode
