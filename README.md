# danbot-status
![travis-ci](https://travis-ci.com/VineyS/danbot-status-py.svg?branch=main)
[![CodeQL](https://github.com/VineyS/danbot-status-py/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/VineyS/danbot-status-py/actions/workflows/codeql-analysis.yml)
[![Upload Python Package](https://github.com/VineyS/danbot-status-py/actions/workflows/python-publish.yml/badge.svg)](https://github.com/VineyS/danbot-status-py/actions/workflows/python-publish.yml)

DanBot Status is a module built in python for getting all statistical services used by DanBotHost.
# Changelog
- v0.0.1: Initial release
- v0.0.2: Converted the module to a Asynchronous Package
- v0.1.1: Added Support for Synchronous and Asynchronous Programming 
- v0.2.0: Rewrote the module to use the new version of the API
- v0.2.1: Fixed some README mistakes

# Upgrade Module
`pip install --upgrade danbot-status`

# Installation
`pip install danbot-status`  --> For Windows

`pip3 install danbot-status`  -->   For Linux

# Usage 
`import danbotstatus`  --> Importing Module in Python

# Classes
danbotstatus.SynchronousState()  -->  For Synchronous Coding

danbotstatus.AsynchronousState()  -->  For Asynchronous Coding

# Errors
danbotstatus.APIError()  ->  Thrown when the API is not responding or is down

# Basic Example Of danbotstatus in Asynchronous Environment In Discord Bot (discord.py)

` This method needs the module discord.py `
```py
import discord
from danbotstatus import AsynchronousState()
dbs = AsynchronousState()
bot = discord.Client()

@bot.event
async def on_ready():
    print("Logged In as " + bot.user )
    
    
@bot.event
async def on_message(message):
    if message.content == 'check all node status':
        nodestats = await dbs.fetch_all()
        await message.channel.send(nodestats)
        
bot.run("TOKEN")
```
# Basic Example Of danbotstatus in Synchronous Environment In Flask (Flask)

` This method needs the module Flask `
```py
from flask import Flask
from danbotstatus import SynchronousState
dbs = SynchronousState()
app = Flask(__name__)

@app.route('/')
def index():
    return {'status': "alive"}
    
    
@app.route('/allstats')
def nodestats():
    ns = dbs.fetch_all()
    return ns
        
if __name__ == '__main__':
    app.run()
```
# Basic Functions in the module (SynchronousState)
*pssst, this is not an example , this just shows the functions the module has*
```py
from danbotstatus import SynchronousState
dbhs = danbotstatus.SynchronousState()
allnodestats = dbhs.fetch_all()   # Gets All Stats
time = dbhs.fetch_time()   # Gets the time of the API
names = dbhs.fetch_server_names()   # Gets the names of the nodes
stats = dbhs.fetch_server_stats("Server Name", 3)   # Gets the stats of the specific servers, Accepts 2 Optional Arguements, either the server name or the index positioning of the dictionary

print(allnodestats)  # This method returns a dictionary
print(time)  # This method returns a string
print(names)  # This method returns a list
print(stats)  # This method returns a dictionary
```
# Basic Functions in the module (AsynchronousState)
*pssst, this is not an example , this just shows the functions the module has*
```py
from danbotstatus import AsynchronousState
dbhs = AsynchronousState()
allnodestats = await dbhs.fetch_all()   # Gets All Stats
time = await dbhs.fetch_time()   # Gets the time of the API
names = await dbhs.fetch_server_names()   # Gets the names of the nodes
stats = await dbhs.fetch_server_stats("Server Name", 3)   # Gets the stats of the specific servers, Accepts 2 Optional Arguements, either the server name or the index positioning of the dictionary

print(allnodestats)  # This method returns a dictionary
print(time)  # This method returns a string
print(names)  # This method returns a list
print(stats)  # This method returns a dictionary
```
---

Thank You.

Module Built By Viney. Any Queries or Issue, feel free to make an Issue in the issue tab of Github. This project is welcome to receive any contributions by submitting in  PR's
