python  
import discord
from discord.ext import commands

Token= Some_random_token_given_to_your_bot #DO NOT SHARE it
client = commands.Bot(command_prefix='y.') #here ive chosen .y to be my bot command, most common ones are !,$ but theyre used alot to go for something unique

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game(name="")) #this shows the activity of the discord bot
    
client.run("Token")  #now! never share your bot token!
