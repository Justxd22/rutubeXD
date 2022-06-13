import os, datetime, sys, json
from pyrogram.types import ReplyKeyboardMarkup


token = os.getenv("token", "") #telegram bot token
app_id = os.getenv("app_id", "")
app_hash = os.getenv("app_hash", "")
logGroup =  os.getenv("logGroup", False) # change this to group id

x = datetime.datetime.utcnow()
i = x + datetime.timedelta(hours=3)
y = i.strftime("%Y-%m-%d_%I:%M%P")
print(y)
print("My PID is:", os.getpid())


if len(str(token)) < 5: print("please put your token in env"); sys.exit(1)


keybd = ReplyKeyboardMarkup([
     ['🤖 Ping', '⁉️ Help', '👀Who?'],
     ['⚠️ REPORT', '😊 Thanks']], resize_keyboard=True)


stk0 = "CAADBAADrgcAAnILQFPgjUtxHDj-oQI"
stk1 = "CAADBAADlQoAAo8RQFOWkvFydBKJlwI"
stk2 = "CAADBAADSAsAAn_eOFPurvLfXO2hzAI"
stk3 = "CAADBAAD0QoAAkKSOFND8vqd0dBlhQI"
stk4 = "CAADBAADRgkAAhzwOFMQTCV2uQABp4wC"
stk5 = "CAADBAADHwoAAgTjOFPwcaIN8VE3uQI"
stk6 = "CAADBAAD2AgAAv1sOFOBvhMuUqdpVgI"
stk7 = "CAADBAAD_AkAAzI4U1zm0zS8ZmfzAg"
stk8 = "CAADBAADZQoAAvmvQFN_0Kq6nbL7IAI"
fthl = "CAACAgEAAxkBAAEDhMhhv1eWCc2bLbg8V5ZW2w7v5lVz0QAClQEAAjT0-UWjXL_zWuG_FiME"

start_msg0 = "Hi human,"
start_msg1 = "I'm very fast **RUTUBE DOWNLOADER** \n\nI can download any video from rutube\n\nJust send me any rutube links to start"

help_text = """ Hi %s,

Welcome to **PLACE_HOLDER** 👋

I can download rutube links with instant speed
just send a link and grab a coffee

🔴🔴 **Notes** 🔴🔴
┏━━━━━━━━━━━━━━━━━━━━━━
• **Bot** is completely free for use,
• So please don't abuse/spam the bot
• After **Download Finshes** you can save to your downloads directory,
• Directly by long pressing a song then **Click save to Downloads**
• Reply to **/report** to report any bugs
• Make sure you report the error link too
• Check out **/about**
┗━━━━━━━━━━━━━━━━━━━━━━━

** ⚠️ REPORT any bugs at @xd2222 ⚠️ **"""

about_text = """
╭────[🔅Rutube Bᴏᴛ🔅]───⍟
│
├<b>🤖 Bot Name : Rutube</b>
│
├<b>💢 Source : <a href='https://github.com/Justxd22/rutubeXD'>Justxd22/rutubeXD</a></b>
│
├<b>🌐 Server : <a href='https://heroku.com'>Heroku</a></b>
│
├<b>📕 Library : <a href='https://github.com/pyrogram'>Pyrogram 1.2.8</a></b>
│
├<b>㊙ Language: <a href='https://www.python.org'>Python 3.9.4</a></b>
│
├<b>👨‍💻 Developer : <a href='https://github.com/Justxd22'>Justxd22</a></b>
│
╰──────[Thanks 😊]───⍟"""

msg0 = "**Fetching Link...**"
msg1=  "**Sorry But I can't get this link for you** (private content)"
msg2 = "**Downloading.....**"
msg3 = "**Download Finished**\n\n**Uploading**......"
msg4 = "**Please choose a Video quality** you would like to download"
msg5 = "**Please choose Audio quality** for the Video you selected"
msg6 = "**Got a 429 error (HTTP Too many reqests)** \nplease report any problems to @bryllbots_support \n I will reboot now, Please retry after 1 min"
msg7 = "**Video downloaded, Downloading Audio....**"
msg8 = "**Error code %s** Kindly report this"
msg9 = "**Joining Video with Audio you Selected....**"
msg10 = "**Huh?** you don't want video or audio,\nthen what do you want??"
msg11 = "**Please Send a Valid RUTUBE Link**"
msg12 = "**Sorry, the Link you requested is age-restricted**"
msg13 = "**Sorry, this video is Private**"
msg14 = "**Sorry, this video is Region Blocked**"
msg16 = "**Regex Error, Please report this issue** along with the link"

logger1 = "**New user!!**"
logger2 = "**User Says**:\n\n"
logger3 = "**User Wants To report** \n\n"
logger4 = "you have to say something like **/report video isn't playable**\nOr reply to a message\n\n** ⚠️ REPORT any bugs at @bryllbots_support  ⚠️ **"
logger5 = "**User is Happy** says thanks "


headers = {
       'Connection': 'keep-alive',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
       'cache-control': 'max-age=0',
       'Content-Type': 'application/json',
       'Accept': '*/*',
       'Origin': 'https://rutube.ru',
       'Sec-Fetch-Site': 'same-site',
       'Sec-Fetch-Mode': 'cors',
       'Sec-Fetch-Dest': 'empty',
       'Accept-Language': 'en-US,en;q=0.9'}
