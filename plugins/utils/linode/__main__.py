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
    "ssh_lin", about={
        'header': "Create SSH Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}ssh_lin [user]:[pw]:[exp]"})
async def ssh(msg: Message):
    """SSH account"""
    replied = msg.input_str 
    if not replied:
        await msg.err("```Isi user:exp blok....```", del_in=5)
        return
    if ":" not in replied:
        await msg.err("```Format harus user:pw:exp...```", del_in=5) 
        return
    await msg.edit("```Sedang membuat akun, tunggu...```")
    async with aiohttp.ClientSession() as req:
        u = replied.strip().split(':')[0]
        p = replied.strip().split(':')[1]
        e = replied.strip().split(':')[2]
        domain = f"z2z.dfmlta.me"
        param = f":6969/adduser/exp??user={u}&password={p}&exp={e}"
        url = ("http://"+domain+param)
        async with req.get(url, headers=header) as resp:
            if resp.status != "success":
            #return 
              today = DT.date.today()
              later = today + DT.timedelta(days=int(e))
              await msg.edit(
              text=(f"**━━━━━━━━━━━━━━━━**\n"
              f"** ⟨ SSH Account ⟩** \n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**Username:** `{u}`\n"
              f"**Password:** `{p}`\n"
              f"**Domain:** `{domain}`\n"
              f"**DNS Domain:** `{domain1}`\n"
              f"**Port SSL :** `222, 447`\n"
              f"**Port WS :** `80`\n"
              f"**Port WS SSL :** `443`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**PayLoad WS:**\n"
              f"**`GET / HTTP/1.1[crlf]Host: {domain}[crlf]Connection: Keep-Alive[crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**Exp Until:** `{later}`\n"
              f"**━━━━━━━━━━━━━━━━**\n"),
         
             disable_web_page_preview=True,
             parse_mode=enums.ParseMode.MARKDOWN
     
    
        )
        
@userge.on_cmd(
    "vmess_lin", about={
        'header': "Create VMESS Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}vmess_lin [user]:[exp]"})
async def vmess(msg: Message):
    """vmess account"""
    replied = msg.input_str 
    if not replied:
        await msg.err("```Isi user:exp blok....```", del_in=5)
        return
    if ":" not in replied:
        await msg.err("```Format harus user:exp...```", del_in=5) 
        return
    await msg.edit("```Sedang membuat akun, tunggu...```")
    async with aiohttp.ClientSession() as req:
        u = replied.strip().split(':')[0]
        p = replied.strip().split(':')[1]
        param = f":6969/create-vmess?user={u}&exp={p}"
        url = ("http://z2z.dfmlta.me"+param)
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
              await msg.edit(
        text=(f"**━━━━━━━━━━━━━━━━**\n"
                  f" **⟨ VMESS ⟩**\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f"**» Remarks :** `{u}`\n"
                  f"**» Domain :** `{domain}`\n"
                  f"**» UUID :** `{uuid}`\n"
                  f"**» Port TLS :** `{porttls}`\n"
                  f"**» Port HTTP :** `{porthttp}`\n"
                  f"**» Path :** `{path}`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f" **Vmess TLS link :**\n"
                  f"**» `{x[0]}`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f" **Vmess HTTP link :**\n"
                  f"**» `{x[1].strip()}`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f"** Expired :** `{later}`\n"
                  f"**━━━━━━━━━━━━━━━━**"),
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.MARKDOWN
        )
        
 @userge.on_cmd(
    "trojan_lin", about={
        'header': "Create TROJAN Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}trojan_lin [user]:[exp]"})
async def vmess(msg: Message):
    """TROJAN account"""
    replied = msg.input_str 
    if not replied:
        await msg.err("```Isi user:exp blok....```", del_in=5)
        return
    if ":" not in replied:
        await msg.err("```Format harus user:exp...```", del_in=5) 
        return
    await msg.edit("```Sedang membuat akun, tunggu...```")
    async with aiohttp.ClientSession() as req:
        u = replied.strip().split(':')[0]
        p = replied.strip().split(':')[1]
        param = f":6969/trojan-create1?user={u}&exp={p}"
        url = ("http://z2z.dfmlta.me"+param)
        async with req.get(url, headers=header) as resp:
            if resp.status != "error":
            #return 
              xx = await resp.text()
              x = xx.replace('[','').replace(']','').replace('"',
'').split(',')
            remarks = re.search("#(.*)",x[0]).group(1)
            domain = re.search("@(.*?):",x[0]).group(1)
            uuid = re.search("trojan://(.*?)@",x[0]).group(1)
        #port = re.search(domain+":(.*?)",x[0]).group(1)
            today = DT.date.today()
            later = today + DT.timedelta(days=int(p))
            await message.edit(
        text=(f"**━━━━━━━━━━━━━━━━**\n"
              f"** ⟨ Trojan-ws ⟩** \n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**Remarks:** `{u}`\n"
              f"**Domain:** `{domain}`\n"
              f"**UUID:** `{uuid}`\n"
              f"**Port:** `443`\n"
              f"**Network:** `ws/grpc`\n"
              f"**Path:** `/trojan-ws`\n"
              f"**ServiceName:** `trojan-grpc`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"** Trojan-ws URL:**\n"
              f" `{x[0]}`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"** Trojan-grpc URL:**\n"
              f" `{x[1]}`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**Exp Until:** `{later}`\n"
              f"**━━━━━━━━━━━━━━━━**\n"),
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.MARKDOWN
        )
        
