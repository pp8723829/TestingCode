import discord
from discord.exe import commands

bot=commands.bot(command_prefix= '@')

@bot.event
async def on_ready():
    print('>>機器人狀態:線上<<')

bot.run('OTc5OTI2NzUyNTE0MTU4NjAz.GK8VfV.nMqcA4K595RcLDHm9lPuZ_7xcBZNzJH7Z-3u1Q')