from tcping import Ping
from userge import userge, Message


@userge.on_cmd("cek", about="cek server ping")
async def ping(message: Message):
    replied = message.input_str 
    if not replied:
        await message.edit("`JGN KOSONG BLOK!`")
        return
    await message.edit("`Tunggu Blog !`")
    s = replied.strip().split(':')[0]
    z = ping.ping(3)
    if len(list(z)) == 3:
         await message.edit(f" `{z}\n`")
    else:
          await message.edit(f" `Not Responds`")
     
