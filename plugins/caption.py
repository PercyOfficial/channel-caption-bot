# Infinity Bots

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

@Client.on_message(filters.document & filters.channel)
async def caption(client, message: Message):
    await message.edit("@KdramaSearch_bot #Kdrama Uploaded By @Percy_jackson_4",
          reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Cortana Updates", url="https://t.me/Cortana_BOTS")]
            ]
                                           )
                      )
