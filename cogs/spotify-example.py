import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix = '!') 

class Command(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

    #If you'd like to do something like this, you'll have to use Spotify. For now.
    #Also, when using a cog command like this, you HAVE to put "async def spotify(self, ctx):, otherwise it will not work.
  
  @commands.command(aliases=['songs'])
  async def spotify(self, ctx):
    x=random.randint(1,{whatever number you want})
#here, do await ctx.send('{spotify song link}')
		
def setup(bot):
    bot.add_cog(Command(bot))