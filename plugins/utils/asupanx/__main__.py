from asyncio import *
import aiohttp
import base64
from pyrogram import enums
from userge import userge, Message
import time, os, math, requests, re, json
import datetime as DT
import requests as req
from pyrogram import Client, filters

from userge import userge, Message, filters


@userge.on_cmd("asupan", about="asupan")
async def asupan(client, message):
    yanto = await message.reply("🔎 `Search asupan...`")
    pop = message.from_user.first_name
    ah = message.from_user.id
    await message.reply_video(
        choice(
            [
                lol.video.file_id
                async for lol in client.search_messages(
                    "asupancilikbot", filter=enums.MessagesFilter.VIDEO
                )
            ]
        ),
        False,
        caption=f"Nih Kak [{pop}](tg://user?id={ah}) Asupannya 🥵"
    )

    await yanto.delete()
