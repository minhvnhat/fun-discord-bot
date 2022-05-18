import hikari
import os
from dotenv import load_dotenv

# Load token from env
load_dotenv()
TOKEN = os.getenv("TOKEN")


bot = hikari.GatewayBot(token=TOKEN)

bot.run()