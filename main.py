# CONFIG
token = "TOKEN_HERE" # Google how to get token if you don't have.
prefix = "~"

import asyncio
from discord.ext import commands
import discord
import random
import re

print("Loading bot..")

words = ['pog', 'message', 'sample', 'test', 'discord', 'minecraft', 'bot', 'mee6', 'poggr', 'poggers', 'troll', 'nootnoot', 'this is a message', 'give me free nitro', 'ignore me please', 'why are you reading this', 'made you look', 'hi', 'hello', 'this is another random message', 'this is a message with no context', 'this message serves no purpose', 'hi audit logs its me', 'its me', 'isnt this entertaining?', 'this message will self-destruct', 'this message will also self-destruct', 'this message will go poof', 'poof', 'my password is....', '#auditlog spam', 'dont mind me', 'this is a string', 'this is a bunch of garbage', 'this message is for mee6 levels', 'this message is for experience', '#freeexperience', 'xp', 'dont mind me... im collecting xp', 'just chilling', 'this is message number 999999999999999999999', 'm e s s a g e', 'hello, this is a message which wont last long', 'insert message here', 'insert creative quote here', 'insert useless message here', 'dont ask', 'no need to question', 'insert creative message here', 'typo', 'spam', 'this is not spam', 'give me nitro', 'look at me xp farming', 'this randomizer is cool', 'hello there', 'i see you', 'peek a boo', 'boo!']

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot Loaded!")

@bot.command()
async def farm(ctx, amount=10):
    await ctx.message.delete()
    print("Farming XP")
    for r in range(amount):
        message = await ctx.send(random.choice(words))
        await asyncio.sleep(random.uniform(1,5))
        await message.delete()
        await asyncio.sleep(random.uniform(61,65))
    print("Farm complete")

bot.run(token, bot=False) 
