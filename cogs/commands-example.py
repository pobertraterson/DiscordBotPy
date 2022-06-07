import os
import discord
from discord.ext import commands
import random

bot = bot = commands.Bot(command_prefix = '!') #using ! because it's the most popular

class Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['commands', 'command'])
    async def help(self, ctx):
#similar to spotify, but instead of doing spotify songs, do commands.

def setup(bot):
    bot.add_cog(Command(bot))

#you need to run this with main.py, starting the file by itself will not work and it will crash... same with the spotify file