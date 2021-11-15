from discord import activity
from discord.ext import commands
from discord.flags import Intents
from dotenv import load_dotenv
from os import getenv
import cogs
import discord

load_dotenv()

intents = discord.Intents.default()
intents.emojis = True

bot = commands.Bot(command_prefix=".", Intents=intents)

@bot.event
async def on_ready():
     print("Ready !")
     activiter = discord.Streaming(name="KellOog'S RP", url="https://twitch.tv/Weetoos")
     await bot.change_presence(activity=activiter)

bot.add_cog(cogs.spec(bot))
bot.add_cog(cogs.log(bot))
bot.add_cog(cogs.erreur(bot))
bot.run(getenv("TOKEN"))