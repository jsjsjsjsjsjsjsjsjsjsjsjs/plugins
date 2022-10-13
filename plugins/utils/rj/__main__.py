import aiohttp
import base64
from pyrogram import enums
from userge import userge, Message
import time, os, math, requests, re, json
import datetime as DT

HTTP_TIMEOUT = 10

class TimeoutRequestsSession(requests.Session):
    def request(self, *args, **kwargs):
        kwargs.setdefault('timeout', HTTP_TIMEOUT)
        return super(TimeoutRequestsSession, self).request(*args, **kwargs)

requests = TimeoutRequestsSession()
requests.headers.update({"AUTH_KEY":"meki"})

@userge.on_cmd(
    "vmess", about={
        'header': "Create VMESS Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}vmess [user]:[exp]"})
async def vmess(msg: Message):
    """vmess account"""
    replied = message.input_str 
    if not replied:
        await message.err("```Isi user:exp blok....```", del_in=5)
        return
    if ":" not in replied:
        await message.err("```Format harus user:exp...```", del_in=5) 
        return
    await message.edit("```Sedang membuat akun, tunggu...```")
    async with aiohttp.ClientSession() as ses:
        u = replied.strip().split(':')[0]
	p = replied.strip().split(':')[1]
        url = f"http://rajasa-v.bhm.my.id:6969/create-vmess?user={u}&exp={p}"
        async with ses.get(url) as resp:
            if resp.status != 200:
                return await msg.err("Unable to process your request")
            xx = await resp.text()
        if xx['status_code'] == 0:
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
            return await msg.err(dumps(xx['status_error']))
        out_str = (
            f"**━━━━━━━━━━━━━━━━**\n"
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
                  f"**━━━━━━━━━━━━━━━━**"
        )
        await msg.edit(out_str)
