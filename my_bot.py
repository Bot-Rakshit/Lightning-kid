import requests
from apikeys import *
from bs4 import BeautifulSoup as bs
import discord
from discord.ext import commands
from datetime import datetime

# loading in our first webpage
r = requests.get("https://aicf.in/all-events/")
# convert to a beautiful soup object
soup = bs(r.content, "html.parser")
tournament = []
for row in soup.find_all('table')[0].tbody.find_all('tr')[1:]:
    tournament.append(row.find_all('td')[1].text)
start_date = []
for row in soup.find_all('table')[0].tbody.find_all('tr')[1:]:
    start_date.append(row.find_all('td')[3].text)
end_date = []
for row in soup.find_all('table')[0].tbody.find_all('tr')[1:]:
    end_date.append(row.find_all('td')[4].text)
city = []
for row in soup.find_all('table')[0].tbody.find_all('tr')[1:]:
    city.append(row.find_all('td')[5].text)

# client
intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intents=intents)

# Functionality
@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def Calendar(ctx, *, city1=None):
    if city1 is None:
        await ctx.send(f'{ctx.author.mention}, Please enter your city to view events!')
        return
    await ctx.send(f'{ctx.author.mention} Your city is {city1}! Looking for events.')
    if city1 in city:
        event_dates = [datetime.strptime(date, '%d-%m-%Y').date() for date in start_date]
        today = datetime.now().date()
        for date, tournament_name in zip(event_dates, tournament):
            if city[city.index(city1)] and date >= today:
                details = (f'The next tournament in {city1} is {tournament_name}. '
                           f'The tournament starts on {start_date[event_dates.index(date)]} '
                           f'& ends on {end_date[event_dates.index(date)]}. '
                           f'{ctx.author.mention} Good Luck :)')
                await ctx.send(details)
                return
        await ctx.send(f'{ctx.author.mention}, no upcoming tournaments found in {city1}.')
    else:
        await ctx.send(f'{ctx.author.mention}, {city1} not found in our list of cities.')

# running the client on the server
client.run(token)
