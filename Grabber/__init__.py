import logging  

from pyrogram import Client 

from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

OWNER_ID = 6257270528
sudo_users = ["6257270528", "6257270528"]
GROUP_ID = -1002082803552
TOKEN = "7051461986:AAHOAv-SN8-UQzWwEUrjS98Jmxrim1gDB0k"
mongo_url = "mongodb+srv://te3:te23@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority"
PHOTO_URL = ["https://telegra.ph/file/72ea883532b722f405059.jpg", "https://telegra.ph/file/72ea883532b722f405059.jpg"]
SUPPORT_CHAT = "MUSIC_CHAT_GRP"
UPDATE_CHAT = "MUSIC_CHAT_GRP"
BOT_USERNAME = "Fancy_Waifu_Husbando_Bot"
CHARA_CHANNEL_ID = -1002082803552
api_id = 22792918
api_hash = "ff10095d2bb96d43d6eb7a7d9fc85f81"


application = Application.builder().token(TOKEN).build()
Grabberu = Client("Grabber", api_id, api_hash, bot_token=TOKEN)
client = AsyncIOMotorClient(mongo_url)
db = client['Character_catcher']
collection = db['anime_characters']
user_totals_collection = db['user_totals']
user_collection = db["user_collection"]
group_user_totals_collection = db['group_user_total']
top_global_groups_collection = db['top_global_groups']



