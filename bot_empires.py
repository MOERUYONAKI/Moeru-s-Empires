# - - - - - - - - - - - - - E M P I R E S - - - - - - - - - - - - -


# - - - - - I M P O R T S - - - - -


import discord.__main__ as discord
from random import *
from Moeru_modules.kingdoms import *
from Moeru_modules.empire import Moerus_kd
from discord.__main__ import *
from discord.ext import commands
from discord.ext.commands.bot import Bot
from discord.ext.commands import has_permissions


# - - - - - S C R I P T _ P R I N C I P A L - - - - -


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = '!', description = 'kingdoms maker', intents = intents)

empires = {}

# - - - - - - - - - - - - - - - - - - - - 

@bot.command(name = 'new_empire')
async def emp_create(ctx, * , names : str):
    if ctx.message.author.name not in empires.keys():
        empires[ctx.message.author.name] = Kingdom(name = names, cities = [])
        print(f'{ctx.message.author.name} crée un empire')
        await ctx.send(embed = discord.Embed(title = 'Nouvel empire', description = f'Vous venez de créer votre empire au nom de **{names}** !', color=0x00ffff))

    else:
        await ctx.send(f'Vous possédez déjà un empire')

@bot.command(name = 'new_city')
async def city_create(ctx, * , names : str):
    if ctx.message.author.name in empires.keys():
        empires[ctx.message.author.name].add_city(City(names))

        print(f'{ctx.message.author.name} crée une ville')
        await ctx.send(embed = discord.Embed(title = 'Nouvelle ville', description = f'Vous venez de créer une ville au nom de **{names}** !', color=0x00ffff))

    else:
        await ctx.send(f"Vous ne possédez pas d'empire")

@bot.command(name = 'show_empire')
async def empire_view(ctx, member : discord.Member = None):
    if member == None:
        if ctx.message.author.name in empires.keys():
            await ctx.send(embed = discord.Embed(title = f"{ctx.message.author.name}'s kingdom", description = f'{empires[ctx.message.author.name].show_cities()}', color=0x00ffff))

        else:
            await ctx.send(f"Vous ne possédez pas d'empire")
            
    else:
        if member.name in empires.keys():
            await ctx.send(embed = discord.Embed(title = f"{member.name}'s empire", description = f'{empires[member.name].show_cities()}', color=0x00ffff))

        else:
            await ctx.send(f"Cet utilisateur ne possède pas d'empire")

@bot.command(name = 'lvl_upgrade')
async def up_city(ctx, * , name : str):
    if ctx.message.author.name in empires.keys():
        for city in empires[ctx.message.author.name].cities:
            if name == city.c_name:
                if empires[ctx.message.author.name].gold >= city.upgrade_price():
                    empires[ctx.message.author.name].gold -= city.upgrade_price()
                    city.add_lvl()
                    await ctx.send(embed = discord.Embed(title = f"{ctx.message.author.name}'s empire", description = f"La ville {name} a été améliorée d'un niveau !", color=0x00ffff))

                else:
                    await ctx.send("Vous n'avez pas assez d'or pour améliorer cette ville")

    else:
        await ctx.send("Vous ne possédez pas d'empire")

@bot.command(name = 'rank_upgrade')
async def up_city(ctx, * , name : str):
    if ctx.message.author.name in empires.keys():
        for city in empires[ctx.message.author.name].cities:
            if name == city.c_name:
                city.rank_upgrade()
                await ctx.send(embed = discord.Embed(title = f"{ctx.message.author.name}'s empire", description = f"Le rang de la ville {name} vient d'augmenter !", color=0x00ffff))

    else:
        await ctx.send("Vous ne possédez pas d'empire")

@bot.command(name = 'show_inventory')
async def gold_and_troops(ctx):
    if ctx.message.author.name in empires.keys():
        await ctx.send(embed = discord.Embed(title = f"{ctx.message.author.name}'s empire", description = empires[ctx.message.author.name].inventory(), color=0x00ffff))

    else:
        await ctx.send(f"Vous ne possédez pas d'empire")  


# - - - - - - - - - - - - - - - - - - - - 

@bot.event
async def on_ready() :
    activity = discord.Game(name = "la guerre !")
    await bot.change_presence(status = discord.Status.idle, activity = activity)
    print('Le bot est prêt !')
    print(round(bot.latency * 1000), "ms")


# - Sécurisation du Token -
try:
    token = open("C:\\Users\\1bbor\\OneDrive\\Documents\\GitHub\\Tokens.txt", 'r')
    
except:
    try:
        token = open("C:\\Users\\lduma\\Desktop\\developement\\dev\\Tokens.txt", 'r')
        
    except:
        token = open("C:\DocBot\Tokens.txt", 'r')
    
TOKEN = token.readline()
bot.run(TOKEN)
token.close()