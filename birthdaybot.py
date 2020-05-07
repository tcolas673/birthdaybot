import os
import discord
from discord.ext import commands, tasks
from datetime import datetime

import json
with open('birthdays.json', 'r+') as f:
    birthdays = json.load(f)


    client = commands.Bot(command_prefix = 'b!') 

    target_channel_id = os.environ.get('ID')
    token = os.environ.get('TOKEN')

    @client.event
    async def on_ready():
        print('Bot is ready.')

    @tasks.loop(seconds=24)
    async def called_once_a_day():
        await client.wait_until_ready()
        date = datetime.date(datetime.now())
        datem = date.strftime('%y/%m/%d')
        if datem[3:] in birthdays:
            name = birthdays[datem[3:]]
            channel = client.get_channel(target_channel_id)
            msg = 'Happy Birthday, %s!' % name
            print(msg)
            await print(channel)

    @client.command()
    async def all(ctx):
        msg = ''
        for birthday in birthdays:
            name = birthdays[birthday]
            msg = msg + name + ' ' + birthday + '\n'
        await ctx.send(msg)

    @client.command()
    async def today(ctx):
        date = datetime.date(datetime.now())
        datem = date.strftime('%y/%m/%d')
        if datem[3:] in birthdays:
            name = birthdays[datem[3:]]
            await ctx.send('Happy Birthday, %s!' % name)

    @client.command()
    async def thisMonth(ctx):
        date = datetime.date(datetime.now())
        datem = date.strftime('%y/%m/%d')
        month = datem[3:5]
        found = False
        for birthday in birthdays:
            if birthday[:2] == month:
                found = True
                name = birthdays[birthday]
                msg = name + ' ' + birthday
                await ctx.send(msg)
            else:
                continue
        if found == False:
            msg = 'No birthdays this month'
            await ctx.send(msg)

    # make a command to see birthdays for each month
    @client.command()
    async def month(ctx, month):
        found = False
        month = month.lower()
        months = dict(january='01',february='02', march='03', april='04', may='05', june='06', july='07', august='08', september='09',october='10',november='11',december='12')
        for birthday in birthdays:
            if birthday[:2] == months[month]:
                found = True
                name = birthdays[birthday]
                msg = name + ' ' + birthday
                await ctx.send(msg)
        if found == False:
            msg = 'No birthdays in %s' % month
            await ctx.send(msg)

    # make a birthday appear using someone's name
    @client.command(aliases = list(birthdays.values()))
    async def name(ctx, name):
        for birthday in birthdays:
            if name == birthdays[birthday]:
                await ctx.send(birthday)
            else:
                continue

    # add birthdays to dictionary
    @client.command()
    async def add(ctx, name, birthday):
        f.seek(0)
        birthdays.update({birthday: name})
        json.dump(birthdays, f)
        await ctx.send( name + '\'s Birthday added')

    # edit a birthday 
    @client.command()
    async def edit(ctx, name, birth):
        for birthday in birthdays:
            if name == birthdays[birthday]:
                birthdays.pop(birthday, None)
                f.seek(0)
                birthdays.update({birth: name})
                json.dump(birthdays, f)
                await ctx.send('Birthday updated')
                break
            else:
                continue

    # delete birthday function
    @client.command()
    async def delete(ctx, name):
        for birthday in birthdays:
            if name == birthdays[birthday]:
                birthdays.pop(birthday, None)
                await ctx.send('Birthday deleted')
                break
            else:
                continue

    called_once_a_day.start()
    
    client.run(token)
