import logging
from typing import Optional

import hikari
import lightbulb
import lavasnek_rs
import lavalink

# If True connect to voice with the hikari gateway instead of lavasnek_rs's
HIKARI_VOICE = True

from dotenv import load_dotenv
import os

# Load token from env
load_dotenv()

PREFIX = "bm"
TOKEN = os.getenv("TOKEN")
LAVALINK_PASSWORD = os.getenv("LAVALINK_PASSWORD")

plugin = lightbulb.Plugin("Music")

@plugin.listener(hikari.ShardReadyEvent)
async def start_lavalink(event: hikari.ShardReadyEvent) -> None:
    """Event that triggers when the hikari gateway is ready."""
    print("voice shard i am ready")
    

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_plugin(plugin)



