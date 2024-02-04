import discord
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import os

# from apikey import *


intents = discord.Intents.default()
intents.members = True

token = ''
client = commands.Bot(command_prefix = '!', intents=intents)


# bot event

@client.event
async def on_ready():
    log.info(f'Your Darling {bot.user.name} Is Online')
    print('----------------------')
    print(f'| {bot.user.display_name} Is Online |')
    print('----------------------')

@client.event
async def on_member_join(member):
    print(f'"{bot.user.name}" Join Server:{guild.name} | ID: {guild.id} \n with {guild.member_count} Member Inside')
    await channel.send('Hello..')

@client.event
async def on_member_remove(member):
    print(f'"{bot.user.name}" Was Left Server:{guild.name} | ID:{guild.id}')

@client.event
async def on_message(message):
    
    if message.content == "hi":
        await message.delete()
        await message.channel.send(f'{user.user.name} Dont send that again')


# bot command

#test command
@client.command()
async def test(ctx):
    await ctx.send('Test')

#ping command
@client.command(aliases=['p','pi'])
async def ping(ctx):
    await ctx.send('Pong..')

#join command
@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You are not in Voice channel, you must be in Voice channel")

#left command
@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client_disconnect()
        await ctx.send(f'{bot.user.name} Was Left the voice channel')
    else:
        await ctx.send(f'{bot.user.name} Not in the voice channel')

#kick command
@client.command()
@has_permissions(kick_members = True)
async def kick(ctx, member:discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been Kicked')

@kick.error
async def kick_error(ctx, error):
    is isinstance(error, commands.MissingPermissions):
    await ctx.send('You dont have permission to kick people')

#ban command
@client.command()
@has_permissions(ban_members = True)
async def ban(ctx, member:discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User {member} has been banned')

@ban.error
async def ban_error(ctx, error):
    is isinstance(error, commands.MissingPermissions):
    await ctx.send('You dont have permission to ban people')

#unban command
@client.command()
@has_permissions(administrator = True)
async def unban(ctx, member: discord.Member, *, reason = None):

    banned_users = await ctx.guild.bans()
    print(banned_users)
    member_name, member_discriminator = member.split("#")
    print(member_name)

    for ban_entry in banned_users:
        print(ban_entry)
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, command.MissingPermissions):
        await ctx.send("You dont have permission to use the command")

#embed
@client.command()
async def embed(ctx):
    embed = discord.Embed(title="Testing", url="https://google.com", description="Testing embed in python", color=0x4dff4d)
    embed.set_author(name=ctx.author.display_name, url="https://instagram.com/kazuo_yuuka", icon_url=ctx.author.avatar_url)
    await ctx.send(embed)

client.run(token)
