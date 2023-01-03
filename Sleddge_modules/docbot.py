import discord 
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="D!", intents = intents)

@bot.event
async def on_ready():
    print("ready")

bot.run("MTAyMzcwMTk5MTU4MDUwNDA3NA.G6iadh.lV1sMDk1uILSrEnuJZsurWQz8Dbg3gNpdSZSOQ")