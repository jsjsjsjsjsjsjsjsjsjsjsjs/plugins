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
async def asupan_cmd(client: Client, message: Message):
    m = await edit_or_reply.str(message, "`Tunggu Sebentar...`")
    await gather(
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
