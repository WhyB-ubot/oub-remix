""" This trash plugin. """
import asyncio

from pyrogram.errors import FloodWait
from userge import userge, Message


@userge.on_cmd('copy',
  about={'header': "Copy message",
    'usage': "{tr}copy reply to message",
  },
)
async def msg_copy(message: Message):
    if message.reply_to_message:
      await message.delete()
      try:
        await message.reply_to_message.copy(message.reply_to_message.message_id)
      except FloodWait as e:
        await asyncio.sleep(e.x)
    else:
        await message.edit("reply to message hangs you want to copy")
        await message.delete(3)