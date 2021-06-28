# danbot-status

DanBot Status is a module built in python for getting all statistical services used by DanBotHost.

# Installation
`pip install danbot-status`  --> For Windows

`pip3 install danbot-status`  -->   For Linux

# Usage 
`import danbotstatus`  --> Importing Module in Python

# Basic Example In Discord Bot ( discord.py)

` This method needs the module discord.py `
```py
import discord
import danbotstatus as dbs
bot = discord.Client()

@bot.event
async def on_ready():
    print("Logged In as " + bot.user )
    
    
@bot.event
async def on_message(message):
    if message.content == 'check all node status':
        nodestats = await dbs.getallnodestats()
        await message.channel.send(nodestats)
        
bot.run("TOKEN")
```
# Basic Functions in the module
*pssst, this is not an example , this just shows the functions the module has*
```py
import danbotstatus as dbhs
allnodestats = await dbhs.getallnodestats()   # Gets All Node Status
allstats = await dbhs.getallstats()   # Gets All Status including nodestatus and misc
allawait sysinfo = await dbhs.getallsysinfo()   # Gets All Node System Informations
lavastats = await dbhs.getlavastatus(int)  #Gets a particular lava status, Replace int by number. For example: lavastats = dbhs.getlavastatus(1)  gives Lava1 information
misc = await dbhs.getmiscstatus()  # Gets misc status
leaderboard = await dbhs.leaderboard()  # Gets Leaderboard 
nodestats = await dbhs.getnodestatus(int) # Gets a particular node status
sysinfo = await dbhs.getsysinfo(int) # Gets a particular node information, Replace int by node number
print(allnodestats)   # Returns data in dictionary
print(allstats)        # Returns data in dictionary
print(allsysinfo)        # Returns data in dictionary
print(lavastats)         # Returns data in bool from --> True if its online, False if its offline
print(leaderboard)  #Returns data in list
print(nodestats)    # Returns data in dictionary
print(sysinfo) # Returns data in dictionary
```
---

Thank You.

Module Built By Viney. Any Queries or Issue, feel free to make an Issue in the issue tab of Github. This project is welcome to receive any contributions by submitting in  PR's
