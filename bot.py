import hikari
import lightbulb
import os
from tts import tts_request
from dotenv import load_dotenv

# Load token from env
load_dotenv()

PREFIX = "bm"
TOKEN = os.getenv("TOKEN")

from const import PREFIX, TOKEN

bot = lightbulb.BotApp(token=TOKEN,
    default_enabled_guilds=(906827483150684180),
    intents=hikari.Intents.ALL,
    prefix=PREFIX
)

# @bot.listen(hikari.GuildMessageCreateEvent)
# async def print_msg(event):
#     msg = event.content
#     print(msg)
#     await tts_request(msg)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    bot.load_extensions_from("./extensions/", must_exist=True)
    print('Bot has started!')

@bot.command
@lightbulb.command(name='ping', description='Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

# No need to implement anything here since nothing will run
@bot.command
@lightbulb.command(name='group', description='Says group!')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

@my_group.child
@lightbulb.command('subcommand', 'This is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a subcommand!')

@bot.command
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.command('add', 'Add ttwo numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

bot.run()