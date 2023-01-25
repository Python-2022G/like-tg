import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    MessageHandler,
    filters
)

TOKEN = os.environ['TOKEN']

likes = 0
dislikes = 0

keyboard = [
        ['👍', '👎']
    ]

def start(update: Update, context: CallbackContext):
    update.message.reply_html(text="<b>Assalomu alaylum!</b>\n\n<i>like botga xush kelibsiz!!</i>", \
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard))

def like(update: Update, context: CallbackContext):
    global likes
    likes += 1
    update.message.reply_html(text=f"<b>like:</b> {likes}\n<b>dislike:</b> {dislikes}", \
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard))


def dislike(update: Update, context: CallbackContext):
    global dislikes
    dislikes += 1
    update.message.reply_html(text=f"<b>like:</b> {likes}\n<b>dislike:</b> {dislikes}", \
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard))

def main():
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    dp.add_handler(handler=CommandHandler(command='start', callback=start))

    dp.add_handler(handler=MessageHandler(filters=filters.Filters.text('👍'), callback=like))
    dp.add_handler(handler=MessageHandler(filters=filters.Filters.text('👎'), callback=dislike))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()