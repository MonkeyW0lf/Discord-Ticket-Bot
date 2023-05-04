import discord
from discord import app_commands
from discord.ext import commands
from discord.utils import get

import random
from datetime import datetime
import datetime

import os

import calendar
import time
ts = calendar.timegm(time.gmtime())

from config.config import status

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="$", intents=intents,
                   activity=discord.Game(name=status))

bot.remove_command('help')

from config.config import funfact
funFact = [funfact]


intents.message_content = True
intents.guilds = True
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@bot.event
async def on_ready():
    print("Bot running with:")
    print("Username: ", bot.user.name)
    print("User ID: ", bot.user.id)

    from cogs.ticket import SelectView
    bot.add_view(SelectView())

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            if filename[:-3] not in ["view"]:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print('Cogs loaded successfully')

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands(s)")
    except Exception as e:
        print(e)

            

from config.config import token
bot.run(token)
