import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    MessageHandler,
    filters
)
from db import DB

TOKEN = os.environ['TOKEN']

keyboard = [
    ['👍', '👎']
]
db = DB()

def start(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    db.add_user(user_id=str(user_id))
    update.message.reply_html(text="<b>Assalomu alaylum!</b>\n\n<i>like botga xush kelibsiz!!</i>", \
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))

def like(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    db.increase_like(user_id=str(user_id))
    data = db.get_likes(user_id=str(user_id))
    update.message.reply_html(text=f"<b>like:</b> {data['like']}\n<b>dislike:</b> {data['dislike']}", \
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))


def dislike(update: Update, context: CallbackContext):
    user_id = update.message.chat.id
    db.increase_dislike(user_id=str(user_id))
    data = db.get_likes(user_id=str(user_id))
    update.message.reply_html(text=f"<b>like:</b> {data['like']}\n<b>dislike:</b> {data['dislike']}", \
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))


def default(update: Update, context: CallbackContext):
    update.message.reply_html(text="iltimos buttonlardan birini bosing!", \
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True))

def main():
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    dp.add_handler(handler=CommandHandler(command='start', callback=start))

    dp.add_handler(handler=MessageHandler(filters=filters.Filters.text('👍'), callback=like))
    dp.add_handler(handler=MessageHandler(filters=filters.Filters.text('👎'), callback=dislike))

    dp.add_handler(handler=MessageHandler(filters=filters.Filters.all, callback=default))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()