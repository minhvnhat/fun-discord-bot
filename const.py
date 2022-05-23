from dotenv import load_dotenv
import os

# Load token from env
load_dotenv()

PREFIX = "bm"
TOKEN = os.getenv("TOKEN")
LAVALINK_PASSWORD = os.environ["LAVALINK_PASSWORD"]