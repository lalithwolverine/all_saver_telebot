from typing import Final
from telegram import Update
from telegram.ext import CommandHandler, Application, MessageHandler,filters,ContextTypes
import requests
from pytube import YouTube

# TOKEN :Final = '6982432240:AAGohongzRMIvf8YVVa1Zirfi8HZ2aNEDEk'
# BOT_USERNAME : Final = '@lalith_saver_bot'

# #Commands
# async def start_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Hello !\n This is Lalith's Bot !!\n Enjoy downloading!!!")


# async def help_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Paste any valid link to download media content :)")

    
# #Responses
# def handle_respnse(text : str) ->str:
#     processed : str= text.lower()

#     if 'Hello' in processed:
#         return ''

link=input("Enter youtbe link: ")
yt=YouTube(link)
print(yt.streams.filter(only_audio=True))
print(yt.streams.filter(only_video=True))