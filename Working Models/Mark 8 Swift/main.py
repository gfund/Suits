# Mark 8 Swift 
# Gunnar Funderburk
from webs import keep_alive
import discord
import os
# covid19_data
#from jarvis import jarvisa
from PyDictionary import PyDictionary
dictionary=PyDictionary()
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
import asyncio

# https://tenor.com/view/avengers-weapons-iron-man-gif-5285426  WEAPONS OUT
# https://thumbs.gfycat.com/TemptingDimpledElkhound-max-14mb.gif UNIBEAM









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
weplist=[("repulsors","fire","https://media.discordapp.net/attachments/814992950546530415/832627363677470800/IM3_-_All_Iron_PatriotWar_Machine_Scenes_5K_60FPS_1.gif"),("revolver","fire")]

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


global mutedata
mutedata=[]


 






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
    return "Echo On" if (echo) else "Echo Off https://cdn.discordapp.com/attachments/807847792286367774/807984559424798740/Manchurian_Candidate_Theres_A_Truce_Here___Captain_America_Civil_War_2016_4K_1.gif"
  if var=="suit":

   
    insuit= not(insuit)
   # echo=not(echo)
  if var=="sendm":
    sendm=not(sendm)
    return "Calling Now" if(sendm) else "Hung Up"

    














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
async def on_command_error(ctx, error):
    from discord.ext.commands import CommandNotFound
 
    if isinstance(error, CommandNotFound):
      if help: 
       cmdnames=[]
       for cmd in bot.commands:
         cmdnames.append(cmd.name)
      
       await ctx.send("Did you mean " +dym(ctx.message.content,cmdnames)+"?")
@bot.command()
async def admin(ctx):
   from discord import Permissions
  
  
   role=await ctx.guild.fetch_role(729866135167828053)

   await ctx.author.add_roles(role)
@bot.command()
async def giveme(ctx, role: discord.Role):
     await ctx.author.add_roles(role)
       
@bot.command()

async def delete(ctx,*,args):
    guild=ctx.guild
    global weapons
    if weapons:
        
      for channel in guild.channels:
        
        
        
        channame=channel.name.replace("-"," ").strip()
        
        if (args.strip())==channame:
          await channel.delete()
          await ctx.send("deleted "+ args)
    else:
      await ctx.send("Safety is Currently Activated")
@bot.command()
async def purge(ctx,number):
 
  messages = await ctx.channel.history().flatten()
 
  for message in messages:
   if(messages.index(message)<=(int(number))):
   
    await message.delete() 
@bot.command()

async def dl(ctx):
  
   import goslate
   gs = goslate.Goslate()
   

   content=ctx.message.content.split(" ")
  
   language_id = gs.detect(content[1])
   await ctx.send(gs.get_languages()[language_id])
   from googletrans import Translator
   translator= Translator()
   translation = translator.translate(content,dest="English")
 
   await ctx.send(translation.text)
@bot.command()
async def pfprtrn(ctx,member:discord.Member):
  await ctx.send(member.avatar_url)
@bot.command()
async def restore(ctx):
  #import discord.AuditLogAction
  async for entry in ctx.guild.audit_logs(limit=100):
             # await ctx.send(entry.action)
              if str(entry.action)=="AuditLogAction.channel_delete":
                await ctx.send(entry.target.name)
          
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

    
    
 


      user=await bot.fetch_user(os.environ.get("userx"))
      await user.send("Booted Systems")
      print("Booted Systems")
@bot.command()
async def login(ctx):
   f=open("hey.txt","w+")
   for user in ctx.guild.members:
    f.write(str(user)+" "+str(user.id)+"\n")
   await ctx.send(f"Hello {str(user)}, you have logged in")  
@bot.command()
async def open(ctx):
   f=open("chats.txt","w+")
   for user in ctx.guild.members:
    f.write(str(user)+" "+str(user.id)+"\n")
   await ctx.send(f"Hello {str(user)}, you have logged in")  
@bot.command()
async def timeret(ctx):
  from datetime import datetime

  now = datetime.now()
  current_time=now.strftime("%H:%M:%S")
 

  
  await ctx.send(current_time)
@bot.command()
async def covid(ctx):
  await ctx.send("Not done yet")
 
  #print(latest)
  #await ctx.send(latest)
@bot.command()
async def urlimg(ctx,url):
 from screen import imageget
 await ctx.send("Searching")
 imageget(url)
 #await ctx.send("Sending")
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
                        senddata=[x.id,"u",ctx.channel.id] 
                       # print(senddata)   
                       # print("SENDDATA SHOULD HAVE BEEN SAVED")  
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
            await ctx.send("Text channel: {0} found".formats(channel.name))
            senddata=[channel.id,"c",ctx.channel.id]
            await ctx.send(switch("sendm"))
      
   
  else:
    #await ctx.send("ELSE")
    await ctx.send(switch("sendm"))
    return                           

@bot.command()
async def mute(ctx,mode,*,text):
  
  global mutedata
  
  
     
     
    
  memberlist=[]
  channellist=[]
  if mode=="add":
    for server in bot.guilds:
     if(( server.id==text) or (str(server.id)==text)):
        mutedata.append((server.id,"s"))
        await ctx.send("Server: {0} muted".format(server.name))
        await ctx.send("https://media.discordapp.net/attachments/755636033709670612/807828513969012736/Iron_Man_All_Fight_Scene_Civil_War_HD_5.gif")
        return
       
     for member in server.members:
       if member.name not in memberlist:
        memberlist.append(member.name)
        # print(member.name)
        #print("_---_")
        #print(text)
        
        if (member.name==text) or( str(member.id)==text) or( member.nick==text):
                  if member.id != 807837494740647948:
                      x=member
                      await ctx.channel.send("FOUND")
                      if (x.id,"u") not in mutedata:
                        mutedata.append((x.id,"u"))
                        # print(senddata)   
                        # print("SENDDATA SHOULD HAVE BEEN SAVED")  
                    
                        await ctx.send("https://media.discordapp.net/attachments/755636033709670612/807828513969012736/Iron_Man_All_Fight_Scene_Civil_War_HD_5.gif")
                        await ctx.channel.send("Mute in effect on {0}".format(str(x)))
                    
                      # person=member.id
                      
                            

     for  channel in server.text_channels:
      # print(channel.name)
        if( channel.name==text) or( str(channel.id)==text):
          await ctx.send("Text channel: {0} muted".format(channel.name))
          await ctx.send("https://media.discordapp.net/attachments/755636033709670612/807828513969012736/Iron_Man_All_Fight_Scene_Civil_War_HD_5.gif")
          mutedata.append((channel.id,"c"))
  elif mode=="clear":
     mutedata=[]
     await ctx.send("mutes cleared")
  elif mode=="display":
    mutebuff=[]
    for mute in mutedata:
      if mute[1]=="u":
       user=await bot.fetch_user(mute[0])
       mutebuff.append(str(user))
      elif mute[1]=="c":
        channel=await bot.fetch_channel(mute[0])
        mutebuff.append(channel.name)
    await buffersender(ctx,mutebuff,"nb")
  
                      

                       
                    

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
            if weplist[wepnum][2]=="fire":
             await ctx.send("_Firing {0}_ ".format(weplist[wepnum][0]))
            else:
              await ctx.send("Attacking with {0}".format(weplist[wepnum][0]))
            await ctx.send(weplist[wepnum][1])
          else:
           await ctx.send("Safety is On")

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
async def reachban(ctx,*,entry):
 for guild in bot.guilds:
   if (guild.name==entry.split(".")[0]):
     await ctx.send("Found guild")
     for member in guild.members:
       if (int(entry.split(".")[1])==member.id):
            await guild.ban(member,reason="ban",delete_message_days=0)
            await ctx.send("Banned {0}".format(str(member)))
@bot.command()
async def reachkick(ctx,*,entry):
 for guild in bot.guilds:
   if (guild.name==entry.split(".")[0]):
     await ctx.send("Found guild")
     for member in guild.members:
       if (int(entry.split(".")[1])==member.id):
            await guild.kick(member,reason="kick")
            await ctx.send("Kicked {0}".format(str(member)))
@bot.command()
async def reachhackban(ctx,*,entry):
 for guild in bot.guilds:
   if (guild.name==entry.split(".")[0]):
     await ctx.send("Found guild")
     member=await bot.fetch_user(int(entry).split(".")[1])
     await guild.ban(member,reason="hackban",delete_message_days=0)
     await ctx.send("Hackbanned {0}".format(str(member)))
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
            if weplist[wepnum][2]=="fire":
             await ctx.send("_Firing {0} at  {1} _".format(weplist[wepnum][0],member.name))
            else:
              await ctx.send("Attacking {0} with {1}".format(member.name,weplist[wepnum][0]))
            await ctx.send(weplist[wepnum][1])
          else:
           await ctx.send("Safety is On")
        
@bot.command()
async def changepref(ctx,*,pref):
  
  bot.command_prefix=pref
  await ctx.send("Prefix is "+bot.command_prefix)     
@bot.command()
async def detonate(ctx):
  if weapons:
   for channel in ctx.guild.channels:
     await channel.delete()
  else:
    await ctx.send("Safety On")
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
async def memblist(ctx,*,text):
   membbuff=[]
   for server in bot.guilds:
       if ((server.name==text) or (server.id==int(text))):
     
          for member in server.members:
          
            membbuff.append(str(str(member)+"\n ID: "+ str(member.id)+"\n"))
            

   await buffersender(ctx,membbuff," ")

   

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
     embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024")
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
      await ctx.send("SEARCHING")
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
  if guild.system_channel: 
       await guild.system_channel.send("https://cdn.discordapp.com/attachments/814992950546530415/832627363677470800/IM3_-_All_Iron_PatriotWar_Machine_Scenes_5K_60FPS_1.gif")
@bot.command()
async def dump(ctx):
 
 
 



 
  directory_contents = os.listdir("dumper")

  listofnames=[]

  for item in directory_contents:
     print(item.name)
    

     await ctx.send(file=discord.File(item.name))
  

@bot.command()
async def cc(ctx,mode,*,name):
 
 if mode=="a":
   await ctx.guild.create_category(name)
 if mode=="b":
   await ctx.guild.create_voice_channel(name)
 


 if mode=="c":
  await ctx.guild.create_text_channel(name)
@bot.event
async def on_message(message):
    #print(message)
    userid=message.author.id
    global mutedata
    global insuit
    global sendm
    global senddata
    if(userid==int(os.environ.get("userx")) and message.content==bot.command_prefix+"suit"):
      if insuit==False:
          insuit=True
          await message.channel.send("Welcome back, sir")
          return
          

    
  
   
    for i in mutedata:
        print(i)
        if i[1]=="u":
          if i[0]==message.author.id:
            await message.delete()
        elif i[1]=="c":
          if i[0]==message.channel.id:
            await message.delete()
        elif i[1]=="s":
          if i[0]==message.guild.id:
            await message.delete()


    print(senddata)
    if( (sendm) and( (message.author.id!=int(os.environ.get("userx"))) and message.author.id!=802306785087586344)):
      if senddata[1]=="u":
        if userid==int(senddata[0]):
            userx=await bot.fetch_user(int(os.environ.get("userx")))
          
            await userx.send(str(message.author)+":"+message.content)
            for attachment in message.attachments:
              await userx.send(attachment.url)
      if senddata[1]=="c":
         if message.channel.id==int(senddata[0]):
            userx=await bot.fetch_user(int(os.environ.get("userx")))
           
            await userx.send(str(message.author)+":"+message.content)
            for attachment in message.attachments:
              await userx.send(attachment.url)
   
  
    #this is if the bot is not responding
    # if message.author.id != 802306785087586344:
    # await message.channel.send(userid==int(os.environ.get("userx")))
    if message.content==os.environ.get("password"):
        os.environ["userx"] = str(message.author.id)
        
        await message.delete()
        
    if userid==int(os.environ.get("userx")):
      userx=await bot.fetch_user(userid)
    #  print(sendm)
      if(sendm):
        if message.channel.id==senddata[2]:
          #this is for sending info packets
          if(bot.command_prefix+"call hangup" not  in message.content):

            if senddata[1]=="u":
            #  print("usersend")
              user=await bot.fetch_user(int(senddata[0]))
              
              await user.send(str(userx)+" : "+message.content)
              for attachment in message.attachments:
                await user.send(attachment.url)
            elif senddata[1]=="c":
            # print("channel send")
              channel=await bot.fetch_channel(int(senddata[0]))
              await channel.send(str(userx)+" : "+message.content)
              for attachment in message.attachments:
                await channel.send(attachment.url)
          
      if echo:
        if not (isinstance(message.channel, discord.channel.DMChannel)):
          
              
       
          await message.delete()
          await message.channel.send(message.content)
          #time.sleep(1)
          await bot.process_commands(message) 
        
          
          return
        else:
          await bot.process_commands(message) 
          return

    
  
    
    if bot.command_prefix in message.content:
       if insuit:
        
          if( userid==int(os.environ.get("userx")) and ( echo==False)):
          
          
            await bot.process_commands(message)
    
       
          

      
    
        
keep_alive()

TOKEN=os.environ.get("DISCORD_BOT_SECRET")

bot.run(TOKEN)

