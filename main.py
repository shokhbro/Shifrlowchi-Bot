import logging

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Salom {user.mention_html()}!. Menga xabarni yuboring va men shifrlab beraman.",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def foydalanish_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    await update.message.reply_text("Bu bot matnlarni kaliti 3ga teng bo'lgan shifr bilan almashtirib beradi.")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    kirit = update.message.text
    # print(kirit)

    saqla = ''  
    n = list()

    for i in kirit:
        if i == ' ':
            t = ord(i)
        else:
            t = ord(i) + 3
            if i in 'zZyYxX':
                t = (ord(i)-25)+3 
        saqla += chr(t)

    await update.message.reply_text(saqla)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6965442504:AAHQzbSjJ-09Sqz_ptexRdjGU-uhGw6mGwk").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("foydalanish", foydalanish_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()