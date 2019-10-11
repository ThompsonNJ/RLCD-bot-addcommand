import discord
import steam
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import sqlite3

bot = discord.Client()


@bot.event
async def on_ready():
    print("Online")


@bot.event
async def on_message(message):
    if message.content.lower().startswith('!add'):
        print('hello')
        api = steam.WebAPI("C136679DFD24DD703C2BBAE308FD4F25")
        steam_name = message.content.strip("!add ")
        steamID = api.ISteamUser.ResolveVanityURL(vanityurl="alrounder80")#!a.format(steam_name)) #hard code this for now
        steamID = steamID['response']
        steamID = steamID['steamid']
        print(steamID)
        await bot.send_message(message.channel, "steam://url/SteamIDPage/{}".format(steamID))


bot.run(TOKEN)
