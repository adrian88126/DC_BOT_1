import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix="[", intents=intents)
@bot.event
async def on_ready():
    print(">>bot online>>")
bot.run('MTEyOTc3NTI2NTI0NjA4OTM4OA.GWPxZf.cEBML0MW9jqgsWmjzvZkTAgFQTw5Q-UoGQqtL4')
