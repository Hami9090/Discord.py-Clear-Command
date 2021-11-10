import discord
import datetime
from discord.ext import commands
from discord.ext.commands.core import command, has_permissions


#We are now writing the prefix bot that you can put anything, which I considered "!"
client = commands.Bot(command_prefix="!")

#Now I create an event that when the bot goes online,
# it tells me in the terminal that this bot went online.
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

#These equations are also useful
#for the footer that when you run
#the bot and use the command,
# you will realize
time = datetime.datetime.now()
today_time = time.strftime(" • Today at %I:%M %p")


#Well, first I define the command here,
# what is its name that I use this command when I run the robot.
@client.command()
@has_permissions(manage_messages=True)
#The amount also means how much message to delete
async def clear(ctx, amount=100):
    mention = ctx.author.mention
    await ctx.channel.purge(limit=amount)
    #Here, too, we define what Embed will say to us when he deletes the messages
    my_embed = discord.Embed(title=f'{amount} Messages Delete', description=f'\n\n **message have been successfully delete ✅**' f'\n\n **🖱️ By :** {mention}', colour = 0x87FF00)
    my_embed.set_thumbnail(
        url = ctx.author.avatar_url)
    my_embed.set_footer(text=f"\n\n{ctx.author.name}{today_time} " , icon_url=ctx.author.avatar_url)
    await ctx.send(embed=my_embed)
    await member.send(embed=my_embed)
#Here we put the robot token inside "" to run the bot
client.run("")