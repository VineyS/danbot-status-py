import requests
base = "https://danbot.host/nodeStatus"
sysinfo = 'https://danbot.host/sysinfo'
leaderboard = "https://api.danbot.host/leaderboard"
######################################
#####     GETTING ALL STATUS     #####
######################################

def getallstats():
    r = requests.get(base)
    if r.status_code == 200:
        return r.json()          ## RETURNS ALL STATUS IN DICTIONARY
    else:
        error = f"Error when fetching, please try again! Status Code : {r.status_code}"
        return error

######################################
####   GETTING ONLY NODE STATUS   ####
######################################

def getallnodestats():
    r = requests.get(base)
    if r.status_code == 200:
        nodestats = r.json()['nodestatus']
        return nodestats        #  RETURNS ONLY NODES STATUS IN FORM OF DICTIONARY
    else:
        error = f"Error when fetching, please try again! Status Code : {r.status_code}"
        return error
###############################################
######  GETTING A PARTICULAR NODE STATUS  #####
###############################################

def getnodestatus(val = None):
    if val is None:
        error = "Node number can't be of NoneType"
        return error

    else:
        r = requests.get(base)
        if r.status_code == 200:
            jsonify = r.json()['nodestatus']
            if int(val) == 0:
                error = "Node 0 wasn't found!"
                return error
            elif int(val) < 0:
                error = "Node number can't be a negative value!"
                return error
            elif int(val) > 0 and int(val) <= len(jsonify):
                result = jsonify[f"Node{val}"]
                return result                  # Returns Particular Node Status In Dictionary
        else:
            error = f"Error when fetching, please try again! Status Code : {r.status_code}"
            return error

##########################################
#####  GETTING MISC STATUS     ##########
##########################################

def getmiscstatus():
    r = requests.get(base)
    if r.status_code == 200:
        jsonify = r.json()['misc']
        return(jsonify)
    else:
        error = f"Error when fetching, please try again! Status Code : {r.status_code}"
        return error            # Returns Misc Status in form of Dictionary 

##########################################
#####  GETTING LAVA STATUS     ##########
##########################################

def getlavastatus(val = None):
    if val is None:
        error = "Node number can't be of NoneType"
        return error
    else:
        r = requests.get(base)
        if r.status_code == 200:
            jsonify = r.json()['misc']
            if int(val) == 0:
                error = "Lava0 wasn't found!"
                return error
            elif int(val) < 0:
                error = "Lava number can't be a negative value!"
                return error
            elif int(val) > 0 and int(val) <= len(jsonify):
                try:
                    result = jsonify[f'Lava{val}']
                except KeyError as e:
                    rerror = f"{e} was not found! "
                    return rerror   
                else:
                    return result   # Returns True, if its online
                
        else:
            error = f"Error when fetching, please try again! Status Code : {r.status_code}"
            return error
#############################################
####   GETTING ALL  SYSTEM INFORMATION   ####
#############################################

def getallsysinfo():
    r = requests.get(sysinfo)
    if r.status_code == 200:
        sysstats = r.json()
        return sysstats        #  RETURNS SYSTEM(NODE) INFORMATION STATUS IN FORM OF DICTIONARY
    else:
        error = f"Error when fetching, please try again! Status Code : {r.status_code}"
        return error


##############################################
#########  GETTING PARTICULAR SYS INFO #######
##############################################

def getsysinfo(val = None):
    if val is None:
        error = "Node number can't be of NoneType"
        return error
    else:
        r = requests.get(sysinfo)
        if r.status_code == 200:
            jsonify = r.json()
            if int(val) == 0:
                error = "Node 0 wasn't found!"
                return error
            elif int(val) < 0:
                error = "Node number can't be a negative value!"
                return error
            elif int(val) > 0 and int(val) <= len(jsonify):
                result = jsonify[f"Node{val}"]
                return result                  # Returns Particular Node Status In Dictionary
        else:
            error = f"Error when fetching, please try again! Status Code : {r.status_code}"
            return error

#############################################
#####    GETTING LEADERBOARD ################
#############################################
def getleaderboard():
    r = requests.get(leaderboard)
    if r.status_code == 200:
        result = r.json()
        return result  # Returns Leaderboard in list, where each list values are dictionary type
    else:
        error = f"Error when fetching, please try again! Status Code : {r.status_code}"
        return error

print(getleaderboard())


    

