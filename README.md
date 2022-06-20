# Rutube_XD

Features :] :
 - Amazing download speeds
 - Up to 4k resolutions supported
 - Optimized for low resources
 - No useless code laying around (looking at you youtubedl)
 - Minimal libs required
 - Easy to Setup/Deploy
 - very low hardware/network usage
 - Supports Heroku/railway/local deploys
 - Completely safe no third-party libs used
   all data collected is safe (check requr.txt) 

<img src="./demo/demo1.jpg" alt="demo"/>
<img src="./demo/demo2.jpg" alt="demo"/>

enjoy :)

# Setup
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/Jj6vqk?referralCode=4_MSke)
[![Deploy on Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Justxd22/rutubeXD)

### Railway
it's easier to deploy on railway, it has free builtin redis db, 
and a deploy template everything is set up for you.
  - Click railway button
  - put your token/env in variables
  - enjoy!

### Heroku
  - click the heroku deploy button
  - make a new bot with bot father on telegram copy token
  - paste your token and other env, then deploy
  - enjoy!

### Local deploy
## Normal 
  - clone this repo
    `git clone https://github.com/Justxd22/rutubeXD && cd rutubeXD/`
  - install requirements with pip
    `pip install ./requirements.txt`
  - fill in stuff.py with your env
  - Install ffmpeg if you're on linux use apt if not google 'how to install ffmpeg'
    `apt install ffmpeg`
  - run bot.py
    `python3 bot.py`
  - enjoy!! :]

## Docker
  - Clone or download Dockerfile
  - set your env in .env.sample file  
    then rename it to .env
  - Build Dockerfile  
    `docker build .`
  - Find image id then run it  
    `docker images` --> copy your image id  
    `docker run YOURID`  
    Or run with -it to see logs  
    `docker run -it YOURID` 


# Credits

[@pyrogram](https://github.com/pyrogram/pyrogram) - telegram bot api

pm on telegram for any queries [@Pine_Orange](t.me/Pine_Orange) or [@xd2222](t.me/xd2222)

# Donations
You can support my work by donating to the following address,
THANKS KIND FRIEND!
  - XMR - `433CbZXrdTBQzESkZReqQp1TKmj7MfUBXbc8FkG1jpVTBFxY9MCk1RXPWSG6CnCbqW7eiMTEGFgbHXj3rx3PxZadPgFD3DX`
