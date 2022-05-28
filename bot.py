import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
@bot.command()
async def ping(ctx):
    await ctx.send(f'延遲: {round(bot.latency*1000)} 毫秒')

@bot.event
async def on_ready():
    channel=bot.get_channel(859571060701790211)
    await channel.send('Status:**``Online``**)'
    f'延遲 {round(bot.latency*1000)} 毫秒')
    print('Done')



bot.run('OTc5OTI2NzUyNTE0MTU4NjAz.GK8VfV.nMqcA4K595RcLDHm9lPuZ_7xcBZNzJH7Z-3u1Q')