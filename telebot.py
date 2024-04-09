from typing import Final
from telegram import Update
from telegram.ext import CommandHandler, Updater, MessageHandler,filters
import requests
from pytube import YouTube

TOKEN :Final = '6982432240:AAGohongzRMIvf8YVVa1Zirfi8HZ2aNEDEk'
BOT_USERNAME : Final = '@lalith_saver_bot'

#Commands
async def start_command(update : Update, context ):
    await update.message.reply_text("Hello !\n This is Lalith's Bot !!\n Enjoy downloading!!!")


async def help_command(update : Update, context ):
    await update.message.reply_text("Paste any valid link to download media content :)")

    
#Responses
def handle_respnse(text : str) ->str:
    processed : str= text.lower()

    if 'youtu' in processed:
        yt=YouTube(text)
        ys=yt.streams.get_highest_resolution()
        return ys.url
    
def download_media(update: Update, context):
    url = update.message.text
    response = handle_response(url)
    update.message.reply_text(response)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_media))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

 