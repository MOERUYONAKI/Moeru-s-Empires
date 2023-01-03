import discord 
from discord.ext import commands
from token_foxy import *

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="D!", intents = intents)

@bot.event
async def on_ready():
    print("ready")

bot.run(str(token_f))