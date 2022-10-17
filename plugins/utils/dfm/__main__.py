import aiohttp
import base64
from pyrogram import enums
from userge import userge, Message
import time, os, math, requests, re, json
import datetime as DT



@userge.on_cmd(
    "ssh_do", about={
        'header': "Create SSH Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}ssh_do [user]:[exp]:[pw]"})
async def _sshh(message: Message):
    replied = message.input_str
    if not replied:
        await message.err("```Isi user:pw:exp blok....```", del_in=5)
        return
    if ":" not in replied:
        await message.err("```Format harus user:pw:exp...```", del_in=5) 
        return
    if ":"":" not in replied:
        await message.err("```Format harus user:pw:exp...```", del_in=5) 
        return
    await message.edit("```Sedang membuat akun, tunggu...```")
    u = message.input_str.strip().split(':')[0]
    p = message.input_str.strip().split(':')[1]
    e = message.input_str.strip().split(':')[2]
    header = {"AUTH_KEY":"meki"}
    url = (
        f"http://128.199.227.220:6969/adduser/exp?user={u}&password={p}&exp={e}"
    )
    async with aiohttp.ClientSession() as requests:
        data = await requests.get(url, headers=header)
        x = await data.text()
    #status = x['status']
    if x != "success":
        await message.edit("Kebanyakn coli ente...!`")
        return
    today = DT.date.today()
    later = today + DT.timedelta(days=int(e))
    await message.edit(
        text=(f"**━━━━━━━━━━━━━━━━**\n"
              f"** ⟨ SSH Account ⟩** \n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**Username:** `{u}`\n"
              f"**Password:** `{p}`\n"
              f"**Domain:** `rkr0.autocf.site`\n"
              f"**Port SSL :** `222, 447`\n"
              f"**Port WS :** `80`\n"
              f"**Port WS SSL :** `443`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**PayLoad WS:**\n"
              f"**`GET / HTTP/1.1[crlf]Host: rkr0.autocf.site[crlf]Connection: Keep-Alive[crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**Exp Until:** `{later}`\n"
              f"**━━━━━━━━━━━━━━━━**\n"),
         
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.MARKDOWN
     
    )
