import discord.__main__ as discord
from discord.__main__ import *
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands import has_permissions

#test

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = "!", description="description", intents = intents)

@bot.event
async def on_ready():
    print("Le bot est en ligne")

@bot.event
async def on_message(message):
    if message.content.lower() =="ping":
        await message.channel.send("pong")
        latency =round(bot.latency * 1000)
        await message.channel.send(f"{latency} ms")
        
        

@bot.command(name="clear")
async def delete(ctx, number_of_message: int):
    print("test")
    said = await ctx.channel.history(limit=number_of_message + 1).flatten()
    for each_message in said:
        print(each_message)
        await each_message.delete()


token = open("C:\\Users\\lduma\\Desktop\\developement\\dev_py\\Xantokens.txt", 'r')
TOKEN = token.readline()
bot.run(TOKEN)
token.close()