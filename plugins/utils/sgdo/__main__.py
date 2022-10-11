""" sgdo Plugin """


import aiohttp
import base64, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import enums
from userge import userge, Message
import time, os, math, requests, re, json
import datetime as DT



@userge.on_cmd(
    "ssh", about={
        'header': "Create Trojan Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}ssh [user]:[exp]:[pw]"})
async def _sshh(message: Message):
    await message.edit("`Please Wait Creating Account ...`")
    if not message.input_str:
        await message.edit("Input Data Frist!`")
        return
    u = message.input_str.strip().split(':')[0]
    p = message.input_str.strip().split(':')[1]
    e = message.input_str.strip().split(':')[2]
    url = (
        f"http://188.166.240.56:82/adduser/exp?user={u}&password={p}&exp={e}"
    )
    async with aiohttp.ClientSession() as requests:
        data = await requests.get(url)
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
              f"**DNS Domain:** `rkr0nsque.keongdns.my.id`\n"
              f"**Port SSL :** `222, 777`\n"
              f"**Port WS :** `2082`\n"
              f"**Port WS SSL :** `443`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**PayLoad WS:**\n"
              f"**`GET / HTTP/1.1[crlf]Host: rkr0.autocf.site[crlf]Connection: Keep-Alive[crlf]User-Agent: [ua][crlf]Upgrade: websocket[crlf][crlf]`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**Pub Key Slowlkeong:**\n"
              f"**`3016fc65960efef9d6c35aca680c10e478ad31b406c9a47eed44d955dcac2f27`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**Exp Until:** `{later}`\n"
              f"**━━━━━━━━━━━━━━━━**\n"),
         
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.MARKDOWN
        InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(text="👥 UsergeTeam", url="https://github.com/UsergeTeam"),
                    InlineKeyboardButton(text="🧪 Repo", url=botpm.UPSTREAM_REPO)
                ],
                [InlineKeyboardButton(text="🎖 GNU GPL v3.0", url=copy_)]
            ])
            await send_start_text(msg, text, path, markup)
    )




@userge.on_cmd(
    "trojan", about={
        'header': "Create Trojan Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}trojan [user]:[exp]"})
async def _ip_look_up(message: Message):
    await message.edit("`Please Wait Creating Account ...`")
    if not message.input_str:
        await message.edit("Input Data Frist!`")
        return
    u = message.input_str.strip().split(':')[0]
    p = message.input_str.strip().split(':')[1]
    url = (
        f"http://188.166.240.56:82/trojan-create?user={u}&exp={p}"
    )
    async with aiohttp.ClientSession() as requests:
        data = await requests.get(url)
        x = await data.text()
    #status = x['status']
    if x != "200":
        #await message.edit("`Aing Lieur Gays!`")
        #return
        domain = re.search("@(.*?):",x).group(1)
        port = re.search(domain+":(.*)",x).group(1)
        today = DT.date.today()
        later = today + DT.timedelta(days=int(p))
        await message.edit(
        text=(f"**━━━━━━━━━━━━━━━━**\n"
              f"** ⟨ Trojan ⟩** \n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**Remarks:** `{u}`\n"
              f"**Domain:** `{domain}`\n"
              f"**Port:** `{port}`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"** Trojan URL:**`{x}`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**Exp Until:** `{later}`\n"
              f"**━━━━━━━━━━━━━━━━**\n"),
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.MARKDOWN
    )

@userge.on_cmd(
    "trojanws", about={
        'header': "Create Trojanws Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}trojanws [user]:[exp]"})
async def _trojanws(message: Message):
    await message.edit("`Please Wait Creating Account ...`")
    if not message.input_str:
        await message.edit("Input Data Frist!`")
        return
    u = message.input_str.strip().split(':')[0]
    p = message.input_str.strip().split(':')[1]
    url = (
        f"http://188.166.240.56:82/trojan-create1?user={u}&exp={p}"
    )
    async with aiohttp.ClientSession() as requests:
        data = await requests.get(url)
        xx = await data.text()
    #status = x['status']
    if xx != "200":
        #await message.edit("`Aing Lieur Gays!`")
        #return
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

@userge.on_cmd(
    "trojango", about={
        'header': "Create Trojan-GO Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}trojango [user]:[exp]"})
async def _trojango(message: Message):
    await message.edit("`Please Wait Creating Account ...`")
    if not message.input_str:
        await message.edit("Input Data Frist!`")
        return
    u = message.input_str.strip().split(':')[0]
    p = message.input_str.strip().split(':')[1]
    url = (
        f"http://188.166.240.56:82/trojango-create?user={u}&exp={p}"
    )
    async with aiohttp.ClientSession() as requests:
        data = await requests.get(url)
        x = await data.text()
    #status = x['status']
    if x != "200":
        #await message.edit("`Aing Lieur Gays!`")
        #return
        domain = re.search("@(.*?):",x).group(1)
        port = re.search(domain+":(.*?)/",x).group(1)
        path = re.search("path=(.*?)&",x).group(1)
        today = DT.date.today()
        later = today + DT.timedelta(days=int(p))
        await message.edit(
        text=(f"**━━━━━━━━━━━━━━━━**\n"
              f"** ⟨ Trojan-GO ⟩** \n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**Remarks:** `{u}`\n"
              f"**Domain:** `{domain}`\n"
              f"**Port:** `{port}`\n"
              f"**Key:** `{u}`\n"
              f"**Path:** `{path}`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"** Trojan-GO URL:**\n"
              f" `{x}`\n"
              f"**━━━━━━━━━━━━━━━━**\n"
              f"**Exp Until:** `{later}`\n"
              f"**━━━━━━━━━━━━━━━━**\n"),
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.MARKDOWN
    )

@userge.on_cmd(
    "vmess1", about={
        'header': "Create VMESS Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}vmess1 [user]:[exp]"})
async def _vmess1(message: Message):
    await message.edit("`Please Wait Creating Account ...`")
    if not message.input_str:
        await message.edit("Input Data Frist!`")
        return
    u = message.input_str.strip().split(':')[0]
    p = message.input_str.strip().split(':')[1]
    url = (
        f"http://188.166.240.56:82/create-vmess1?user={u}&exp={p}"
    )
    async with aiohttp.ClientSession() as requests:
        data = await requests.get(url)
        xx = await data.text()
    #status = x['status']
    if xx != "200":
        #await message.edit("`Aing Lieur Gays!`")
        #return
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
                  f" **⟨ VMESS ⟩**\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f"**» Remarks :** `{u}`\n"
                  f"**» Domain :** `{domain}`\n"
                  f"**» UUID :** `{uuid}`\n"
                  f"**» Port TLS/GRPC :** `{porttls}`\n"
                  f"**» Port HTTP :** `{porthttp}`\n"
                  f"**» Path :** `{path}`\n"
                  f"**» ServiceName :** `vmess-grpc`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f" **Vmess TLS link :**\n"
                  f"**» `{x[0]}`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f" **Vmess HTTP link :**\n"
                  f"**» `{x[1].strip()}`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f" **Vmess GRPC link :**\n"
                  f"**» `{x[2].strip()}`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f"** Expired :** `{later}`\n"
                  f"**━━━━━━━━━━━━━━━━**"),
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.MARKDOWN
    )

@userge.on_cmd(
    "vless", about={
        'header': "Create VLESS Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}vless [user]:[exp]"})
async def _vless(message: Message):
    await message.edit("`Please Wait Creating Account ...`")
    if not message.input_str:
        await message.edit("Input Data Frist!`")
        return
    u = message.input_str.strip().split(':')[0]
    p = message.input_str.strip().split(':')[1]
    url = (
        f"http://188.166.240.56:82/create-vless?user={u}&exp={p}"
    )
    async with aiohttp.ClientSession() as requests:
        data = await requests.get(url)
        xx = await data.text()
    #status = x['status']
    if xx != "200":
        #await message.edit("`Aing Lieur Gays!`")
        #return
        x = xx.replace("[","").replace("]","").replace("'",
"").split(",")
        remarks = re.search("#(.*)",x[0]).group(1)
        domain = re.search("@(.*?):",x[0]).group(1)
        uuid = re.search("vless://(.*?)@",x[0]).group(1)
        porttls = re.search(f"{domain}:(.*?)?path",x[0]).group(1)
        porthttp = re.search(f"{domain}:(.*?)?path",x[1]).group(1)
        path = re.search("path=(.*)&",x[0]).group(1)
        today = DT.date.today()
        later = today + DT.timedelta(days=int(p))
        await message.edit(
        text=(f"**━━━━━━━━━━━━━━━━**\n"
                  f" **⟨ VLESS ⟩**\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f"**» Remarks:** `{remarks}`\n"
                  f"**» Domain:** `{domain}`\n"
                  f"**» Port TLS:** `2084`\n"
                  f"**» Port HTTP:** `8880`\n"
                  f"**» UUID:** `{uuid}`\n"
                  f"**» Encryption:** `none`\n"
                  f"**» NetWork:** `Websocket` `(WS)`\n"
                  f"**» Path:** `/v2ray`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f"**» TLS VLESS Url:**\n"
                  f"      `{x[0]}`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f"**» HTTP VLESS Url:**\n"
                  f"      `{x[1]}`\n"
                  f"**━━━━━━━━━━━━━━━━**\n"
                  f"**Expired Until:** `{later}`\n"
                  f"**━━━━━━━━━━━━━━━━**"),
        disable_web_page_preview=True,
        parse_mode=enums.ParseMode.MARKDOWN
    )
          
@userge.on_cmd(
    "vmess", about={
        'header': "Create VMESS Account",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}vmess [user]:[exp]"})
async def _vmess(message: Message):
    await message.edit("`Please Wait Creating Account ...`")
    if not message.input_str:
        await message.edit("Input Data Frist!`")
        return
    u = message.input_str.strip().split(':')[0]
    p = message.input_str.strip().split(':')[1]
    url = (
        f"http://188.166.240.56:82/create-vmess?user={u}&exp={p}"
    )
    async with aiohttp.ClientSession() as requests:
        data = await requests.get(url)
        xx = await data.text()
    #status = x['status']
    if xx != "200":
        #await message.edit("`Aing Lieur Gays!`")
        #return
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
          
