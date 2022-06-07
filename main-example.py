import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import time


bot = commands.Bot(command_prefix = '!') #using ! because it's the most popular, but you can use whatever works, like ?
bot.remove_command("help") #this is just here because it works for me, for some reason

load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN') #you'll need dotenv because you'll need this to be secret so nobody else can access your discord bot. install dotenv by using pip (pip install python-dotenv)

@bot.event
async def on_ready():
  print("Logged in as {0.user}".format(bot))
  await bot.change_presence(activity=discord.Activity
  (type=discord.ActivityType.listening, name= "Music")) #so it says listening to music in sidebar

#Hello! In case you don't know, to create a command do
#@bot.command()
#async def {command name}(ctx):
#	await ctx.send('Message')

@bot.command()
async def load(ctx, extension):
  bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')
  
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')
try:
    bot.run(TOKEN)
except discord.errors.LoginFailure as e:
        print("Login unsuccessful.")

#the unload and load cogs is so you can have files in the "cogs" folder, this is to not clog up your main.py file with random long winded commands.
#try and except is to show you an error message if login is unsuccessful rather than spit out an error and crash on you.