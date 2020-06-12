import os
import db
import json
import discord
# from dotenv import load_dotenv
from discord.ext import commands, tasks
from datetime import datetime

client = commands.Bot(command_prefix = 'b!') 
client.remove_command('help')

# load_dotenv()

token = os.getenv('TOKEN')
birthdays = db.connect()

@client.event
async def on_ready():
    print('Bot is ready.')

@tasks.loop(hours=24)
async def called_once_a_day():
    await client.wait_until_ready()
    date = datetime.date(datetime.now())
    datem = date.strftime('%y/%m/%d')
    results = birthdays.find({"birthday":datem[3:]})
    for birthday in results:
        name = birthday["name"]
        channel = client.get_channel(birthday["cid"])
        msg = 'Happy Birthday, %s!' % name
        print(msg)
        await channel.send(msg)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        print(error, type(error))
        await ctx.send(error)
    elif isinstance(error, discord.ext.commands.errors.CommandNotFound):
        print(error, type(error))
        await ctx.send("That's not a command. Take a look at commands https://github.com/tcolas673/birthdaybot")
    else:
        print(error, type(error))
        await ctx.send("Whoops! Looks liks something's amiss")

@client.command()
async def all(ctx):
    msg = ''
    for birthday in birthdays.find({"sid":ctx.guild.id}).sort('birthday',1):
        name = birthday["name"]
        msg = msg + name + ' ' + birthday['birthday'] + '\n'
    if not msg:
        await ctx.send("No birthdays have been added yet")
    else:    
        await ctx.send(msg)

@client.command(aliases=['help'])
async def commands(ctx):
    embed = discord.Embed(
            title ='Supported Commands',
            color = discord.Colour.gold()
        )
    embed.add_field(name='b!add name mm/dd', value='Add a name and birthday to the system.', inline=False)
    embed.add_field(name='b!all', value='Lists all birthdays in the system.', inline=False)
    embed.add_field(name='b!delete name', value='Removes a birthday from the system.', inline=False)
    embed.add_field(name='b!deleteAll', value='Removes all birthday\'s added.Administrator\'s only', inline=False)
    embed.add_field(name='b!edit name', value='Allows you to edit a birthday in the system with that corresponding name.', inline=False)
    embed.add_field(name='b!help', value='Lists all bot commands.', inline=False)
    embed.add_field(name='b!here', value='Allocates all Happy birthday notices to current channel.', inline=False)
    embed.add_field(name='b!month monthoftheyear', value='Allows you to view all birthdays for that month.', inline=False)
    embed.add_field(name='b!name username', value='Shows birthdate of user if in the system', inline=False)
    embed.add_field(name='b!thisMonth', value='Shows all birthdays for the current month.', inline=False)
    embed.add_field(name='b!today', value='Prints a happy birthday message for birthdays today', inline=False)
    await ctx.send(embed=embed)

@client.command()
async def here(ctx):
    await ctx.send('Are you sure you want all birthday messages posted here? Enter y for yes or n for no')
    #pull in response
    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30)
    if msg.content == 'n':
       await ctx.send('No worries nothing was changed')
    elif msg.content == 'y':
        # set up a role check
        if ctx.message.author.guild_permissions.administrator:
            birthdays.update_many({"sid":ctx.guild.id}, {"$set":{"cid": ctx.channel.id}})
            await ctx.send('All Birthday notices will appear here')
        else:
            await ctx.send('Only Administrators can use this function')
    else:
       await ctx.send('Operation ended. Invalid input')
   
@client.command()
async def today(ctx):
    date = datetime.date(datetime.now())
    datem = date.strftime('%y/%m/%d')
    results = birthdays.find({"birthday":datem[3:], "sid":ctx.guild.id})
    if results.count() < 1:
        msg = 'No birthdays today'
        await ctx.send(msg)
    else:
        for birthday in results:
            name = birthday["name"]
            await ctx.send('Happy Birthday, %s!' % name)


@client.command()
async def thisMonth(ctx):
    date = datetime.date(datetime.now())
    datem = date.strftime('%y/%m/%d')
    month = str(datem[3:5])
    
    results = birthdays.find({"month":month, "sid":ctx.guild.id}).sort('birthday',1)
    if results.count() < 1:
        msg = 'No birthdays this month'
        await ctx.send(msg)
    else:
        msg = ''
        for birthday in results:
            name = birthday["name"]
            msg = msg + name + ' ' + birthday['birthday'] + '\n'
        await ctx.send(msg)
               
# make a command to see birthdays for each month
@client.command()
async def month(ctx, month):
    month = month.lower()
    months = dict(january='01',february='02', march='03', april='04', may='05', june='06', july='07', august='08', september='09',october='10',november='11',december='12')
    results = birthdays.find({"month":months[month], "sid":ctx.guild.id}).sort('birthday',1)
    if results.count() < 1:
        msg = 'No birthdays in %s' % month
        await ctx.send(msg)
    else:
        msg = ''
        for birthday in results:
                name = birthday["name"]
                msg = msg + name + ' ' + birthday['birthday'] + '\n'
        await ctx.send(msg)
    
# make a birthday appear using someone's name
@client.command()
async def name(ctx, name):
    results = birthdays.find({"name":name, "sid":ctx.guild.id})
    if results.count() < 1:
        msg = 'No birthdays found with that name'
        await ctx.send(msg)
    else:
        for birthday in results:
            await ctx.send(birthday["birthday"])

def validate(date_text):
        date_text = '2020/'+ date_text
        try:
            datetime.strptime(date_text, '%Y/%m/%d')
            return True
        except ValueError:
            return False

# add birthdays to dictionary
@client.command()
async def add(ctx, name, birthday):
    if len(birthday) < 4:
        return False
    # make sure birthday is listed in the right format
    if validate(birthday) == False:
        await ctx.send("Incorrect data format, should be MM/DD")
    else:
        birthdays.insert_one({
            "name": name,
            "birthday": birthday,
            "month": birthday[:2],
            "sid": ctx.guild.id,
            "cid": ctx.channel.id
            })
        await ctx.send(name + '\'s birthday was added')

# edit a birthday 
@client.command()
async def edit(ctx, name, birth):
    results = birthdays.find({"name":name, "sid":ctx.guild.id})
    if results.count() < 1:
        msg = 'No birthdays found with that name'
        await ctx.send(msg)
    elif validate(birth) == False:
        await ctx.send("Incorrect data format, should be MM/DD")
    else: 
        birthdays.update_one({"name":name, "sid":ctx.guild.id}, {"$set":{"birthday":birth, "month":birth[:2]}})
        await ctx.send('Birthday updated')
            

# delete birthday function
@client.command()
async def delete(ctx, name):
   results = birthdays.find({"name":name, "sid":ctx.guild.id})
   if results.count() < 1:
        msg = 'No birthdays found with that name'
        await ctx.send(msg)
   else:
    birthdays.delete_one({"name":name, "sid":ctx.guild.id})
    await ctx.send('Birthday deleted')

# delete birthday function
@client.command()
async def deleteAll(ctx):
   #send a message to confirm
   await ctx.send('Are you sure you want to delete all birthdays? Enter y for yes or n for no')
   #pull in response
   msg = await client.wait_for('message', check=lambda message: message.author == ctx.author, timeout=30)
   if msg.content == 'n':
       await ctx.send('No worries nothing was deleted')
   elif msg.content == 'y':
        # set up a role check
        if ctx.message.author.guild_permissions.administrator:
            birthdays.delete_many({"sid":ctx.guild.id})
            await ctx.send('All Birthday\'s have been deleted')
        else: 
            await ctx.send('Only Administrators can use this function')
   else:
       await ctx.send('Operation ended. Invalid input')




called_once_a_day.start()

client.run(token)
