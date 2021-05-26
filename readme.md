
![AnimDL Cover](https://raw.githubusercontent.com/justfoolingaround/animdl/master/assets/cover.png)

# AnimDL - Download & Stream your favorite anime

AnimDL is an incredibly powerful tool for downloading and streaming anime.

### Usage

```
animdl.py [( download | stream | grab ) --query QUERY | continue | help ]
```

### Installation

Clone / download the repo and simply run:

```
pip install -r requirements.txt
```

### Core features

- Abuses the developer's knowledge of internal streaming mechanisms in various different sites to hunt down high quality stream links.
- Doesn't make a single unnecessary request to any servers and rules out such requests.
- Doesn't use any heavy dependencies such as Selenium or Javascript Evaluators.
- Effectively bypasses DRMs in several streaming sites.
- Integrates AnimeFillerList so that the user can filter out any fillers from downloading or streaming.
- Only tool in existence to bypass [9Anime](https://9anime.to)'s cloudflare protection.
- Operates with full efficiency and speed by using Python's generator functions to their full capacity.
- Supports [bloc97/Anime4K](https://github.com/bloc97/Anime4K/) for real time anime upscaling.
- Supports streaming with [`mpv`](https://github.com/mpv-player/mpv/), an incredibly efficient, fast and light-weight dependency.

And along with these above features, AnimDL supports top anime sites (supported sites are mentioned below)!

### Supported Sites

| Website | Available Qualities | Status | Streamable | Downloadable |
| ------- | ------------------- | ------ | --------- | ------------ |
| [4Anime](https://4anime.to/) | 720p, 1080p | Working | Yes | Yes |
| [9Anime](https://9anime.to/) | 720p, 1080p | Working | Yes | Yes for MP4, no for m3u8 |
| [AnimeFreak](https://www.animefreak.tv/) | 720p, 1080p | Working | Yes | Yes |
| [AnimePahe](https://www.animepahe.com/) | 720p, 1080p | Working | Yes | No |
| [Animixplay](https://www.animixplay.to/) | 480p, 720p, 1080p | Working | Yes | Yes for MP4, no for m3u8 |
| [GogoAnime](https://www1.gogoanime.ai/) | 480p, 720p, 1080p | Working | Yes | Yes for MP4, no for m3u8 |
| [Twist](https://www.twist.moe/) | 720p, 1080p | Working | Yes | Yes |

If a site is not working, please don't worry, you're encouraged to make an issue! 

Want more sites? AnimDL seems to support the best sites currently but that doesn't mean we won't add more sites! You're encouraged to raise as many issues as possible for requests to add support for an anime site.

### Scraping from a site

If you've used the `cli.py`, you've probably noticed one thing. You can't choose a specific provider to download from. While it looks 
like that from the front, you can actually choose a specific provider by simply putting the URL to your anime from that site to the 
search query.

**For example:**

| Query | Will Recognize | Action |
| ----- | -------------- | ------ |
| [AnimePahe URL](https://animepahe.com/anime/b0c3ed18-0721-df22-574b-63dc56a57f68) | Yes | Will start scraping One Piece from AnimePahe |
| [AnimePahe Player URL](https://animepahe.com/play/b0c3ed18-0721-df22-574b-63dc56a57f68/321b254b5d2f1349dc49b6db4f43ff028591e51c1b3ce7f51f23e1c2d0606961) | Yes | Will convert to anime URL and start scraping One Piece from it. This will not download a singular episode. |
| [Twist URL](https://twist.moe/a/one-piece) | Yes | Will start scraping One Piece from Twist |
| [Animixplay URL](https://animixplay.to/v1/one-piece) | Yes | Will start scraping One Piece from Animixplay |
| `one piece` | No | Will search through Animixplay and show selections |

### Streaming

Streaming needs an additional dependency known as `mpv`, you can download it from [here.](https://github.com/mpv-player/mpv/releases/)

If you're having issues with the installation of mpv, you can make an issue to recieve full help on its installation and usage.

### Coming soon (features)

- HLS downloading; a support for downloading m3u8. There are libraries for this but they are not that efficient.
- GUI (Possibly with Javascript frameworks, don't worry, I'll pick the most efficient one)

### Disclaimer

Downloading or streaming copyrighted materials might be illegal in your country.