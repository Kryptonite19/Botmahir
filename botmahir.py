import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event

async def on_ready():
    print('Mahir kulübeye geldi.')

@client.event

async def on_member_join(member):
    print(f'{member} kıraathaneye katıldı selam olsun !!')

client.run('NzQ1MjgxNzMxNDI2Mzg1OTUx.Xzvfsw.dBG1KD3bVi-PlVBp9u9CaCSsf6g')
