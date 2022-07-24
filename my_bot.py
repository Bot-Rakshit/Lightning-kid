import requests
from apikeys import *
from bs4 import BeautifulSoup as bs
#loading in our first webpage
r = requests.get("https://aicf.in/all-events/")
#convert to a beautiful soup object
soup=bs(r.content,"html.parser")
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
bro = []

# importing discord package
import discord
from discord.ext import commands

#client
client = commands.Bot(command_prefix = '!')
#Functionality 
@client.event
async def on_ready():
    print('Bot is ready')
    print("---------------------------------------------------")
    print("---------------------------------------------------")
    print("\n")

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def Calendar(ctx, *, city1=None):
    if city1 == None:
        await ctx.send(f'{ctx.author.mention}, Please enter your city to view events!')
        return
    await ctx.send(f'{ctx.author.mention} Your city is {city1}! Looking for events.')
    if city1 in city:
        tourney_name = tournament[city.index(city1)]
        start_date_1 = start_date[city.index(city1)]
        end_date_1 = end_date[city.index(city1)]
    details =(f'The tournament is : {tourney_name} The tournament starts on  {start_date_1} & ends on {end_date_1}. {ctx.author.mention} Good Luck :) ' )
    await ctx.send(details)
         #   tourney_name = tournament[city.index(msg.content)]
         #   start_date_1 = start_date[city.index(msg.contenxt)]
         #   end_date_1 = end_date[city.index(msg.content)]
         #   await msg.channel.send("The tournament is:",tourney_name,"\n","The start date is:",start_date_1,"\n","The end date is:",end_date_1)

    

# load in the necessary libararies 




#running the client on the server
client.run(token)

