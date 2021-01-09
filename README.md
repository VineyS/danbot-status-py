# danbot-status

DanBot Status is a module built in python for getting all statistical services used by DanBotHost.

# Installation
`pip install danbot-status`  --> For Windows

`pip3 install danbot-status`  -->   For Linux

# Usage 
`from danbotstatus import dbhs`  --> Importing Module in Python

# Basic Example

```py
from danbotstatus import dbhs
allnodestats = dbhs.getallnodestats()   # Gets All Node Status
allstats = dbhs.getallstats()   # Gets All Status including nodestatus and misc
allsysinfo = dbhs.getallsysinfo()   # Gets All Node System Informations
lavastats = dbhs.getlavastatus(int)  #Gets a particular lava status, Replace int by number. For example: lavastats = dbhs.getlavastatus(1)  gives Lava1 information
misc = dbhs.getmiscstatus()  # Gets misc status
leaderboard = dbhs.leaderboard()  # Gets Leaderboard 
nodestats = dbhs.getnodestatus(int) # Gets a particular node status
sysinfo = dbhs.getsysinfo(int) # Gets a particular node information, Replace int by node number


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

Module Built By Viney. Any Queries or Issue, feel free to make an Issue in the issue tab of Github.


