from discord import activity
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
import cogs
import discord

load_dotenv()

bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
     print("Ready !")
     activiter = discord.Streaming(name="KellOog'S RP", url="https://twitch.tv/Weetoos")
     await bot.change_presence(activity=activiter)
     

bot.add_cog(cogs.spec(bot))
bot.add_cog(cogs.log(bot))
bot.run(getenv("TOKEN"))