from asyncio import gather
from random import choice

from pyrogram import Client, enums, filters
from pyrogram.types import Message
from userge import userge

@userge.on_cmd(
    "asupanx", about={
        'header': "Kegoblokan yang haqiqi",
        'description': "Kegoblokan yg haqiqi",
        'usage': "{tr}asupanx"})
async def asupanx(client: Client, message: Message):
    Asu = await edit_or_reply(message, "`Tunggu Sebentar...`")
    await gather(
        Asu.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupanx.video.file_id
                    async for asupanx in client.search_messages(
                        "tedeasupancache", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )
