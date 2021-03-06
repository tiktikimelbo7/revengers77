from telegram.ext import CommandHandler
from telegram import ParseMode

help_text = "*Ravager Bot Commands* \n" \
            "/start : Start the authorization flow for google drive access\n" \
            "/add\_drive : Set default drive either personal or shared drive through the menu\n" \
            "/download : Add download task\n" \
            "/upload : Upload content if a download fails by replying to the source message or upload multiple times\n"\
            "/abort : Abort an ongoing task\n" \
            "/admin\_interface : Admin interface access \(only available in private chat and for admins\)\n" \
            "/revoke : Revoke and delete your google account on the bot\n" \
            "/help : See all the commands"


class Help:
    def __init__(self):
        pass

    @staticmethod
    def help(update, context):
        update.message.reply_text(quote=True, text=help_text, parse_mode=ParseMode.MARKDOWN_V2)

    def help_handler(self):
        help_handler = CommandHandler("help", self.help)
        return help_handler
