from typing import Counter
from discord.ext.commands.errors import CommandInvokeError
import discord
from discord.ext import commands
import datetime
import function
import asyncio
from discord.utils import get

timereturn = "%d/%m/%Y %H:%M"
datereturn = "%d/%m/%Y %H:%M:%S"

def logs_spec(ctx,start_time,end_time,duree):
    log = "|" + str(start_time.strftime(timereturn) + "|\n" + f'Auteur : {ctx.author}\n Fin du spec: {end_time.strftime(timereturn)}\n Durée: {duree}\n__________________________________________\n') 
    with open('logs_spec.txt','a') as f:
        f.write(log)
    return logs_spec

def logs_spec_timeout(ctx,start_time):
    log = "|" + str(start_time.strftime(timereturn) + "|\n" + f'Auteur : {ctx.author}\n Fin du spec: TimeOut\n Durée: TimeOut\n__________________________________________\n') 
    with open('logs_spec.txt','a') as f:
        f.write(log)
    return logs_spec_timeout

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
            reaction, user = await self.bot.wait_for('reaction_add', timeout=10 , check=check)
        except asyncio.TimeoutError:
            await ctx.message.delete()
            await ctx.send(f'<@{ctx.author.id}>, tu dors ?', delete_after=20)
            logs_spec_timeout(ctx,start_time)
        else:
            end_time = datetime.datetime.now()
            duration  = end_time - start_time
            duration_in_s = duration.total_seconds()
            convert = function.convert_seconds(duration_in_s)
            logs_spec(ctx,start_time,end_time,convert)
            await ctx.message.delete()
            info = discord.Embed(title=user, color=0x318bdb)
            info.add_field(name="Debut du spec:",value=start_time.strftime(datereturn))
            info.add_field(name="Fin du spec:",value=end_time.strftime(datereturn))
            info.add_field(name="Durée:",value=convert)
            await ctx.send(embed=info,delete_after=15)

class log(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def log(self,ctx):
        user = ctx.author
        roleadmin = get(user.roles, id=807568934307627048)
        rolefondateur = get(user.roles, id=796776575278121029)
        if roleadmin in user.roles or rolefondateur in user.roles :
            await ctx.message.delete()
            await ctx.send(file=discord.File(r'logs_spec.txt'),delete_after=30)
            await ctx.send(f'<@{user.id}> tu as 30 secondes pour telecharger le fichier',delete_after=30)
        else:
           await ctx.message.delete()
           await ctx.send(f'<@{user.id}> tu as pas le role pour executer cette commande',delete_after=15)
