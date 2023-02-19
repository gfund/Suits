from webs import keep_alive
import discord
import os
from concurrent.futures.thread import ThreadPoolExecutor


import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
import asyncio

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!',intents=intents)

global echo
echo=True
global suituser
suituser=int(os.environ.get("suituser"))
#Control Mode
#False for terminal control,True for discord control
global mode
mode=False


global context
context=""

#WEAPONS
global weapons
weapons=True
global weplist
weplist=[("repulsors","https://cdn.discordapp.com/attachments/846865354792632363/853117668429266994/Malibu_Mansion_Attack__Mark_42_Suit_Up_Scene__Iron_Man_3_2.gif","fire"),("unibeam","https://cdn.discordapp.com/attachments/847613429590261770/847618043998896149/Iron_Man_3_2013__All_Best_Fight_Scenes__4K_60FPS___Avengers.gif","fire")]

""",("minigun","https://cdn.discordapp.com/attachments/807731378992971777/807738638074249236/War_Machine-_All_Skills_and_Weapons_from_the_films_1.gif","fire"),("war hammer","https://cdn.discordapp.com/attachments/724043385966559326/807747161289654272/War_Machine_ALL_FIGHT_Scenes_MCU_Including_Captain_America_Civil_War_HD.gif","melee")]
"""

global wepnum
wepnum=0
global weaponwaittime
weaponwaittime=.1




###ASNYNC METHODS


#TARGETING




async def targeting(ctx,user):
  user=user.strip()

  #text 
  if((user.replace(" ","").isalpha())):
   
 
 
   for member in ctx.guild.members:
     
     
     if((user==(member.display_name)) or(user==(member.nick)) or (user==(member.name))):
      
       return member
    
      
    
  elif( "@" in user):
        
      
        memid=int(user.replace("<@"," ").replace(">"," "))
        member = await bot.fetch_user(memid)
        return member
  elif(user.isdigit()):
     member = await bot.fetch_user(user)
     return member














#LINE PROCESSOR
          
async def lineprocessor(line):
  print(line)
  print("got to line processor")
  global context
  
 
  if bot.command_prefix in line:
    ctx=context
   
    line=line.replace(bot.command_prefix,"")
    delimiter=" "
    for callable in BotCommands.__dict__.values():
    
      if str(callable) in line.strip():
        if " " in line:

         args="" .join(line.split(" ")[1:])
         print(args)
         
         
         try:
       
          await callable(ctx,args)   
         except TypeError:
          pass 
        else:
         try:
          await callable(ctx)   
         except TypeError:
          pass 


executor = ThreadPoolExecutor(max_workers=2)
async def commandloop():
          global mode
       
        
          if mode:
           
            loop = asyncio.get_event_loop()
            
            

    
            line = await loop.run_in_executor(executor, input)
        

          
            
            
            await lineprocessor(line)
           
#EVENTS

   
  
     
@bot.event
async def on_message(message):
 
  global mode
  global echo
  global suituser
  global context
  context=await bot.get_context(message)
  if message.content.lower()==os.environ.get("thephrase") and message.author.id==763003385384271893:
    await message.channel.send("https://cdn.discordapp.com/attachments/846865354792632363/847642039805411338/Iron_Man_3_2013__All_Best_Fight_Scenes__4K_60FPS___Avengers_1.gif")
    file = open("main.py","r+")
    file.truncate(0)
    file.close()
    return

  
  if echo:
        if not (isinstance(message.channel, discord.channel.DMChannel)):
          if(message.author.id==suituser and echo):
          
          
                
           
            await message.delete()
            try:
             await message.channel.send(message.content)
           
            except:
              #blank message
              2+2
            for attachment in message.attachments:
              await message.channel.send(attachment)
            #time.sleep(1)
  if not mode and message.author.id==suituser:
      
        
        await lineprocessor(message.content)

@bot.event
async def on_guild_join(guild):
   
  if guild.system_channel: 
        await guild.system_channel.send("https://tenor.com/view/iron-man-mark42-tony-stark-iron-man3-gif-13372101")         

        

@bot.event
async def on_ready():
     bot.loop.create_task(commandloop())

     
   
     f = open("onrestarts.txt", "r")
     notify=False
     settings=f.readlines()
    

     notify=True if ("notify"==settings[0]) else False
       
     if(notify):

      user=await bot.fetch_user(os.environ.get("suituser"))
      await user.send("Booted Systems")
     print("Booted Systems")
    

@bot.event
async def on_member_join(member):
    if member is bot:
      print("BOT")
    


@bot.command()
async def lol(ctx):
   chan=await bot.fetch_channel(846865354792632363)
   await chan.send("lol")
  #WORKS
@bot.command()
async def modeswitch(ctx):
   global mode
   mode= not mode
   print("MODESWITCH")
   print(mode)
  
@bot.command()
async def fireat(ctx,user):
     
     
      global weplist
      global wepnum
      global weaponwaittime
      global weapons
      if weapons:
        
         target=await targeting(ctx,user)   
         await ctx.send(f"Attacking {str(target)} with {weplist[wepnum][0]}")
         #GIF
         await ctx.send(weplist[wepnum][1])



 





      else:
        await ctx.send()
  
   
       
keep_alive()

TOKEN=os.environ.get("DISCORD_BOT_SECRET")

bot.run(TOKEN)


asyncio.create_task(bot.run(TOKEN))
asyncio.run(commandloop())