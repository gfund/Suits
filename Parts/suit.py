#Suit Basics Controller V1
#needed to manipulate files
import json
#discord classes
import discord
#Firebase imports
import firebase_admin
from firebase_admin import credentials, db

#Suit class to define common variables and suit functions
class Suit:
    suituser = 0
    prefix = ""
    weapons = False
    state = None
    entrygif = ""
    cogs = []
    botvar = None
    datab = None

    def load(self, bot, filename="suitvar.json"):
        #open json file
        suitsettings = open(filename)
        #load json file
        settings = json.load(suitsettings)
        #get userid of suituser
        self.suituser = int(settings['suituser'])
        #get bot prefix
        self.prefix = settings['prefix']
        #get weapon boolean
        self.weapons = settings['weapons']
        #get and set suit state
        state = SuitState()
        self.state = state.loadstate(settings['state'])
        #get entry gif
        self.entrygif = settings['entrygif']
        #get cogs for loading
        self.cogs = settings['cogs']
        #passing bot to botvar
        self.botvar = bot
        #set the prefix
        self.botvar.command_prefix = self.prefix
        #load db
        credfile, dburl = settings['dbdata']
        self.datab = Database(credfile, dburl)

        #load suit cogs
        for cog in self.cogs:
            try:
                #load cog by cog
                bot.load_extension(f"Cogs.{cog}")
            except Exception as e:
                #print exception if the cog file has an error
                print(e)

    #do entry function
    async def entry(self, guild):
        #check if there is a guild system channel to send gif too
        if guild.system_channel:
            await guild.system_channel.send(file=discord.File(self.entrygif))

    #send message text to user
    #messagetxt: text input
    #mode:format of input
    async def usersend(self, messagetext, mode="text"):

        user = await self.botvar.fetch_user(self.suituser)

        if (mode == "text"):

            await user.send(messagetext)
        if (mode == "file"):
            await user.send(file=discord.File(messagetext))

#Suit State 
class SuitState:
    name = ""
    variablesset = {}
    triggers = {}

    def loadstate(self, jsonin):
        state = jsonin.split(" ")
        self.name = state[0]
        self.variablesset = {}
        self.triggers = {}

#Database Class
class Database:
    url = ""
    credfile = ""
    dbobj = None
     #initialze the db from the credential file and the url 
    def __init__(self, credfile, url):

        cred = credentials.Certificate(credfile)

        firebase_admin.initialize_app(cred, {'databaseURL': url})

        self.dbobj = db
    #IO operations
    #path database path to read or write too
    #mode read or write Defaults to read
    #writearg Optional what to write, if nothing written does not need to be sent
    def io(self, path, mode="r", *writearg):

        if (mode == "r"):

            ref = self.dbobj.reference(path)
            data = ref.get()
            return data
        elif (mode == "w"):
            ref = self.dbobj.reference(path)
            ref.set(writearg)
#Suit Basics Controller V1
#needed to manipulate files
import json
#discord classes
import discord
#Firebase imports
import firebase_admin
from firebase_admin import credentials, db

#Suit class to define common variables and suit functions
class Suit:
    suituser = 0
    prefix = ""
    weapons = False
    state = None
    entrygif = ""
    cogs = []
    botvar = None
    datab = None

    def load(self, bot, filename="suitvar.json"):
        #open json file
        suitsettings = open(filename)
        #load json file
        settings = json.load(suitsettings)
        #get userid of suituser
        self.suituser = int(settings['suituser'])
        #get bot prefix
        self.prefix = settings['prefix']
        #get weapon boolean
        self.weapons = settings['weapons']
        #get and set suit state
        state = SuitState()
        self.state = state.loadstate(settings['state'])
        #get entry gif
        self.entrygif = settings['entrygif']
        #get cogs for loading
        self.cogs = settings['cogs']
        #passing bot to botvar
        self.botvar = bot
        #set the prefix
        self.botvar.command_prefix = self.prefix
        #load db
        credfile, dburl = settings['dbdata']
        self.datab = Database(credfile, dburl)

        #load suit cogs
        for cog in self.cogs:
            try:
                #load cog by cog
                bot.load_extension(f"Cogs.{cog}")
            except Exception as e:
                #print exception if the cog file has an error
                print(e)

    #do entry function
    async def entry(self, guild):
        #check if there is a guild system channel to send gif too
        if guild.system_channel:
            await guild.system_channel.send(file=discord.File(self.entrygif))

    #send message text to user
    #messagetxt: text input
    #mode:format of input
    async def usersend(self, messagetext, mode="text"):

        user = await self.botvar.fetch_user(self.suituser)

        if (mode == "text"):

            await user.send(messagetext)
        if (mode == "file"):
            await user.send(file=discord.File(messagetext))

#Suit State 
class SuitState:
    name = ""
    variablesset = {}
    triggers = {}

    def loadstate(self, jsonin):
        state = jsonin.split(" ")
        self.name = state[0]
        self.variablesset = {}
        self.triggers = {}

#Database Class
class Database:
    url = ""
    credfile = ""
    dbobj = None
     #initialze the db from the credential file and the url 
    def __init__(self, credfile, url):

        cred = credentials.Certificate(credfile)

        firebase_admin.initialize_app(cred, {'databaseURL': url})

        self.dbobj = db
    #IO operations
    #path database path to read or write too
    #mode read or write Defaults to read
    #writearg Optional what to write, if nothing written does not need to be sent
    def io(self, path, mode="r", *writearg):

        if (mode == "r"):

            ref = self.dbobj.reference(path)
            data = ref.get()
            return data
        elif (mode == "w"):
            ref = self.dbobj.reference(path)
            ref.set(writearg)
