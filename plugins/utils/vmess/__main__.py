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
    "vmess", about={
        'header': "Create VMESS Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}vmess [server]:[user]:[exp]"})
async def vmess(message: Message):
    """vmess account"""
    replied = message.input_str 
    if not replied:
        await message.edit("`JGN KOSONG BLOK!`")
        return
    elif ":" not in replied:
        await message.edit("`USER:EXP !`")
        return
    await message.edit("`Tunggu Blog !`")
    async with aiohttp.ClientSession() as req:
        s = replied.strip().split(':')[0]
        u = replied.strip().split(':')[1]
        p = replied.strip().split(':')[2]
        param = f":6969/create-vmess?user={u}&exp={p}"
        url = ("http://"+s+param)
        async with req.get(url, headers=header) as resp:
            if resp.status != "error":
            #return 
              xx = await resp.text()
       # if xx['status_code'] == 0:
              x = xx.replace("[","").replace("]","").replace("'",
"").split(",")
              z = base64.b64decode(x[0].replace("vmess://","")).decode("ascii")
              z = json.loads(z)
              z1 = base64.b64decode(x[1].replace("vmess://","")).decode("ascii")
              z1 = json.loads(z1)
              porttls = z['port']
              porthttp = z1['port']
              domain = z['add']
              uuid = z['id']
              path = z['path']
              today = DT.date.today()
              later = today + DT.timedelta(days=int(p))
              await message.edit(
        text=(f"**━━━━━━━━━━━━━━━━**\n"
                  f" ** ⚡️ VMESS ACCOUNT ⚡️️ **\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f"**🔰 Remarks :** `{u}`\n"
                  f"**🔰 Domain :** `{domain}`\n"
                  f"**🔰 UUID :** `{uuid}`\n"
                  f"**🔰 Port TLS :** `{porttls}`\n"
                  f"**🔰 Port HTTP :** `{porthttp}`\n"
                  f"**🔰 Path :** `isi apa aja bebas`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f" **Vmess TLS link :**\n"
                  f"**🔰 `{x[0]}`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f" **Vmess HTTP link :**\n"
                  f"**🔰 `{x[1].strip()}`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f" **Vmess GRPC link :**\n"
                  f"**🔰 `{x[2].strip()}`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f"** Expired :** `{later}`\n"
                  f"**━━━━━━━━━━━━━━━━**"),
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.MARKDOWN
        )
        
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
    "trialvm", about={
        'header': "Create VMESS Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}trialvm [server]"})
async def vmess(message: Message):
    """vmess account"""
    replied = message.input_str 
    if not replied:
        await message.edit("`JGN KOSONG BLOK!`")
        return
    #elif ":" not in replied:
        #await message.edit("`USER:EXP !`")
        #return
    await message.edit("`Tunggu Blog !`")
    async with aiohttp.ClientSession() as req:
        s = replied.strip().split(':')[0]
        param = f":6969/trial-vmess"
        url = ("http://"+s+param)
        async with req.get(url, headers=header) as resp:
            if resp.status != "error":
            #return 
              xx = await resp.text()
       # if xx['status_code'] == 0:
              x = xx.replace("[","").replace("]","").replace("'",
"").split(",")
              z = base64.b64decode(x[0].replace("vmess://","")).decode("ascii")
              z = json.loads(z)
              z1 = base64.b64decode(x[1].replace("vmess://","")).decode("ascii")
              z1 = json.loads(z1)
              remarks = z['ps']
              porttls = z['port']
              porthttp = z1['port']
              domain = z['add']
              uuid = z['id']
              path = z['path']
              today = DT.date.today()
              later = today + DT.timedelta(days=int(1))
              await message.edit(
        text=(f"**━━━━━━━━━━━━━━━━**\n"
                  f" ** ⚡️ TRIAL VMESS  ⚡️️ **\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f"**🔰 Remarks :** `{remarks}`\n"
                  f"**🔰 Domain :** `{domain}`\n"
                  f"**🔰 UUID :** `{uuid}`\n"
                  f"**🔰 Port TLS :** `{porttls}`\n"
                  f"**🔰 Port HTTP :** `{porthttp}`\n"
                  f"**🔰 Path :** `isi apa aja bebas`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f" **Vmess TLS link :**\n"
                  f"**🔰 `{x[0]}`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f" **Vmess HTTP link :**\n"
                  f"**🔰 `{x[1].strip()}`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f" **Vmess GRPC link :**\n"
                  f"**🔰 `{x[2].strip()}`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f"** Expired :** `{later}`\n"
                  f"**━━━━━━━━━━━━━━━━**"),
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.MARKDOWN
        )
        
@userge.on_cmd(
    "trojan", about={
        'header': "Create TROJAN Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}trojan [user]:[exp]"})
async def trojan(message: Message):
    """TROJAN account"""
    replied = message.input_str 
    if not replied:
        await message.edit("`JGN KOSONG BLOK!`")
        return
    elif ":" not in replied:
        await message.edit("`USER:EXP !`")
        return
    elif ":" and ":" not in replied:
        await message.edit("`DOMAIN:USER:EXP !`")
        return
    await message.edit("`Tunggu Blog !`")
    async with aiohttp.ClientSession() as req:
        d = replied.strip().split(':')[0]
        u = replied.strip().split(':')[1]
        p = replied.strip().split(':')[2]
        param = f":6969/trojan-create?user={u}&exp={p}"
        url = ("http://"+d+param)
        async with req.get(url, headers=header) as resp:
            if resp.status != "error":
            #return 
              xx = await resp.text()
              x = xx.replace("[","").replace("]","").replace("'",
"").split(",")
            #remarks = re.search("#(.*)",x[0]).group(1)
            domain = re.search("@(.*?):",x[0]).group(1)
            uuid = re.search("trojan://(.*?)@",x[0]).group(1)
        #port = re.search(domain+":(.*?)",x[0]).group(1)
            today = DT.date.today()
            later = today + DT.timedelta(days=int(p))
            await message.edit(
        text=(f"**━━━━━━━━━━━━━━━━**\n"
              f"** 🍂 Trojan-ws Account 🍂** \n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**🎋Remarks:** `{u}`\n"
              f"**🎋Domain:** `{domain}`\n"
              f"**🎋UUID:** `{uuid}`\n"
              f"**🎋Port:** `443`\n"
              f"**🎋Network:** `ws/grpc`\n"
              f"**🎋Path:** `/trojan`\n"
              f"**🎋ServiceName:** `trojan`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**🎋 Trojan-ws URL:**\n"
              f" `{x[0]}`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**🎋 Trojan-grpc URL:**\n"
              f" `{x[1]}`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**🎋Exp Until:** `{later}`\n"
              f"**━━━━━━━━━━━━━━━━**\n"),
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.MARKDOWN
        )
        
