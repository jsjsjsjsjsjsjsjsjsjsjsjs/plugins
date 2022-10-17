# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge-Assistant > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Userge-Assistant/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import (
    Message, InlineKeyboardMarkup, InlineKeyboardButton)
from userge import userge


@userge.on_message(filters.command("tepo") & filters.me)
async def _rules(_, message: Message):
    replied = message.reply_to_message
    if replied:
        msg_id = replied.message_id
    else:
        msg_id = message.message_id
    markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Official Channel",
                    url="https://t.me/TheUserGe"),
                InlineKeyboardButton(
                    text="Unofficial Help",
                    url="https://t.me/UnofficialPluginsHelp")
            ],
            [
                InlineKeyboardButton(
                    text="Main Repo",
                    url="https://github.com/UsergeTeam/UserGe"),
                InlineKeyboardButton(
                    text="Plugins Repo",
                    url="https://github.com/UsergeTeam/Userge-Plugins")
            ],
            [
                InlineKeyboardButton(
                    text="Tutorial",
                    url="https://t.me/usergeot/612003")
            ]
        ]
    )
    await userge.send_message(message.chat.id,
                           text=("**Welcome**\n"
                                 "__Check out our channels and Repo's 🤘__"),
                           reply_to_message_id=msg_id,
                           reply_markup=markup)
