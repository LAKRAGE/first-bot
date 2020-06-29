import discord
import random
import os
from discord.ext import commands, tasks
client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('UNDER DEVELOPMENT'))
    print('Bot is ready.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments.')
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required perms to use this command")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I am missing the perms to use this command.")
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid Command')





@client.command()
async def hello(ctx):
    await ctx.send('Hello mate. How are you? I am currently under development')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *,question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes definitely.',
                 'You may rely on it',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good',
                 'Yes',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good',
                 'Very doubtful.']
    await ctx.send (f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def rps(ctx,*,choice):
    answer = ['rock',
                  'paper',
                  'scissors']
    await ctx.send (f'You chose {choice}\nBot chose {random.choice(answer)}')
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'{amount} messages have been deleted!')
@client.command()
async def about(ctx):
    await ctx.send(f'Hey! I am new in this world. LAKRAGE gave me my life. I am under development and one day I will be perfect!')
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} Has Been Kicked For {reason}.')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} Has Been Banned For {reason}.')

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'unbanned {user.mention}')
            return
    @client.command()
    async def load(ctx, extension):
        client.load_extension(f'cogs.{extension}')
@client.command()
async def unload(ctx, extension):
        client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):

    if filename.endswith('py'):
        client.load_extension(f'cogs.{filename[:-3]}')
@client.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.add_roles(role)
    await ctx.send('Added Roles!')
@client.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member=None):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not member:
        await ctx.send("Please specify a member")
        return
    await member.remove_roles(role)
    await ctx.send('Removed Roles!')


@client.command()
async def coinflip(ctx):
    choices = ["Heads","Tails"]
    randomcoin = random.choice(choices)
    await ctx.send(randomcoin)

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    await channel.send(f'Welcome, {member.mention} to the server!')
    roles = discord.utils.get(member.guild.roles, name="VISITOR")
    await member.add_roles(roles)
@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    await channel.send(f'Goodbye, {member}!')















client.run('NzI2NDIwNzQyNzYxMzQ5MTUw.XvifWw.7ET0PYIb18LK9iunIT_z87ZkDe8')
