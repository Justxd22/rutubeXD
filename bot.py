import os, sys, time, json, random, traceback,\
       datetime, asyncio, string, asyncio, logging

from random import randint
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from stuff import *
from tube import fetch, download
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied, FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid


savedTokens = {}
processedUsers = {}
CURRENT_PROCESSES = {}
ADMINS = [800219239, 2107284001, 1033516714]

tube = Client("rutube",
      api_id = app_id, api_hash = app_hash,
      bot_token = token)

@tube.on_message(filters.private & filters.command("start") or filters.regex("🤖 Ping"))
async def start(client, message):
    await message.reply_text(start_msg0, reply_markup = keybd)
    await message.reply_sticker(stk5)
    await message.reply_text(start_msg1)
    await logger(client, message, logger1)

@tube.on_message(filters.private & filters.command("help") or filters.regex("⁉️ Help"))
async def help(client, message):
    user_id = message.from_user.id
    username = "@" + message.from_user.username
    frname = message.from_user.first_name
    lasname = message.from_user.last_name
    name = ""

    if username != "None":
       name = username
    elif frname != "None":
       name = frname
    elif username == "None" and frname == "None":
       name = str(user_id)

    await message.reply_text(help_text%name, reply_markup = keybd, disable_web_page_preview=True)
    await message.reply_sticker(stk8)


@tube.on_message(filters.private & filters.regex("thanks") or filters.regex("Thanks") or filters.regex("thank you") or filters.regex("Thank you") or filters.regex("😊 Thanks"))
async def thank(client, message):
    ran = randint(0, 1)
    if ran == 1:
        await message.reply_text("**You are welcome**", reply_markup = keybd)
    else:
        await message.reply_text("**it's my duty**", reply_markup = keybd)

    await message.reply_sticker(stk7)


@tube.on_message(filters.private & filters.regex("about") or filters.regex("👀Who?"))
async def about(client, message):
    user_id = message.from_user.id
    username = "@" + message.from_user.username
    frname = message.from_user.first_name
    lasname = message.from_user.last_name
    name = ""

    if username != "None":
       name = username
    elif frname != "None":
       name = frname
    elif username == "None" and frname == "None":
       name = str(user_id)

    await message.reply_text(about_text, reply_markup = keybd, disable_web_page_preview=True)
    await message.reply_sticker(stk5)


@tube.on_message(filters.command("report"))
async def report(client, message):
    tex = message.text
    try:
       mes = message.reply_to_message.id;
       mes = await client.get_messages(message.chat.id, mes)
       mes = mes.text

    except: mes = None

    if len(tex) == 7 and mes is None or tex == "⚠️ REPORT"  and mes is None:
       await message.reply_text(logger4)
       await message.reply_sticker(stk0)
    else:
       await message.reply_text("**Reported to admins**")
       await message.reply_sticker(stk0)
       text = "**User Reported** \n\n" + tex + "\n " + str(mes) + f"\n\n {message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} {message.from_user.mention}"
       await client.send_message("Pine_Orange", text)
       await client.send_message("1033516714", text)

    await logger(client, message, logger3, tex)


@tube.on_message(filters.command(["warnu"]))
async def warnu(client, message):
    if message.from_user.id not in ADMINS:
        await message.reply_text("**You aren't authorized to use this command**")
        return
    if len(message.command) == 1:
        await message.reply_text("""You can use this cmd to send message to specific user
\nSend message is this format in order to send message to specific user\n/warnu {user I'd to whom you want to send message} {message to send the user}\n
Eg :- /warnu 1234567890 Hi""")
        return

    try:
        user_id = int(message.command[1])
        sk_mes = message.reply_to_message.id;
        sk_mes = await client.get_messages(message.chat.id, sk_mes)
        sk_mes = sk_mes.text

        sk_reply = await message.reply_text(
                       text=f"Sending message to <a href='tg://user?id={user_id}'><b>User</b></a>",
                       disable_web_page_preview=True,
                       parse_mode='HTML'
        )
        await client.send_message(
                user_id,
                f"""**{sk_mes}**""", disable_web_page_preview=True)
        await sk_reply.delete()
        await message.reply_text(
            text=f"Message sent successfully to <a href='tg://user?id={user_id}'><b>User</b></a>",
            disable_web_page_preview=True,
            parse_mode='HTML'
        )
    except:
        traceback.print_exc()
        await message.reply_text(f"User notification failed \n\n<code>{traceback. format_exc()}</code>")


async def logger(c, m, msg, text=""):
    client = c; message = m;
    if not logGroup: return
    ms = msg + text + f"\n\n{message.from_user.first_name} {message.from_user.last_name} @{message.from_user.username} {message.from_user.id} {message.from_user.mention}"
    await client.send_message(logGroup, ms, disable_web_page_preview=True)

@tube.on_message(filters.text & filters.private)
async def ru(client, message):
    link = message.text
    if "🤖 Ping" in link: await start(client, message); return
    elif "⁉️ Help"  in link: await help(client, message); return
    elif "👀Who?" in link: await about(client, message); return
    elif "⚠️ REPORT" in link: await report(client, message); return
    elif "😊 Thanks" in link: await thank(client, message); return

    await logger(client, message, logger2, link)


    if "ru" in link:
        await message.reply_sticker(stk4)
        msg = await message.reply_text("Working on it...")
        savetoken = await fetch(client, message, msg, link)
        savedTokens[message.from_user.id] = savetoken
    else:
        print(len(link), "ru" in link, link)
        await message.reply_sticker(stk2)
        await message.reply_text(msg11)

@tube.on_callback_query()
async def calls(client, message):
    data = message.data
    save = savedTokens[message.from_user.id]
    await message.answer()

    if not  message.from_user.id in savedTokens:
       await message.message.edit_text("**Sorry this Process Expired** resend a link")
       return

    if message.from_user.id in processedUsers and processedUsers[message.from_user.id] == "processing":
       await message.message.edit_text("**Only One task at a time**")
       return

    res1, res2  = data.split("|")
    res = (int(res1),int(res2))

    tex = "Hold on!, "; ran = randint(0, 1);
    if ran == 0: tex = "Wait up!, "
    await message.message.edit_text(tex + msg2)
    processedUsers[message.from_user.id] = "processing"
    processState = await download(client, message, save, res)
    processedUsers[message.from_user.id] = processState




tube.run()
