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
    "ssh_apik2", about={
        'header': "Create SSH Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}ssh_apik2 [user]:[pw]:[exp]"})
async def ssh(msg: Message):
    """SSH account"""
    replied = msg.input_str 
    if not replied:
        await msg.err("```Isi user:exp blok....```", del_in=5)
        return
    if ":" not in replied:
        await msg.err("```Format harus user:exp...```", del_in=5) 
        return
    if ":"":" not in replied:
        await msg.err("```Format harus user:exp...```", del_in=5) 
        return
    await msg.edit("```Sedang membuat akun, tunggu...```")
    async with aiohttp.ClientSession() as req:
        u = replied.strip().split(':')[0]
        p = replied.strip().split(':')[1]
        e = replied.strip().split(':')[2]
        param = f":6969/adduser/exp??user={u}&password={p}&exp={e}"
        url = ("http://apik2-ws.bhm.my.id"+param)
        async with req.get(url, headers=header) as resp:
            if resp.status != "success":
            #return 
              today = DT.date.today()
              later = today + DT.timedelta(days=int(e))
              await message.edit(
              text=(f"**━━━━━━━━━━━━━━━━**\n"
              f"** ⟨ SSH Account ⟩** \n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**Username:** `{u}`\n"
              f"**Password:** `{p}`\n"
              f"**Domain:** `apik2-ws.bhm.my.id`\n"
              f"**DNS Domain:** `apik2-wsnsque.keongdns.my.id`\n"
              f"**Port SSL :** `222, 777`\n"
              f"**Port WS :** `2082`\n"
              f"**Port WS SSL :** `443`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**PayLoad WS:**\n"
              f"**`GET / HTTP/1.1[crlf]Host: apik2-ws.bhm.my.id[crlf]Connection: Keep-Alive[crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**Pub Key Slowlkeong:**\n"
              f"**`d6f6c35b19edc459b976e4f8967404cd2d60afe76bfe1a691e7fd3eabdde0152`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**Exp Until:** `{later}`\n"
              f"**━━━━━━━━━━━━━━━━**\n"),
         
             disable_web_page_preview=True,
             parse_mode=enums.ParseMode.MARKDOWN
     
    
        )
        
