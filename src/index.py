import datetime
import re

import discord
from discord.ext import commands

from urllib import parse, request


bot = commands.Bot(command_prefix="!", description="This is a helper bot")

image="https://lh3.googleusercontent.com/proxy/Iftiii4h2Vx4Ha35MJxfv5d2hwICSqcKfvUlJJwEcr1VIlnbzQyDd5Rx-yhqUapDX2EbNTndXDUsOq2JQZF51DWq1GtPbEd4OE7JjcX5XmOP0BJjsaU"

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", 
    description="Programming a discord bot is very fun",
    timestamp=datetime.datetime.utcnow(),
    color= discord.Color.blue())
    embed.add_field(name="Server create at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}"),
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}"),
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}"),
    embed.set_thumbnail(url=f"{image}")
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    search_query = parse.urlencode({'search': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + search_query)
    search_result = search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())

    await ctx.send('http://www.youtube.com/watch?v=' + search_results[0])


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Tutorials", url="http://www.twitch.tv/accountname"))
    print("My bot is ready")

bot.run("NzUxNDQ4NDYxODc3OTY4OTYw.X1JO6g.dkRhLfG-j10YUzYYDIp3wedl_rw")
