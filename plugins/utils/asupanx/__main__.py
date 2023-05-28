from random import choice
from pyrogram import Client, filters, enums

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
        caption=f"Nih Kak [{pop}](tg://user?id={ah}) Asupannya 🥵",
    )

    await yanto.delete()
