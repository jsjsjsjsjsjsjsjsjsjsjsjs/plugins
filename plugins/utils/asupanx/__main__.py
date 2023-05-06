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
    "asupan", about={
        'header': "Sangat GABUT",
        'description': "kegabutan yg haqiqi",
        'usage': "{tr}asupan"})
async def asupan_cmd(client: Message):
    m = await message.edit("`Tunggu Sebentar...`")
    await message.edit(
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "tedeasupancache", filter="video"
                    )
                ]
            ),
        ),
        m.delete(),
    )
