import discord
import os
from discord.ext import commands
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix="[", intents=intents)
@bot.event
async def on_ready():
    print(">>bot online>>")
bot.run(os.environ['BOT_TOKEN'])
