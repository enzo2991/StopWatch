from typing import Counter
from discord.ext.commands.errors import CommandInvokeError
import discord
from discord.ext import commands
import datetime
import function
import asyncio

class spec(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def spec(self,ctx):
        user = ctx.author
        start_time = datetime.datetime.now()
        await ctx.message.add_reaction("❌")
        def check(reaction, user):
            return user == ctx.author and (str(reaction.emoji) in "❌")
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=64800 , check=check) 
        except asyncio.TimeoutError:
            await ctx.message.delete()
            await ctx.send(f'<@{ctx.author.id}>, tu dors ?', delete_after=20)
        else:
            end_time = datetime.datetime.now()
            duration  = end_time - start_time
            duration_in_s = duration.total_seconds()
            convert = function.convert_seconds(duration_in_s)
            await ctx.message.delete()
            info = discord.Embed(title=user, color=0x318bdb)
            info.add_field(name="Debut du spec:",value=start_time)
            info.add_field(name="Fin du spec:",value=end_time)
            info.add_field(name="Durée:",value=convert)
            await ctx.send(embed=info)
