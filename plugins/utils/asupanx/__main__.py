import aiohttp
import base64
from pyrogram import enums
from userge import userge, Message
import time, os, math, requests, re, json
import datetime as DT
import requests as req
from pyrogram import Client, filters

from userge import userge, Message, filters


# add filters handler
@userge.on_filters(("asupan", [".", "-", "^", "!", "?"]) & filters.me)  # filter my private messages
async def asupan(client: Client, message: Message):
    if message.chat.id == -1001554560763:
        return await edit_or_reply(message, "**This command is prohibited from being used in this group**")
    ram = await edit_or_reply(message, "`Wait a moment...`")
    await gather(
        ram.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "punyakenkan", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )
