from pyrogram import enums
import m3u8 as m3u
import asyncio, os, time, math, re, json
from requests import get
from stuff import msg0, msg1, msg2, msg3, msg4, msg6, msg7, msg8, msg9, msg10, msg11, stk0, stk1, stk3, fthl, headers
from saveProgress import Save
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from urllib.request import urlretrieve

blackbar = "●"
whitebar = "○"

async def fetch(c, m, fetch, link):
    rupt   = 'https?://rutube\.ru/(?:video|(?:play/)?embed)/(?P<id>[\da-z]{32})'
    search = re.search(rupt, link)
    if not search:
       await m.reply_text('**Please send valid rutube link!**')
       await fetch.delete()
       await m.reply_sticker(stk0)
       return

    id = search.groups()[0]
    try:
       data = get(f'http://rutube.ru/api/video/{id}' , headers=headers)
       vid  = get(f'http://rutube.ru/api/play/options/{id}',  headers=headers)
       data = json.loads(data.text)
       vid  = json.loads(vid.text)

       m3u8d = vid["video_balancer"]["m3u8"]
       m3u8d = get(m3u8d, headers=headers)
       m3u8  = m3u.loads(m3u8d.text)

       title = data['title']
       times = data['duration']
       date  = (data['created_ts']).split('T')[0]
       thumbnail = data['thumbnail_url']
       views = data['hits']
       author  = data['author']['name']
       channel = data['author']['site_url']

    except Exception as e:
       if "429" in str(e):
          print(msg6, str(e))
          await m.reply_text(msg6)
          await fetch.delete()
          await m.reply_sticker(stk0)
          return

       print(e)
       await fetch.delete()
       await m.reply_text(str(e))
       await m.reply_sticker(stk0)
       return

    mins = 0; secs = 0
    length = ""
    while 11111:
        if times > 59:
            times -= 60; mins += 1
        else:
            secs = times; length = f"{mins}:{secs}"
            break

    msgFetch = f"""
**Title:** {title}
**Author:** <a href="{channel}"><b>{author}</b></a>
**Length:** {length}
**Views:** {views}
**Date:** {date}"""

    msgFetch += "\n\n"
    await fetch.delete()

    theButtonsV = []
    streams = m3u8.playlists

    for stream in streams:
        res = stream.stream_info.resolution[1]
        if res > 1080:
           if res > 1080 and res < 1920:
              res = "2k"
           elif res > 1990: res = "4k"
        else: res = str(res) + "p"
        #TODO calc video size from bitrate and length
#        size = humanbytes(stream.filesize_approx)
        buttonText = f"{res}"
#        if size is None: buttonText = f"{res}\n{tex}"
        cdata  = f"{stream.stream_info.resolution[0]}|{stream.stream_info.resolution[1]}"
        button = [InlineKeyboardButton(str(buttonText), callback_data=cdata)]
        theButtonsV.append(button)

    ioV = []
    for item in theButtonsV: ioV.append(item[0])
    theButtonsVCraft = [[i1, i2] for i1, i2 in zip(ioV[::2], ioV[1::2])]
    if len(theButtonsV)%2 == 1:
       theButtonsVCraft.append(theButtonsV[-1])
    theButtonsV = theButtonsVCraft
    replyButtons = InlineKeyboardMarkup(theButtonsV)
    msg = await m.reply_photo(thumbnail, caption=msgFetch + msg4, reply_markup=replyButtons, quote=True)
    saveToken = Save(streams, c, m, msg, title, author, thumbnail, data['duration'], msgFetch)
    return saveToken

async def download(c, m, savetoken, res):
    streams = savetoken.getSteams()

    try: thumb = urlretrieve(savetoken.thumb)[0]
    except Exception as e: print(str(e));

    try:
       link = None
       for stream in streams:
           if stream.stream_info.resolution == res:
              link = stream.uri
              break

       if not link:
          await m.message.edit_text("**Can't find Video Quality You selected** Something went wrong")
          await m.message.reply_sticker(stk0)
          return "processed"


       path = savetoken.title + ".mp4"
       cmd  = f"ffmpeg -y -i '{link}' -c copy -id3v2_version 3 -metadata title='{savetoken.title}' -metadata artist='{savetoken.artist}' '{path}'"

       code = await runShell(cmd, savetoken)
       if code != 0:
          await m.message.edit_text(msg8%code)
          return  "processed"

       await m.message.edit_text(savetoken.info + "**Uploading...**")
    except Exception as e:
        if "429" in str(e):
            print(msg6, str(e))
            await m.message.edit_text(msg6)
            await m.message.reply_sticker(stk0)
            return

        print(e)
        await m.message.edit_text(str(e))
        await m.message.reply_sticker(stk0)
        return "processed"

    media = open(path, 'rb')
    print(savetoken.title)
    tim = time.time()
    try:
       await c.send_chat_action(m.from_user.id, enums.ChatAction.UPLOAD_VIDEO)
       await c.send_video(chat_id = m.from_user.id, video=media,
                caption = savetoken.title,
                file_name = savetoken.title,
                thumb = thumb,
                duration = savetoken.length,
                reply_to_message_id = m.message.reply_to_message.id,
                progress=progresss,
                progress_args=(m.message, tim, savetoken.title, savetoken.info))
       os.remove(path)

    except Exception as e:
       print(e)
       await m.message.edit_text(str(e))
       await m.message.reply_sticker(stk0)
       os.remove(path)
       return "processed"


    return "processed"


async def tHePrOgReSsHoOk(timedone, times, savetoken):
    downloadprogress = ((times - timedone)*100)/times

    #Not the best progressbar in the world but it works!
    if downloadprogress <= 1: # 1
       blackbars = 0; whitebars = 20
    elif downloadprogress <= 5: # 2 3 4 5
       blackbars = 1; whitebars = 19
    elif downloadprogress <= 10: # 6 7 8 9 10
       blackbars = 2; whitebars = 18
    elif downloadprogress <= 15: # 11 12 13 14 15
       blackbars = 3; whitebars = 17
    elif downloadprogress <= 20: # 16 17 18 19 20
       blackbars = 4; whitebars = 16
    elif downloadprogress <= 25: blackbars = 5; whitebars = 15;
    elif downloadprogress <= 30: blackbars = 6; whitebars = 14;
    elif downloadprogress <= 35: blackbars = 7; whitebars = 13;
    elif downloadprogress <= 40: blackbars = 8; whitebars = 12;
    elif downloadprogress <= 45: blackbars = 9; whitebars = 11;
    elif downloadprogress <= 50: blackbars = 10; whitebars = 10;
    elif downloadprogress <= 55: blackbars = 11; whitebars = 9;
    elif downloadprogress <= 60: blackbars = 12; whitebars = 8;
    elif downloadprogress <= 65: blackbars = 13; whitebars = 7;
    elif downloadprogress <= 70: blackbars = 14; whitebars = 6;
    elif downloadprogress <= 75: blackbars = 15; whitebars = 5;
    elif downloadprogress <= 80: blackbars = 16; whitebars = 4;
    elif downloadprogress <= 85: blackbars = 17; whitebars = 3;
    elif downloadprogress <= 90: blackbars = 18; whitebars = 2;
    elif downloadprogress <= 95: blackbars = 19; whitebars = 1;
    elif downloadprogress <= 100: blackbars = 20; whitebars = 0;
    messa = blackbar*blackbars + whitebar*whitebars
#    print(messa)

    letter, fileName, info = typeToDownload.split("|")
    fileName = savetoken.title + ".mp4"
    Mediasize = savetoken.size
    tex = f"""
╭───[**Dᴏᴡɴʟᴏᴀᴅɪɴɢ Yᴏᴜʀ Fɪʟᴇ**]───⍟
│
├<b>📁 Fɪʟᴇ Nᴀᴍᴇ : {fileName}</b>
│
├<b>🗂 Fɪʟᴇ Sɪᴢᴇ : {Mediasize}</b>
│
├<b>✅ Dᴏɴᴇ : {downloadprogress}%</b>
│
├<b>📥 : [{messa}]</b>
╰─────────────────⍟"""

    return tex

#TODO Handle 402 403 http errors from ffmpeg output
#TODO Figure asyncio live stdout of ffmpeg to make progress bar
async def runShell(cmd,savetoken):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stderr = ""
    while 1:
        line = await proc.stderr.readline()
        if line:
           stderr += '\n' + str(line)
        else: break

    print(f'[cmd exited with {proc.returncode}]')
    if not proc.returncode:
       print(1) # placeholder
    elif stderr and proc.returncode != 0:
       print(f'[stderr]\n{stderr}')
       return proc.returncode

    return 0


def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'

async def progresss(current, total, message, start, name, info):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff

        progress = """\n
╭───[**Uᴘʟᴏᴀᴅɪɴɢ Yᴏᴜʀ Fɪʟᴇ**]───⍟
│
├<b>📁 Fɪʟᴇ Nᴀᴍᴇ : {6}</b>
│
├<b>✅ Dᴏɴᴇ : {3} / {4}</b>
│
├<b>🚀 Pʀᴏɢʀᴇss : {2}%</b>
│
├<b>📥 : [{0}{1}]</b>
│
├<b>⚡ Sᴘᴇᴇᴅ : {5}/s</b>
╰─────────────────⍟""".format(
            ''.join(["●" for i in range(math.floor(percentage / 5))]),
            ''.join(["○" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2),
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed), name)

        try:
           uploads = await message.edit(text=info + "\n" + "{}".format(progress))
        except: pass
        await uploads.edit_text(text=info)
