# -*- coding: utf-8 -*-

import os
import re

from telegram.ext import Updater, CommandHandler
import logging

token = os.environ['5324727239:AAH5ptASwVr2pUc4L8xI8gPcjBYGBBjYL-g']
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    exp = update.message.text.replace('/calc', '')
    exp = "".join(exp.split())
    if re.match('^([-+]?([(]?[0-9][)]?[+-/*]?))*$', exp):
        try:
            update.message.reply_text(eval(exp))
        except:
            update.message.reply_text('Ooops error saat kalkulasi')
    else:
        update.message.reply_text('Pola salah')


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("calc", start))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()