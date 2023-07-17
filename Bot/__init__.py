import os, sys, logging
from pyrogram import Client 


#<-----------LOGGING------------>
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger("Bot by @soheru")
LOG.setLevel(level=logging.INFO)
#<-----------Variables-------------->
LOG.info('❤️ Checking Bot Variables.....')
TRIGGERS = os.environ.get("TRIGGERS", "/ !").split(" ")
BOT_TOKEN = os.environ.get('BOT_TOKEN', 'your bot token') #BOT Token Add
API_ID = int(os.environ.get('API_ID', 456789)) #Telgram Api id
APP_HASH = os.environ.get('APP_HASH', 'your api id')# Telgram App hash  
OWNER_ID = os.environ.get('OWNER_ID', 5669981425)
MONGO_DB = os.environ.get("MONGO_DB", 'your mongodb') #MONGO DB FOR ANIME DATA
FILES_CHANNEL = os.environ.get("FILES_CHANNEL", -100456789013)
BOT_NAME = os.environ.get('BOT_NAME', 'Soheru')
#<---------------Connecting-------------->
if BOT_TOKEN is not None:
    try:
        encoder  = Client('AutoEncoder', api_id=API_ID, api_hash=APP_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
        LOG.info('❤️ Bot Connected Created By Github @soheru || Telegram @sohailkhan_indianime ')
    except Exception as e:
        LOG.warn(f'😞 Error While Connecting To Bot\nCheck Errors: {e}')
        sys.exit()       
