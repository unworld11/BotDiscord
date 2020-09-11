import os
import random
from googlesearch import search 
from dotenv import load_dotenv
import json
import wikipedia
from apiclient.discovery import build



# 1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
api_key =os.getenv('API_KEY')

# 2
bot = commands.Bot(command_prefix='!')



@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

newUserMessage = "Welcome To Our Server We created it with Maggi Masala and Chilli Flakes and mods are not gay"

@bot.command
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    await ctx.send(newUserMessage)
    print("Sent message to " + member.name)

@bot.command(name='hey',help='gives intro')
async def hey(ctx):
    await ctx.send("Hey,I am Bjarte.I was created by @unworld.I amm his first test project.I can do Google and Wiki Searches and some fun stuff too")
    await ctx.send("For more Info on commands type '!help'")
    


@bot.command(name='googleit', help ='Does a Google search')
async def Search(ctx,search : str):

    resource = build("customsearch",'v1', developerKey=api_key).cse()
    result = resource.list(q=search, cx='5b643544464eed75a').execute()
    count = 0
    for item in result['items']:
        if count<=5:
            await ctx.send(item['title'])
            await ctx.send(item['link'])
            count+=1
        else:
            break
    


@bot.command(name='wiki',help='does a wikipedia search')
async def wiki(ctx,search :str):
    query = wikipedia.page(search)
    response = query.content
    URLresponse = query.url

    await ctx.send(response[:200])
    await ctx.send(URLresponse)
    
    

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.randint(1, number_of_sides ))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='99',help = 'throws a random brooklyn nine-nine quote')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)



@bot.command(name='69',help='discover it yourseelf')
async def six_nine(ctx):
    response = 'nice mate'
    await ctx.send(response)
    await ctx.send('we are not a NSFW channel')

bot.run(TOKEN)
