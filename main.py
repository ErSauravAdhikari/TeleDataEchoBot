import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def get_user_id(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Your User ID is: {update.effective_user.id}')


def get_full_json(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'{update}')


def get_start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"""
/userid Reurns user's effective user id
/help [/start] Returns this message
/json Echo backs complete JSON that is recieved

Hello, I am Saurav Adhikari. The Creator of this BOT.
How about you give me some stars and follows at github, it would definately help my vanity. 
    
https://github.com/ersauravadhikari/

🤣🤣🤣
    """)


def main():
    TELEGRAM_API = os.environ.get("TELEDATAECHOBOT_API_TOKEN")
    updater = Updater(TELEGRAM_API)
    updater.dispatcher.add_handler(CommandHandler('userid', get_user_id))
    updater.dispatcher.add_handler(CommandHandler('json', get_full_json))
    updater.dispatcher.add_handler(CommandHandler('start', get_start))
    updater.dispatcher.add_handler(CommandHandler('help', get_start))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
