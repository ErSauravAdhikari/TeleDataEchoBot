import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def get_user_id(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Your User ID is: {update.effective_user.id}')


def get_full_json(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'{update}')


def get_start(update: Update, context: CallbackContext) -> None:
    reply_text = "/userid Reurns user's effective user id\n"
    reply_text += "/help [/start] Returns this message\n"
    reply_text += "/json Echo backs complete JSON that is recieved\n"
    reply_text += "\n\n"
    reply_text += "Hello, I am Saurav Adhikari. The Creator of this BOT.\n"
    reply_text += "How about you give me some stars and follows at github, it would definately help my vanity.\n"
    reply_text += "https://github.com/ersauravadhikari/\n🤣🤣🤣"
    
    update.message.reply_text(reply_text)


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
