from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

# Token bot dari BotFather
BOT_TOKEN = "7919276002:AAEZ3WC3xDthbP_4b4CL35HhEJWUCFaHibM"  # Ganti dengan token bot Anda
CHANNEL_ID = -1002249850387  # Ganti dengan ID channel tujuan

# Inisialisasi bot dan dispatcher
bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

# Command /start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply(
        "Halo! Kirimkan pesan anonimmu di sini. Pesanmu akan diteruskan ke channel tujuan.\n\n"
        "⚠️ Jangan kirimkan informasi pribadi atau pesan yang melanggar aturan!"
    )

# Menangani semua pesan teks
@dp.message_handler(content_types=["text"])
async def forward_to_channel(message: types.Message):
    try:
        # Kirim pesan ke channel
        await bot.send_message(
            CHANNEL_ID,
            f"📢 <b>Pengakuan Anonim:</b>\n\n{message.text}"
        )
        # Balas ke pengguna bahwa pesan berhasil dikirim
        await message.reply("Pesanmu telah dikirim secara anonim!")
    except Exception as e:
        await message.reply(f"Terjadi kesalahan: {str(e)}")

# Menjalankan bot
if __name__ == "__main__":
    print("Menfes Bot sedang berjalan...")
    executor.start_polling(dp, skip_updates=True)
