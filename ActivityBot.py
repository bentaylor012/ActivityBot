
"""
 activity tracker bot when it is running it will track how many messages each user is sending and store them
 Future implementation: allow the bot to scrape through old messages on initial start-up and then recreate the 
 json file.
"""

import discord
from discord.ext import tasks, commands
#import numpy as np
#import pandas as pd
import time
import asyncio
import json
from json.decoder import JSONDecodeError



TOKEN = '' #add token here
Sid = #add server id here

client=commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('bot is ready.')
    #id = client.get_guild(Sid)
    #channel=discord.utils.get(server.channels, name="general-chat")
    #channelLink='/channels/'+Sid+'/messages';
    #messages = discord.utils.get(channelLink)
    #print('messages: '+str(len(messages)))
    #print(messages)

@client.event
async def on_message(message):
   
    contains=0
    file = open("logger.json",'r')
    try:
        dict=json.load(file)
    except JSONDecodeError:
        dict={}       
    
    
    if str(message.author)in dict:
        dict[str(message.author)]+=1
        contains=1
    if contains==0:
        dict[str(message.author)]=1
    with open('logger.json', 'w') as outfile:
        json.dump( dict, outfile)
    
    file.close
           
    

#@client.event
#async def

client.run(TOKEN)

