import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# FFMPEG yo'li
FFMPEG_PATH = r"C:\Users\acer\Desktop\ffmpeg-7.1.1-essentials_build\bin"

# Bot tokeningiz
BOT_TOKEN = "8443293671:AAFJsd_nIyBlRy_mm-Lj79VCOJL2jX_noPo"

# Video yuklash funksiyasi
def download_video(url, output_path):
    ydl_opts = {
        'outtmpl': output_path,
        'ffmpeg_location': FFMPEG_PATH,
        'format': 'mp4',
        'noplaylist': True,
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Menga YouTube yoki Instagram linkini yuboring.")

# Foydalanuvchi link yuborganda
async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    chat_id = update.message.chat_id
    video_file = f"video_{chat_id}.mp4"

    try:
        await update.message.reply_text("📥 Video yuklanmoqda...")
        download_video(url, video_file)
        await update.message.reply_video(video=open(video_file, "rb"))
        os.remove(video_file)
    except Exception as e:
        await update.message.reply_text("⚠️ Xatolik: Video yuklab bo‘lmadi.")
        print(e)

# Asosiy bot ishga tushirish
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))

print("✅ Bot ishga tushdi...")
app.run_polling()
