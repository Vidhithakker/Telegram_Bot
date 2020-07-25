#Telegram app->search BotFather
#write /start
#then write /newbot
#Write some name eg:Vt_Bot or Vt123_bot
#You will get some token to access the HTTP API: copy and paste it bot=Bot("---")
from telegram.bot import Bot
from telegram.ext.updater  import Updater
from telegram.ext.dispatcher import Dispatcher
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.parsemode import ParseMode
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import wikipedia
bot=Bot("1178157321:AAGFgWg17vGqZLxTEpCkvkz9A1bduOmSsOQ")

print(bot.get_me())  #getting information of bot

updater=Updater("1178157321:AAGFgWg17vGqZLxTEpCkvkz9A1bduOmSsOQ",use_context=True)  #continous update telegram

dispatcher:Dispatcher=updater.dispatcher   #dispatch msg

keyword=' '
chat_id=' '

def show(update:Update,context:CallbackContext):
    global keyword,chat_id

    keyword=update.message.text
    chat_id=update.message.chat_id
    summary=wikipedia.summary(keyword)
    bot.send_message(
        chat_id=update.effective_chat.id,
        text=summary,
        parse_mode=ParseMode.HTML,
    )
updater.dispatcher.add_handler(MessageHandler(Filters.text,show))
updater.start_polling()

#when you run it and open telegram first and search that name you wrote as Vt123_bot or any u wrote
#write /start and than search whatever you want