import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Done!!')

bot.run('OTc5OTI2NzUyNTE0MTU4NjAz.GK8VfV.nMqcA4K595RcLDHm9lPuZ_7xcBZNzJH7Z-3u1Q')