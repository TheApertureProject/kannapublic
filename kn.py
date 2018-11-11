botversion = '1.2.6'
print("___________________________________________________")
print("""
            _  __                    _  
           | |/ /__ _ _ _  _ _  __ _| | 
           | ' </ _` | ' \| ' \/ _` |_| 
           |_|\_\__,_|_||_|_||_\__,_(_) 
""")
print("             The Kawaii Discord bot !           ")
print("                                                   ")
print("                      "+botversion+"                      ")
print("                                                   ")
print("___________________________________________________")
print()
import time
from time import *
print(('[' + ctime()) + "] Lib 'time' successfully imported !")
import os
print(('[' + ctime()) + "] Lib 'os' successfully imported !")
import datetime
from datetime import *
print(('[' + ctime()) + "] Lib 'datetime' successfully imported !")
import random
from random import *
print(('[' + ctime()) + "] Lib 'random' successfully imported !")
import sys
from sys import exit, version
print(('[' + ctime()) + "] Lib 'sys' [exit, version] successfully imported !")
import asyncio
from asyncio import *
print(('[' + ctime()) + "] Lib 'asyncio' [exit, version] successfully imported !")
import discord
from discord.ext import commands
print(('[' + ctime()) + "] Lib 'discord' successfully imported !")
import dblpy
from dblpy import *
print(('[' + ctime()) + "] Lib 'dblpy' successfully imported !")
print(('[' + ctime()) + '] Establishing connection with the bot...')
bot = commands.Bot(description='Kanna - The Kawaii Discord bot - Server management bot ©2018 Poulpe#2356', command_prefix='k!')
bot.remove_command('help')

def __init__(self, bot):
	self.bot = bot
	self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjQ2NzMzMjYyMzY3NzUyMTk0MCIsImJvdCI6dHJ1ZSwiaWF0IjoxNTQxOTQ5NDU4fQ.qEzwfPUK1VTwU-8lBMVLMY9nTcNlM_yYa6gfsqDpX00'
	self.dblpy = dbl.Client(self.bot, self.token)
	self.bot.loop.create_task(self.update_stats())

#emotes
prefiximg = ':prefiximg:505768310227599371'
#end-emotes

@bot.event
async def on_ready():
	print(('[' + ctime()) + '] Connection successfully established with the bot user :', bot.user.name)
	print('Bot user ID :', bot.user.name)
	await bot.change_presence(activity=discord.Game(name=f'with {len(bot.users)} users, on {len(bot.guilds)} servers | k!help'))
	print(('[' + ctime()) + '] Presence successfully updated !')
	print('___________________________________________________')
        while True:
            logger.info('Attempting to post server count')
            try:
                await self.dblpy.post_server_count()
                logger.info('Succesfully posted server count ({})'.format(len(self.bot.guilds)))
            except Exception as e:
                logger.exception('Failed to post server count\n{}: {}'.format(type(e).__name__, e))
            await asyncio.sleep(1800)

@bot.event
async def on_guild_join(guild):
	my_guild = bot.get_guild(462871882916560896)
	join = my_guild.get_channel(462875598184775700)
	e = discord.Embed(description='', title='Server Joined - {}'.format(guild.name), color=1565439, timestamp=datetime.utcnow())
	e.add_field(name='Member count : {}'.format(guild.member_count), value='Created at {}'.format(guild.created_at))
	e.set_footer(text='Kanna - The Kawaii Discord bot')
	await bot.change_presence(activity=discord.Game(name=f'with {len(bot.users)} users, on {len(bot.guilds)} servers | k!help'))
	await join.send(embed=e)

@bot.event
async def on_guild_remove(guild):
	my_guild = bot.get_guild(462871882916560896)
	join = my_guild.get_channel(462875598184775700)
	e = discord.Embed(description='', title='Server left - {}'.format(guild.name), color=16744448, timestamp=datetime.utcnow())
	e.add_field(name='Member count : {}'.format(guild.member_count), value='Created at {}'.format(guild.created_at))
	e.set_footer(text='Kanna - The Kawaii Discord bot')
	await bot.change_presence(activity=discord.Game(name=f'with {len(bot.users)} users, on {len(bot.guilds)} servers | k!help'))
	await join.send(embed=e)

@bot.event
async def on_member_join(member):
	if member.guild.id == 462871882916560896:
		role = discord.utils.get(member.guild.roles, name='Members')
		await member.add_roles(role)


@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send('I am sorry, but it looks like... you dont have the required permissions !')
		await asyncio.sleep(0.5)
		await ctx.send("I can't let you do that !")
	elif isinstance(error, commands.MissingRequiredArgument):
		await ctx.say('Member not found. Sorry... Retry please !')
	elif isinstance(error, commands.BadArgument):
		await ctx.say('Member not found. Retry please !')

@bot.listen()
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.message.add_reaction('❌')

def is_owner(ctx):
	if ctx.author.id == 458586186328571913:
		return True
	else :
		return False

@bot.group(invoke_without_command=True, aliases=['hlp', 'commandlist', 'commands'])
async def help(ctx):
	e = discord.Embed(description="🔰 Help categories 🔰", title='➡️Interactive help', color=0x33CC33, timestamp=datetime.utcnow())
	e.set_thumbnail(url="https://cdn.discordapp.com/emojis/377480330103488532.png?v=1")
	e.add_field(name='`info`', value='Bot information related commands')
	e.add_field(name='`utilities`', value='All our amazing utilities !')
	e.add_field(name='`moderator`', value='Moderation related commands')
	e.add_field(name='`fun`', value='Fun related commands ~^^')
	e.set_footer(text='Type k!help <category> to display specific commands.')
	if ctx.author.id == 458586186328571913 :
			e.add_field(name='`master`', value="My master's commands !")
	await ctx.send(embed=e)

@help.command(name="info")
async def help_info(ctx):
	e = discord.Embed(description="📎 Basic commands 📎", title='➡️Commands list', color=0x00FFC0, timestamp=datetime.utcnow())
	e.set_thumbnail(url="https://cdn.discordapp.com/emojis/470912852543275009.gif?v=1")
	e.add_field(name=f'<{prefiximg}>`info`', value='Get to know me :3')
	e.add_field(name=f'<{prefiximg}>`ping`', value='Test my reactivity !')
	e.add_field(name=f'<{prefiximg}>`suggest <suggestion>`', value='Tell us what you think we could improve on Kanna. Your suggestion will be sent to the official bot server.')
	e.add_field(name=f'<{prefiximg}>`bugreport <bug>`', value ='If you found some bug or error on Kanna, just tell us via this command ! Your report will be sent to the official bot server.')
	e.add_field(name=f'<{prefiximg}>`help`', value='Displays the primary help message')
	await ctx.send(embed=e)

@help.command(name='all')
async def help_all(ctx):
	c = discord.Embed(description='📚 All the commands 📚', title='➡️Commands list', color=0x003366, timestamp=datetime.utcnow())
	c.set_thumbnail(url="https://cdn.discordapp.com/emojis/471044511804686348.gif?v=1")
	c.add_field(name="`help`, `info`, `ping`, `suggest <suggestion>`, `bugreport <bug>`, `kick <member/id>`,`ban <member/id> <reason>`, `clear <amount of messages>`, `clear <amount of messages>`, `pp <user>`, `roll <number>`", value='Full commands list')
	c.add_field(name="`info`, `utilities`, `moderator`, `fun`", value='Help categories')
	await ctx.send(embed=c)

@help.command(name='utilities')
async def help_utilities(ctx):
	c = discord.Embed(description='⚒️ Utilities ⚒️', title='➡️Commands list', color=0x003366, timestamp=datetime.utcnow())
	c.set_thumbnail(url="https://cdn.discordapp.com/emojis/395627468276367370.png?v=1")
	c.add_field(name=f'<{prefiximg}>`pp <user>`', value='Get the profile picture of some user')
	await ctx.send(embed=c)

@help.command(name="moderator")
async def help_moderator(ctx):
	a = discord.Embed(description="🛡️ Moderator commands 🛡️", title='➡️Commands list', color=0xffff00, timestamp=datetime.utcnow()) 
	a.set_thumbnail(url="https://cdn.discordapp.com/emojis/474539445379661824.png?v=1")
	a.add_field(name=f'<{prefiximg}>`kick <member/id>`', value='Kick someone from the server')
	a.add_field(name=f'<{prefiximg}>`ban <member/id> <reason>`', value='Kick a member from the server permanently (ban)')
	a.add_field(name=f'<{prefiximg}>`clear <amount of messages>`', value='Delete a specific number of messages (no limit - be extremely careful)')
	await ctx.send(embed=a)

@help.command(name="fun")
async def help_fun(ctx):
	d = discord.Embed(description='🎀 Fun 🎀', title='➡️Commands list', color=0xFFA2DD, timestamp=datetime.utcnow())
	d.set_thumbnail(url="https://cdn.discordapp.com/emojis/398860813881835533.png?v=1")
	d.add_field(name='`roll <number>`', value="Roll a dice with the specified number of faces (no limit !)")
	d.add_field(name='Lots of commands incoming !', value="Stay awhile, they'll be deployed soon ;)")
	await ctx.send(embed=d)

@commands.check(is_owner)
@help.command(name="master")
async def help_master(ctx):
	b = discord.Embed(description='♥️ Master commands ♥️', title='➡️Commands list', color=0xFF0000, timestamp=datetime.utcnow())
	b.set_thumbnail(url="https://cdn.discordapp.com/attachments/476653267036930049/498859365046943745/1538964466545.png")
	b.add_field(name=f'<{prefiximg}>`say <channel> <text>`', value='Talk through me !')
	b.add_field(name=f'<{prefiximg}>`shutdown`', value='Shut me down...')
	b.add_field(name=f'<{prefiximg}>`presence`', value='Reload the presence indicator')
	try:
		await ctx.send(embed=b)
	except:
		await ctx.send("Access denied ! Y~you're not my master !")

#fun

@bot.command()
async def roll(ctx, value: int):
	try:
		result=randint(1,value)
		msg = await ctx.send(f'And the result is...')
		await asyncio.sleep(2)
		await msg.edit(content=f'And the result is... {result} ! 🎉')
	except:
		await ctx.send('Please send a valid number of messages !')

@bot.command(aliases=['utilities', 'moderator', 'all', 'master'])
async def fun(ctx):
	await ctx.send("Please type `k!help <name of the category>` to get specific help about a category. Don't forget the `help` !")

@bot.command(aliases=['add', 'invitelink'])
async def invite(ctx):
	await ctx.send("""Here is my invite link ! Thanks for adding me ♥
<https://bit.ly/2KCvxDw>""")

@bot.command(aliases=['profilepic', 'ppic', 'avatar'])
async def pp(ctx, usr: discord.User):
	e = discord.Embed(description="👤 {}'s profile picture".format(usr.name), title='➡️Avatar', color=0x5D5DFF, timestamp=datetime.utcnow())
	e.set_image(url=usr.avatar_url)
	await ctx.send(embed=e)

@commands.check(is_owner)
@bot.command()
async def presence(ctx):
	await bot.change_presence(activity=discord.Game(name=f'with {len(bot.users)} users, on {len(bot.guilds)} servers | k!help'))
	await ctx.send('Presence succesfully updated.')

@bot.command()
async def coolservs(ctx):
	e = discord.Embed(description="🌴 Nicu servers 🌴", title='➡️Discover other places', color=0xFFFFFF, timestamp=datetime.utcnow())
	e.set_thumbnail(url="https://cdn.discordapp.com/attachments/476653267036930049/499655332788830208/471600972045484032.png")
	e.add_field(name='The Aperture Project', value='A nice place to chill out and have fun, with giveaways, kawaii pics and a super friendly community ! https://discord.gg/JEUUM8c')
	e.add_field(name="Sebis's bot tutorial", value='The best server to learn how to code bots in different languages ! https://discord.gg/GWdhBSp')
	await ctx.send(embed=e)

@commands.check(is_owner)
@bot.command(pass_context=True)
async def say(ctx, channel: discord.TextChannel, *, text):
	try:
		await ctx.channel.send(text)
	except Exception as e:
		print(e.args)

@say.error
async def say_handler(ctx, err):
	if isinstance(err, commands.CheckFailure):
		await ctx.send('Sorry, but only my master can use this command !')
	else:
		raise err

@commands.check(is_owner)
@bot.command()
async def shutdown(ctx):
	try:
		await ctx.send('Yes Master !')
		await ctx.send('Shutting down...')
		await ctx.send('Bye !')
		print(('[' + ctime()) + '] Succesfully shutted down.')
		sys.exit()
	except Exception as e:
		print(e.args)
		await ctx.send('An error occured. You should check the logs, I am sure it is nothing !')

@shutdown.error
async def shutdown_handler(ctx, err):
	if isinstance(err, commands.CheckFailure):
		await ctx.send('Access denied. You are not my Master !')
	else:
		raise err

@commands.has_permissions(ban_members=True)
@bot.command()
async def ban(ctx, member: discord.Member, *, reason: str = None):
	try:
		if reason==None:
			await member.ban()
			await ctx.send('Member'+member+'was successfully banned ! Good bye !')
			await ctx.send('And dont come back !')
		else:
			await member.ban(reason=reason)
			await ctx.send(f'Member'+member+'was successfully banned for the following reason : {reason} ! Good bye !')
	except Exception as e:
		print(e.args)
		await ctx.send('An error occured. Maybe did you enter a wrong username ?')

@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, *, member: discord.Member):
	try:
		await member.kick()
		await ctx.send('Member', member, 'was successfully kicked ! Babaï !')
	except Exception as e:
		print(e.args)
		await ctx.send('An error occured. Maybe did you enter a wrong username ?')

@commands.has_permissions(manage_messages=True)
@bot.command()
async def clear(ctx, amount: int):
	amount=amount+1
	try:
		deleted = await ctx.channel.purge(limit=amount)
		await ctx.send(f"`{len(deleted)}` messages successfully deleted !", delete_after = 5)
	except:
		await ctx.send("Something went wrong. Please retry indicating positive numbers only.")

@kick.error
async def kick_handler(ctx, err):
	if isinstance(err, commands.has_permissionsFailure):
		await ctx.send('W~what are you trying to do ?! You dont have the required permissions, baka !')
		await ctx.send("I won't let you do that !")
	else :
		raise err

@bot.command()
async def info(ctx):
	a = """Created by Poulpy#9355
Hosted on Heroku
Running on discord.py v1.0.0a
[Invite link](https://discordapp.com/oauth2/authorize?client_id=467332623677521940&scope=bot&permissions=2146958591)
[Official Server](https://discord.gg/PTT9UpZ)"""
	e = discord.Embed(description="Kanna Kamui, the Kawaii Discord bot !", title='More about me', color=0xF4A2FF, timestamp=datetime.utcnow())
	e.set_thumbnail(url="https://media.discordapp.net/attachments/489041727697584148/505805443453419541/1540620568476.png?width=376&height=376")
	e.add_field(name="Information", value=a)
	e.set_footer(text=botversion)
	e.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
	await ctx.send(embed=e)

@bot.command()
async def bugreport(ctx, *, bug):
	my_guild = bot.get_guild(462871882916560896)
	bugreport = my_guild.get_channel(462876207097053195)
	e = discord.Embed(description=bug, title='Bug Report', color=16711680, timestamp=datetime.utcnow())
	e.set_footer(text='Kanna - The Kawaii Discord bot')
	e.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
	await bugreport.send(embed=e)
	await ctx.send('A~a bug ?... Hope my master will be able to correct that... Anyway, thanks !')

@bot.command()
async def suggest(ctx, *, suggestion):
	my_guild = bot.get_guild(462871882916560896)
	suggested = my_guild.get_channel(464517370036224011)
	e = discord.Embed(description=suggestion, title='Suggestion', color=4259584, timestamp=datetime.utcnow())
	e.set_footer(text='Kanna - The Kawaii Discord bot')
	e.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
	await suggested.send(embed=e)
	await ctx.send('Suggestion sent ! Thanks for your implication !')

@bot.command()
async def ping(ctx):
	t = await ctx.send('Pong!')
	ms = (t.timestamp - ctx.message.timestamp).total_seconds() * 1000
	await t.edit(new_content=f'Pong! Latency : **{int(ms)} milliseconds** !')

bot.run(bot.run(os.environ['TOKEN']))
