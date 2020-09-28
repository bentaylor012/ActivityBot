
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
import requests

logs={}

TOKEN = 'enter-token-here'
Sid = ''#enter server id here

client=commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('bot is ready.')
    authorization = {'Authorization':'Bot TOKEN'}
    r = requests.get('https://discord.com/api/channels/Sid/messages', headers=authorization)
    data=r.json()
    #messages = discord.utils.get(channelLink)
    print('messages: '+str(len(data)))
    for obj in data:
        if obj['author']['username'] in logs:
            logs[obj['author']['username']]+=1
        else:
            logs[obj['author']['username']]=1
        #print(obj['content'])
    with open('logger.json', 'w') as outfile:
        json.dump(logs, outfile)
   

@client.event
async def on_message(message):   
    
    if str(message.author)in logs:
        logs[str(message.author)]+=1
        
    else:
        logs[str(message.author)]=1
    with open('logger.json', 'w') as outfile:
        json.dump(logs, outfile)
    
    file.close
           
    



client.run(TOKEN)

