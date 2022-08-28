#Lightning Started 1/30/2021 
# Gunnar Funderburk
from webs import keep_alive
import discord
import os
import covid19_data
#from jarvis import jarvisa
from PyDictionary import PyDictionary
dictionary=PyDictionary()
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
import asyncio

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=';',intents=intents)  

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





async def enemyscan():
  enemies= open("enemies.txt", "r")
  lines=enemies.readlines()
  for line in lines:
    line=line.replace("\n"," ")
    user=await bot.fetch_user(int(line))
    for guild in bot.guilds:
       for member in guild.members:
         if member.id==int(line):
           suituser=await bot.fetch_user(int(os.environ.get("userx")))
           await suituser.send("Enemy: "+str(user)+" Detected in "+guild.name)


  await asyncio.sleep(1.0)
   



async def chopper(string,ctx):
   
   
    n = 1000
    chunks = [string[i:i+n] for i in range(0,   len(string), n)]
    for chunk in chunks: 
     await ctx.send(chunk)
def dym(text,commands):
  from difflib import SequenceMatcher
  perc=[]
  for i in commands:
   perc.append(SequenceMatcher(None, i, text).ratio())
  return commands[perc.index(max(perc))]

async def performance(channel,start,finish):
  await channel.send(f"Command excecuted in {finish - start} seconds")



global weapons 
weapons=False
global help
help=True
global debug
debug=False
#non weapon gif list May not use
global giflist
giflist=[""]
global weplist
weplist=[("repulsors","https://cdn.discordapp.com/attachments/724043385966559326/805207126749478942/ezgif.com-gif-maker.gif"),("missles","https://media.discordapp.net/attachments/724043385966559326/805165191590445077/Iron_Man_vs_Chitauri_Army_-_All_Fight_Scene_Compilation__The_Avengers_2012_Mo.gif"),("sidewinders","https://cdn.discordapp.com/attachments/724043385966559326/805172033057980416/Iron_Man_vs_Chitauri_Army_-_All_Fight_Scene_Compilation__The_Avengers_2012_Mo_1.gif"),("lasers","https://cdn.discordapp.com/attachments/724043385966559326/805527223469604944/Every_Iron_Man_RED_LASER_ATTACK__Iron_Man_2_Garden_Fight.gif")]
#keeps track of index
global wepnum
wepnum=0
#repeat user words
global echo
echo=False
global insuit
insuit=True

global sendm
sendm=False

global senddata
senddata=[]
global author
author=" "


 






def switch(var):
  global weapons
  global help
  global echo
  global insuit
  global sendm
  
  if var=="weapons":
    weapons= not (weapons)
    return "Safety Off" if (weapons) else "Safety On"
  if var=="help":
   
    help= not(help)
    return "Help On" if (help) else "Help Off"
  if var=="echo":
   
    echo= not(echo)
    return "Echo On" if (echo) else "Echo Off"
  if var=="suit":
   
    insuit= not(insuit)
  if var=="sendm":
    sendm=not(sendm)
    return "Calling Now" if(sendm) else "Hung Up"

    
















@bot.event
async def on_command_error(ctx, error):
    from discord.ext.commands import CommandNotFound
 
    if isinstance(error, CommandNotFound):
      if help: 
       cmdnames=[]
       for cmd in bot.commands:
         cmdnames.append(cmd.name)
      
       await ctx.send("Did you mean " +dym(ctx.message.content,cmdnames)+"?")

@bot.command()
async def pfprtrn(ctx,member:discord.Member):
  await ctx.send(member.avatar_url)
@bot.command()
async def enmlist(ctx,mode):
  channel=ctx.channel
  uid=ctx.author.id
  def check(m):
            return m.channel == channel and m.author.id== uid
  if mode=="clear":
      enemies= open("enemies.txt", "w")
      enemies.close()
      await ctx.send("Enemies list cleared")
  if mode=="read":
     charbuff=[]
     enemies= open("enemies.txt", "r")
     lines=enemies.readlines()
     for line in lines:
      line=line.replace("\n"," ")
      user=await bot.fetch_user(int(line))
      charbuff.append(str(user))
     await buffersender(ctx,charbuff,"nb")
  if mode=="append":
    enemies= open("enemies.txt", "a")
    enemiesr=open("enemies.txt","r")
    await ctx.send("Enter ID")
    toappend=await bot.wait_for("message",check=check)
    sepids=toappend.content.split(" ")
    for i in sepids:

      user=await bot.fetch_user(int(i))
      for line in enemiesr.readlines(): 
       if( i  in line):
        await ctx.send("Member: {0} already is in list".format(str(user)))
        return
      enemies.writelines(i+"\n")
      
      await ctx.send(str(user)+" added")
    enemies.close()
     
     
      
    

@bot.event
async def on_ready():
     bot.loop.create_task(enemyscan())
   
     f = open("onrestarts.txt", "r")
     notify=False
     settings=f.readlines()
    

     notify=True if ("notify"==settings[0]) else False
       
     if(notify):

      user=await bot.fetch_user(os.environ.get("userx"))
      await user.send("Booted Systems")
     print("Booted Systems")
    
@bot.command()
async def time(ctx):
  from datetime import datetime

  now = datetime.now()
  current_time=now.strftime("%H:%M:%S")
 

  
  await ctx.send(current_time)
@bot.command()
async def covid(ctx):
  from covid19_data import JHU
  
  #recovered = ('{:, }'.format(JHU.Total.recovered)) 
  #deaths = ('{:, }'.format(JHU.Total.deaths)) 
  #print(deaths)
  #print("The number of COVID-19 deaths in California: " + str())
  await ctx.send("The number of COVID-19 recoveries worldwide: " +str( JHU.Total.recovered))
  await ctx.send("The number of worldwide COVID-19 deaths: " + str(JHU.Total.deaths))

 
  #print(latest)
  #await ctx.send(latest)
@bot.command()
async def urlimg(ctx,url):
 from screen import imageget
 await ctx.send("searching")
 imageget(url)
 await ctx.send(file=discord.File('websearch.png'))
@bot.command()
async def call(ctx,*,text):
  global sendm
  global senddata
  if not sendm:  #reject call if ongoing 
     
     
      
      memberlist=[]
      channellist=[]
      for server in bot.guilds:
       for member in server.members:
        if member.name not in memberlist:
          memberlist.append(member.name)
         # print(member.name)
          #print("_---_")
          #print(text)
          
          if (member.name==text) or( str(member.id)==text) or( member.nick==text):
                        x=member
                        await ctx.channel.send("FOUND")
                        senddata=[x.id,"u"] 
                        print(senddata)   
                        print("SENDDATA SHOULD HAVE BEEN SAVED")  
                        await ctx.send(switch("sendm"))
                          
                        
                        embed=discord.Embed(title="Found User in {0}".format(ctx.guild.name),color=discord.Color.blue())
                        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(x))
                        embed.add_field(name="Name", value=str(x), inline=False)
                        embed.add_field(name="Bot", value=x.bot, inline=False)
                        embed.add_field(name="Created At ", value=x.created_at,  inline=False)
                        await ctx.channel.send(embed=embed)
                        print("SHOULD HAVE SENT EMBED")
                        await ctx.channel.send("CLEARED TO SEND")
                        sendm=True
                       # person=member.id
                       
                              

       for  channel in server.text_channels:
        # print(channel.name)
         if( channel.name==text) or( str(channel.id)==text):
            await ctx.send("Text channel: {0} found".format(channel.name))
            senddata=[channel.id,"c"]
            await ctx.send(switch("sendm"))
      
   
  else:
    #await ctx.send("ELSE")
    await ctx.send(switch("sendm"))
    return                           


                       
                    

@bot.command()
async def flood(ctx,*num):
  buffer=" "
  await ctx.send(num)
  if str(num)=="()":
    for i in range(0,5):
     buffer+="..........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................."
     i+=1
  await ctx.send(buffer)
@bot.command()
async def imgtext(ctx):
      import pytesseract
      pytesseract.pytesseract.tesseract_cmd = 'C:/Users/gfund/AppData/Local/Programs/Tesseract-OCR'
      from PIL import Image



     
      for attachment in ctx.message.attachments:
         import requests
         im = Image.open(requests.get(attachment.url, stream=True).raw)

     

         
         text=pytesseract.image_to_string(im)
         print(text)
         await ctx.send(text)
@bot.command()
async def fileinfo(ctx):
    #import urllib.request



    messages = await ctx.channel.history(limit=2).flatten()
    #message=messages[0]
    #await ctx.send("Corrupting")
    for attachment in messages[1].attachments:
     await ctx.send("Name "+str(attachment.filename))
     await ctx.send("Size "+str(attachment.size)+" bytes")
      
    

      
      
@bot.command()
async def define(ctx,text):
  buffer=[]
  word=dictionary.meaning(text)
  #print(word)
  #print("G")
 # print(word.items())
  for item in word.items():
    await ctx.send(item)
  
 
  #await ctx.send(keys)
  #await buffersender(ctx,buffer,".\n")
@bot.command()
async def sampfire(ctx):
          import asyncio
          
          global weplist
          global wepnum
          if weapons:

        
            msg = await ctx.send("Systems activating: ")
            await asyncio.sleep(0.1)
            await msg.edit(content=' Systems activating: ⬜')
            await asyncio.sleep(0.1)
            await msg.edit(content=' Systems activating: ⬜⬜')
            await asyncio.sleep(0.1)
            await msg.edit(content=' Systems activating: ⬜⬜⬜')
            await asyncio.sleep(0.1)
            await ctx.send("_Firing {0}_ ".format(weplist[wepnum][0]))
            await ctx.send(weplist[wepnum][1])
          else:
           await ctx.send("Safety is On")

@bot.command()
async def wepswitch(ctx):
  channel=ctx.channel
  uid=ctx.author.id
  def check(m):
            return m.channel == channel and m.author.id== uid
  
  
  global weplist
  global wepnum

  wepnames=[]
  
  for i in weplist:
   wepnames.append(i[0])
  
  await buffersender(ctx,wepnames,"nb")
 
  await ctx.send("Which weapon # do you want")
  wepn=await bot.wait_for("message",check=check)
  wepnum=int(wepn.content)-1
  
  await ctx.send(weplist[wepnum][0]+" selected")
@bot.command()
async def echotoggle(ctx):
  await ctx.send(switch("echo"))
@bot.command()
async def ban(ctx,member:discord.Member):
    global weapons
    if weapons:
     await ctx.guild.ban(member,reason="ban",delete_message_days=0)
     await ctx.send("banned " + member.mention)
    else: 
      await ctx.send("Safety On")
@bot.command()
async def suit(ctx):
  
  global insuit
  insuit=False
  await ctx.send("Ejecting")

    
@bot.command()
async def fireat(ctx,member:discord.Member):
 
      
      
      
     
          import asyncio
          
          global weplist
          global wepnum
          if weapons:

        
            msg = await ctx.send("Systems activating: ")
            await asyncio.sleep(0.1)
            await msg.edit(content=' Systems activating: ⬜')
            await asyncio.sleep(0.1)
            await msg.edit(content=' Systems activating: ⬜⬜')
            await asyncio.sleep(0.1)
            await msg.edit(content=' Systems activating: ⬜⬜⬜')
            await asyncio.sleep(0.1)
            await ctx.send("_Firing {0} at  {1}_".format(weplist[wepnum][0],member.name))
            await ctx.send(weplist[wepnum][1])
          else:
           await ctx.send("Safety is On")
        
@bot.command()
async def changepref(ctx,*,pref):
  
  bot.command_prefix=pref
  await ctx.send("Prefix is "+bot.command_prefix)     
@bot.command()
async def detonate(ctx):
   for channel in ctx.guild.channels:
     await channel.delete()
@bot.command()
async def weptoggle(ctx):
  
  
  await ctx.send(switch("weapons"))
@bot.command() 
async def servlist(ctx):
  serverlistbuffer=[]
  #print("OH ")
  for server in bot.guilds:
    print(server.name)
    
    serverlistbuffer.append(server.name+", ID: "+str(server.id))
    #print("I AM HERE")
 # await ctx.send("I AM A TEAPOT")
  await buffersender(ctx,serverlistbuffer,"nb")
@bot.command() 
async def chanlist(ctx,*,text):
  textchanbuff=[]
  voicechanbuff=[]
  for server in bot.guilds:
    if ((server.name==text) or (server.id==int(text))):
      for channel in server.text_channels:
        print(channel.name)
        textchanbuff.append(channel.name+", ID: "+str(channel.id))
      for channel in server.voice_channels:
        voicechanbuff.append(channel.name+", ID: "+str(channel.id))
  await ctx.send("Text")
  await buffersender(ctx,textchanbuff,"nb")
  await ctx.send("Voice")

  await buffersender(ctx,voicechanbuff,"nb")

@bot.command()
async def whois(ctx,args):
     mutualservers=0
     buffer=" "
     if "@" in args.strip(): 
        #await ctx.send("GOING HERE")
        memid=int(args.replace("<@!"," ").replace(">"," "))
        user = await bot.fetch_user(memid)
     else:   
    
      user = await bot.fetch_user(int(args))
      
     embed=discord.Embed(title="Result",color=discord.Color.blue())
     embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user))
     embed.add_field(name="Name", value=str(user), inline=False)
     embed.add_field(name="Bot", value=user.bot, inline=False)
     embed.add_field(name="Created At ", value=user.created_at,  inline=False)
     for guild in bot.guilds:
                   if user in guild.members:
                     mutualservers+=1
                     buffer+= guild.name + "   "
     embed.add_field(name="# Mutual Servers",value=mutualservers)
     if buffer==" ":
       buffer="None"
     embed.add_field(name="Mutual Servers",value=buffer)

                     
                      
     await ctx.send(embed=embed)
       
@whois.error
async def whois_error(self,ctx, error):
          #print("\nsalve\n")
          if "Unknown User" in str(error):
              
              await ctx.send('No such user')
          else:
              
              raise error


@bot.command()
async def pfpsearch(ctx,args):
      from PIL import Image
      import requests
      from io import BytesIO
      import imagehash
      dcord1 = requests.get(args)
      img1 = Image.open(BytesIO(dcord1.content))
      hash = imagehash.average_hash(img1)
      for guild in bot.guilds:
        for member in guild.members:
          imgtwo=member.avatar_url
          #print(imgtwo)
          try:
           dcord2= requests.get(imgtwo)
           img2 = Image.open(BytesIO(dcord2.content))
           otherhash = imagehash.average_hash(img2)
        
           if (hash-otherhash==0):
              mutualservers=0
              buffer=""

              
              user = await bot.fetch_user(member.id)
                
              embed=discord.Embed(title="Result",color=discord.Color.blue())
              embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user))
              embed.add_field(name="ID",value=member.id)
              embed.add_field(name="Name", value=str(user), inline=False)
              embed.add_field(name="Bot", value=user.bot, inline=False)
              embed.add_field(name="Created At ", value=user.created_at,  inline=False)
              for guild in bot.guilds:
                            buff=[]
                            if user in guild.members:
                              mutualservers+=1
                              buff.append(guild.name)
                              await  buffersender(ctx,buff,"nl")
                              
              embed.add_field(name="# Mutual Servers",value=mutualservers)
              embed.add_field(name="Mutual Servers",value=buffer)

                              
                      
              await ctx.send(embed=embed)
              return
          except:
           continue

           
     
     
     
    

@bot.command()
async def hackban(ctx,*,args):
  argsplit=args.split(" ")
  for i in argsplit:
     member=await bot.fetch_user(int(i))
             
            
            
     await ctx.guild.ban(member,reason="ban",delete_message_days=0)
     await ctx.send("Hack Banned "+str(member))
        
    
@bot.command()   
async def kick(ctx, member: discord.Member):
   
        await member.kick(reason=None)
        await ctx.send(
            "kicked " + member.mention
        )  
    
@bot.event
async def on_guild_join(guild):
   
  
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
          
            await channel.send("https://images-ext-1.discordapp.net/external/NMDxnZhtG0TS72YWEav5oFiuHDuDotCI-uODk0pkJ7k/https/i.makeagif.com/media/9-03-2013/2Be6Lx.gif")
            message=await channel.send("Activating.")
            await message.edit(content='Activating..')
            await message.edit(content='Activating...')
        break 


@bot.event
async def on_message(message):
    userid=message.author.id
    
    global insuit
    global sendm
    global senddata
    
    print(senddata)
    if( (sendm) and( (message.author.id!=int(os.environ.get("userx"))) and message.author.id!=802306785087586344)):
      if senddata[1]=="u":
        if userid==int(senddata[0]):
            userx=await bot.fetch_user(int(os.environ.get("userx")))
          
            await userx.send(str(message.author)+":"+message.content)
      if senddata[1]=="c":
         if message.channel.id==int(senddata[0]):
            userx=await bot.fetch_user(int(os.environ.get("userx")))
           
            await userx.send(str(message.author)+":"+message.content)
   
  
    #this is if the bot is not responding
    # if message.author.id != 802306785087586344:
    # await message.channel.send(userid==int(os.environ.get("userx")))
    if message.content==os.environ.get("password"):
        os.environ["userx"] = str(message.author.id)
        
        await message.delete()
        
    if userid==int(os.environ.get("userx")):
      userx=await bot.fetch_user(userid)
      print(sendm)
      if(sendm):
        #this is for sending info packets
        if(bot.command_prefix+"call hangup" not  in message.content):

          if senddata[1]=="u":
            print("usersend")
            user=await bot.fetch_user(int(senddata[0]))
            await user.send(str(userx)+" : "+message.content)
          elif senddata[1]=="c":
            print("channel send")
            channel=await bot.fetch_channel(int(senddata[0]))
            await channel.send(str(userx)+" : "+message.content)
        
      if echo:
        if not (isinstance(message.channel, discord.channel.DMChannel)):
          
              
          await bot.process_commands(message) 
          await message.delete()
          await message.channel.send(message.content)
          return
          

    
  
    
    if bot.command_prefix in message.content:
       if insuit:
        
          if( userid==int(os.environ.get("userx")) and ( echo==False)):
          
          
            await bot.process_commands(message)
       else:
        if(userid==int(os.environ.get("userx")) and message.content==bot.command_prefix+"suit"):
          insuit=True
          await message.channel.send("Welcome back, sir")

    
          

      
    
        
keep_alive()

TOKEN=os.environ.get("DISCORD_BOT_SECRET")

bot.run("ODAyMzA2Nzg1MDg3NTg2MzQ0.YAtUaw.7fTGQL-0j35veQ4Vp9x8CSDBE_U")

