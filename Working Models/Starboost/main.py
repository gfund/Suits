import threading

from webs import keep_alive
import discord
import os

import datetime
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
import asyncio



import hackchat

def message_got(chat, message, sender):
    
 #send the hack.chat message to the user
 bot.loop.create_task(usersend(f"Hackchat message: {sender}:   {message} "))
   
    
   
#hack.chat details
chat = hackchat.HackChat("Starboost", "ironlegion")
chat.on_message += [message_got]

  
 
  
   
  

      


#send messages to user
async def usersend(messagetext):
    global suituser
   
    user=await bot.fetch_user(suituser)
     
    await user.send(messagetext)



intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!',intents=intents)
global suituser
suituser=int(os.environ.get("suituser"))


@bot.event
async def on_ready():
 

  await usersend("Booted Systems")
  
  
 

@bot.command()
async def ping(ctx):

    await ctx.send((str((bot.latency*1000))) + "ms")

@bot.event
async def on_message(message):
  
  global suituser
  if message.author.id==suituser:
    await bot.process_commands(message)


#get token from env
TOKEN=os.environ.get("DISCORD_BOT_SECRET")
#keep repl alive
keep_alive()
#hack chat
hackchat = threading.Thread(target=chat.run, args=())
hackchat.start()
#discord
bot.run(TOKEN)




