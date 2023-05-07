import aiohttp
import base64
from pyrogram import enums
from userge import userge, Message
import time, os, math, requests, re, json
import datetime as DT
import requests as req
from pyrogram import Client, filters


header = {"AUTH_KEY":"meki"}


@userge.on_cmd(
    "ssh", about={
        'header': "Create SSH Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}ssh [domain:[user]:[pw]:[exp]"})
async def ssh(message: Message):
    """SSH account"""
    replied = message.input_str 
    if not replied:
        await message.edit("`JGN KOSONG BLOK!`")
        return
    elif ":" not in replied:
        await message.edit("`USER:PW:EXP !`")
        return
    await message.edit("`Tunggu Blog !`")
    async with aiohttp.ClientSession() as req:
        d = replied.strip().split(':')[0]
        u = replied.strip().split(':')[1]
        p = replied.strip().split(':')[2]
        e = replied.strip().split(':')[3]
        param = f":6969/adduser/exp??user={u}&password={p}&exp={e}"
        url = ("http://"+d+param)
        async with req.get(url, headers=header) as resp:
            if resp.status != "success":
            #return 
              today = DT.date.today()
              later = today + DT.timedelta(days=int(e))
              await message.edit(
              text=(f"**━━━━━━━━━━━━━━━━**\n"
              f"** ❗️ SSH Account ❗️** \n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**♟ Username:** `{u}`\n"
              f"**♟ Password:** `{p}`\n"
              f"**♟ Domain:** `{d}`\n"
              f"**♟ Port SSL :** `222, 443`\n"
              f"**♟ Port WS :** `80`\n"
              f"**♟ Port WS SSL :** `443`\n"
              f"** ━━━━━━━━━━━━━━━━**\n"
              f"**♟ PayLoad WS:**\n"
              f"**`GET / HTTP/1.1[crlf]Host: {d}[crlf]Connection: Keep-Alive[crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**♟ Exp Until:** `{later}`\n"
              f"**━━━━━━━━━━━━━━━━**\n"),
         
             disable_web_page_preview=True,
             parse_mode=enums.ParseMode.MARKDOWN
     
    
        )
        
@userge.on_cmd(
    "trialsh", about={
        'header': "Create SSH Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}trialsh [domain]"})
async def ssh(message: Message):
    """SSH account"""
    replied = message.input_str 
    if not replied:
        await message.edit("`JGN KOSONG BLOK!`")
        return
    await message.edit("`Tunggu Blog !`")
    async with aiohttp.ClientSession() as req:
        d = replied.strip().split(':')[0]
        param = f"/trial-ssh"
        url = ("http://"+d+param).text.split(":")
        async with req.get(url, headers=header) as resp:
            if resp.status != "success":
            #return
              await message.edit(
              text=(f"**━━━━━━━━━━━━━━━━**\n"
              f"** ❗️ Trial SSH Account ❗️** \n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**♟ Username:** `{url[0].strip()}`\n"
              f"**♟ Password:** `{url[1]}`\n"
              f"**♟ Domain:** `{d}`\n"
              f"**♟ Port SSL :** `222, 443`\n"
              f"**♟ Port WS :** `80`\n"
              f"**♟ Port WS SSL :** `443`\n"
              f"** ━━━━━━━━━━━━━━━━**\n"
              f"**♟ PayLoad WS:**\n"
              f"**`GET / HTTP/1.1[crlf]Host: {d}[crlf]Connection: Keep-Alive[crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**♟ Exp Until:** `30 Minutes`\n"
              f"**━━━━━━━━━━━━━━━━**\n"),
         
             disable_web_page_preview=True,
             parse_mode=enums.ParseMode.MARKDOWN
     
    
        )
