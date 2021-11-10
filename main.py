from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
import cogs

load_dotenv()

bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
     print("Ready !")
     

bot.add_cog(cogs.spec(bot))
bot.add_cog(cogs.log(bot))
bot.run(getenv("TOKEN"))