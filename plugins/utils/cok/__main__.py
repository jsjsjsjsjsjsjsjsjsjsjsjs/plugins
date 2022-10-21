import time
from pyrogram.errors.exceptions.bad_request_400 import YouBlockedUser
from userge import userge, Message
from userge.utils.exceptions import StopConversation


#gen
@userge.on_cmd("tes", about={
	'header': "tes",
	'usage': "{tr}tes [Enter bin]\n"})
	
async def gen(message: Message):
	"""Untuk gen cc"""
	replied = message.input_str
	chat = "@ajunvpnBot"
	await message.edit("```Wait for result... ```")
	msgs = []
	ERROR_MSG = "Unblok bot @binwatcher_bot untuk menggunakan command ini"
	try:
		async with userge.conversation(chat) as conv:
			try:
				await conv.send_message("/menu {}".format(replied))
			except YouBlockedUser:
				await message.err(f"**{ERROR_MSG}**", del_in=5)
				return 
			msgs = await conv.get_response(timeout=30, mark_read=True)
			if "Wait" in msgs.text:
				time.sleep(1)
				msgs = await conv.get_response(timeout=30, mark_read=True) 
				if "Wait" in msgs.text:
					time.sleep(1)
					msgs = await conv.get_response(timeout=30, mark_read=True) 
					if "Wait" in msgs.text:
						time.sleep(1)
						msgs = await conv.get_response(timeout=30, mark_read=True) 
						if "Wait" in msgs.text:
							time.sleep(1)
							msgs = await conv.get_response(timeout=30, mark_read=True)
							if "Wait" in msgs.text:
								time.sleep(1)
								msgs = await conv.get_response(timeout=30, mark_read=True)
								if "Wait" in msgs.text:
									time.sleep(1)
									msgs = await conv.get_response(timeout=30, mark_read=True)
									if "Wait" in msgs.text:
										time.sleep(1)
										msgs = await conv.get_response(timeout=30, mark_read=True)
										if "Wait" in msgs.text:
											time.sleep(1)
											msgs = await conv.get_response(timeout=30, mark_read=True)
											if "Wait" in msgs.text:
												time.sleep(1)
												msgs = await conv.get_response(timeout=30, mark_read=True)
												if "Wait" in msgs.text:
													time.sleep(1)
													msgs = await conv.get_response(timeout=30, mark_read=True)
													if "Wait" in msgs.text:
														time.sleep(1)
														msgs = await conv.get_response(timeout=30, mark_read=True) 
														if "Wait" in msgs.text:
															time.sleep(1)
															msgs = await conv.get_response(timeout=30, mark_read=True)  
															if "Wait" in msgs.text:
																time.sleep(1)
																msgs = await conv.get_response(timeout=30, mark_read=True)  
																if "Wait" in msgs.text:
																	time.sleep(1)
																	msgs = await conv.get_response(timeout=30, mark_read=True) 
																	if "Wait" in msgs.text:
																		time.sleep(1)
																		msgs = await conv.get_response(timeout=30, mark_read=True) 
																		if "Wait" in msgs.text:
																			time.sleep(1)
																			msgs = await conv.get_response(timeout=30, mark_read=True) 
																			if "Wait" in msgs.text:
																				time.sleep(1)
																				msgs = await conv.get_response(timeout=30, mark_read=True) 
																				if "Wait" in msgs.text:
																					time.sleep(1)
																					msgs = await conv.get_response(timeout=30, mark_read=True) 
																					if "Wait" in msgs.text:
																						time.sleep(1)
																						msgs = await conv.get_response(timeout=30, mark_read=True) 
																						if "Wait" in msgs.text:
																							time.sleep(1)
																							msgs = await conv.get_response(timeout=30, mark_read=True) 
	except StopConversation:
		pass 
	try:
		await message.edit(f"{msgs.text}")
	except AttributeError:
		await message.edit(f"`Bot tidak merespon!`", del_in=5)
