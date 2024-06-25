import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from vova import sticker

TOKEN = "7340715564:AAESCXTxXPLtuM5X1GvVTtrwMksoijOLN7I"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message(Command("exit"))
async def echo_handler(message: Message) -> None:
    await message.answer(f"панцерфауст")
    await message.answer_sticker(sticker=sticker.hello)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())