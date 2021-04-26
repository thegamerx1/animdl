AnimDL - Batch Downloader & Stream URL Fetcher
---

AnimDL is a reliable program to download all your anime(s) from a proper server.

Furthermore, this program contains various utilities that will be able to help you make a even greater client.

There is a user-friendly cli tool included with the project.!

The batch downloader included in the program (`cli_old.py`) can be configured using the `config.env` file which also has an example `config.env.example` to help you configure your downloader.

Requirements
---

- Python 3.8 +
- requests
- tqdm
- lxml.html

**Disclaimer**

Downloading copyrighted materials might be illegal in your country.

Additional Information
---

This uses AnimixPlay.To and/or Twist.Moe as the provider of stream urls and in case of AnimixPlay.To, currently, only GogoAnime streams are supported. You can't really select the quality of the anime as it is the raw quality provided; the quality will fluctuate from 480p to 1080p in AnimixPlay and from 720p to 1080p in Twist.Moe.

You may edit or modify the code based on your need. You may recieve help from the developer in any sort of modification you're performing as long as it's not some edgy stuff.

Complete support for TwistMoe (using mechanism similar to [this](https://github.com/justfoolingaround/twistmoe-download-utils)) has been added.

Clickable terminal texts have been removed due to their false length that was expected to cause issue with tqdm.

**Developer Note:** Unless you're using a internet connection >250 Mbps, TwistMoe downloads will have massive fluctuations (downloads that are expected to happen in 2-3 minutes by tqdm could be held back to 2-3 times based on your internet speed). This is due to how the CDN processes the things; for now, there is no solution. 
Even in an unlikely use-case (assuming you're too rich to use these measly tools), like in >250 Mbps internet, download expected to happen in 10-20 seconds extended upto a minute. 
A concurrent/threaded mechanism also proved useless in this case due to same errors. 

If you are rate-limited during a download from twistcdn, you can simply re-run the downloader and it will try to continue from where it left.