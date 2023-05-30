from pythonping import ping
from userge import userge, Message


@userge.on_cmd("cek", about="cek server ping")
async def ping(message: Message):
    replied = message.input_str 
    if not replied:
        await message.edit("`JGN KOSONG BLOK!`")
        return
    await message.edit("`Tunggu Blog !`")
    s = replied.strip().split(':')[0]
    i = ping('{s}', count=3) 
    if i.success:
         await message.edit(f" `{i}\n`")
    else:
          await message.edit(f" `Not Responds`")
     
