import discord
from discord.ext import commands
import os

client=commands.Bot(command_prefix='!')
status=cycle(['jangan lupa tidur','hayo makan'])

@client.event
async def on_ready():
    print("online")
@task.loop(seconds=5)

async def change_status():
    await client.change_presence(activity=discord.listening(next(status)))
@client.event
async def on_member_join(member):
    print(f'{member}has joined a server.')
@client.event
async def on_member_remove(member):
    print(f'{member}has left a server.')
@client.command()
async def ping(ctx):
    await ctx.send(f"pong!{round(client.latency*1000)}ms")
@client.command()
async def clear(ctx,amount=10):
    await ctx.channel.purge(limit=amount)
@client.command()
async def kick(ctx,member=discord.Member,*,reason=None):
    await member.kick(reason=reason)
@client.command()
async def ban(ctx,member=discord.Member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"banned{member.mention}")
@client.command()
async def unban(ctx,*,member):
    banned_user=await ctx.guild.bans()
    member_name,member_discrimitor=member.split('#')

    for ban_entry in banned_user:
        user=ban_entry.user

        if(user.name,user.discrimitor)==(member_name.member_discrimitor):
            await ctx.guild.unban(user)
            await ctx.send(f"unbanned{user.mention}")
            return





client.run(TOKEN)