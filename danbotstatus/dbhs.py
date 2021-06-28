import aiohttp
base = "https://danbot.host/nodeStatus"
sysinfo = 'https://danbot.host/sysinfo'
leaderboard = "https://api.danbot.host/leaderboard"


async def getallstats():
    """
    Fetches the basic json from base url, this method returns a dictionary
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(base) as resp:
            if resp.status == 200:
                return await resp.json()
            else:
                error = "Error when fetching, please try again! Status Code : " + str(resp.status)
                return error


async def getallnodestats():
    """
    Fetches the data related to nodes only, this method returns a dictionary
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(base) as resp:
            if resp.status == 200:
                cache = await resp.json()
                nodestats = cache['nodestatus']
                return nodestats
            else:
                error = "Error when fetching, please try again! Status Code : " + str(resp.status)
                return error


async def getnodestats(val=1):
    """
    Fetches a particular node statistics
    ...
    Parameters
    ----------
    val : An int value, by default its set to 1
    here, the node number has to be inputted. Example: getnodestats(2) returns data for Node 2
    """
    if isinstance(val, int) is False:
        raise ValueError("val parameter has to be integer only!")

    else:
        async with aiohttp.ClientSession() as session:
            async with session.get(base) as resp:
                if resp.status == 200:
                    cache = await resp.json()
                    nodestatus = cache['nodestatus']
                    if int(val) == 0:
                        error = "Node 0 wasn't found!"
                        raise error
                    elif int(val) < 0:
                        error = "Node number can't be a negative value!"
                        return ValueError(error)
                    elif int(val) > 0 and int(val) <= len(nodestatus):
                        result = nodestatus[f"Node{val}"]
                        return result                  # Returns Particular Node Status In Dictionary
                else:
                    error = "Error when fetching, please try again! Status Code : " + str(resp.status)
                    return error


async def getmiscstats():
    """
    Fetches miscellaneous statistics
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(base) as resp:
            if resp.status == 200:
                cache = await resp.json()
                misc = cache['misc']
                return(misc)
            else:
                error = "Error when fetching, please try again! Status Code : " + str(resp.status)
                return error


async def getlavastats(val=1):
    """
    Fetches a particular node statistics
    ...
    Parameters
    ----------
    val : An int value, by default its set to 1
    here, the lava node has to be inputted. Example: getlavastats(2) returns data for Node 2
    """
    if isinstance(val, int) is False:
        raise ValueError("val parameter has to be integer only!")

    else:
        async with aiohttp.ClientSession() as session:
            async with session.get(base) as resp:
                if resp.status == 200:
                    cache = await resp.json()
                    misc = cache['misc']
                    if int(val) == 0:
                        error = "Lava0 wasn't found!"
                        return error
                    elif int(val) < 0:
                        error = "Lava number can't be a negative value!"
                        return error
                    elif int(val) > 0 and int(val) <= len(misc):
                        try:
                            result = misc[f'Lava{val}']
                        except KeyError as e:
                            rerror = f"{e} was not found! "
                            return rerror
                        else:
                            return result   # Returns True, if its online

                else:
                    error = "Error when fetching, please try again! Status Code : " + str(resp.status)
                    return error


async def getallsysinfo():
    """
    Fetches system info details from the data
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(base) as resp:
            if resp.status == 200:
                sysstats = await resp.json()
                return sysstats
            else:
                error = "Error when fetching, please try again! Status Code : " + str(resp.status)
                return error


async def getsysinfo(val=1):
    """
    Fetches a system information about a node
    ...
    Parameters
    ----------
    val : An int value, by default its set to 1
    here, the node number has to be inputted. Example: getsysinfo(2) returns data for system of node 2
    """
    if isinstance(val, int) is False:
        raise ValueError("val parameter has to be integer only!")

    else:
        async with aiohttp.ClientSession() as session:
            async with session.get(base) as resp:
                if resp.status == 200:
                    cache = await resp.json()
                    if int(val) == 0:
                        error = "Node 0 wasn't  found!"
                        return error
                    elif int(val) < 0:
                        error = "Node number can't be a negative value!"
                        return error
                    elif int(val) > 0 and int(val) <= len(cache):
                        result = cache[f"Node{val}"]
                        return result

                else:
                    error = "Error when fetching, please try again! Status Code : " + str(resp.status)
                    return error


async def getleaderboard():
    """
    Fetches the leaderboard in list format
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(base) as resp:
            if resp.status == 200:
                result = await resp.json()
                return result

            else:
                error = "Error when fetching, please try again! Status Code : " + str(resp.status)
                return error
