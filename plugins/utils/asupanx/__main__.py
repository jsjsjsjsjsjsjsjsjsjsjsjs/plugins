import random


from userge import userge, Message
from pyrogram.tl.types import InputMessagesFilterVideo
from pyrogram.tl.types import InputMessagesFilterVoice
from pyrogram.tl.types import InputMessagesFilterPhotos


@userge.on_cmd(
    "asupan", about={
        'header': "Kegoblokan yang haqiqi",
        'description': "Kegoblokan yg haqiqi",
        'usage': "{tr}asupan"})
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@balabalabotbokep", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"Ini Asupannya Buat Kau [{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video orang colmek.")

