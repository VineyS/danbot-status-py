import aiohttp

class AsynchronousStatus:
    def __init__(self):
        self.base = "https://danbot.host/nodeStatus"
        self.sysinfo = 'https://danbot.host/sysinfo'
        self.leaderboard = "https://api.danbot.host/leaderboard"

    async def getallstats(self):
        """
        Fetches the basic json from base url, this method returns a dictionary
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base) as resp:
                if resp.status == 200:
                    return await resp.json()
                else:
                    error = "Error when fetching, please try again! Status Code : " + str(resp.status)
                    return error


    async def getallnodestats(self):
        """
        Fetches the data related to nodes only, this method returns a dictionary
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base) as resp:
                if resp.status == 200:
                    cache = await resp.json()
                    nodestats = cache['nodestatus']
                    return nodestats
                else:
                    error = "Error when fetching, please try again! Status Code : " + str(resp.status)
                    return error


    async def getnodestats(self, val=1):
        """
        Fetches a particular node statistics
        ...
        Parameters
        ----------
        val : An int value, by default its set to 1
        here, the node number has to be passed. Example: getnodestats(2) returns data for Node 2
        """
        if isinstance(val, int) is False:
            raise ValueError("val parameter has to be integer only!")

        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.base) as resp:
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
                            result = nodestatus["Node" + str(val)]
                            return result                  # Returns Particular Node Status In Dictionary
                    else:
                        error = "Error when fetching, please try again! Status Code : " + str(resp.status)
                        return error


    async def getmiscstats(self):
        """
        Fetches miscellaneous statistics
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base) as resp:
                if resp.status == 200:
                    cache = await resp.json()
                    misc = cache['misc']
                    return(misc)
                else:
                    error = "Error when fetching, please try again! Status Code : " + str(resp.status)
                    return error


    async def getlavastats(self, val=1):
        """
        Fetches a particular node statistics
        ...
        Parameters
        ----------
        val : An int value, by default its set to 1
        here, the lava node has to be passed. Example: getlavastats(2) returns data for Node 2
        """
        if isinstance(val, int) is False:
            raise ValueError("val parameter has to be integer only!")

        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.base) as resp:
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
                                result = misc['Lava' + str(val)]
                            except KeyError as e:
                                rerror = f"{e} was not found! "
                                return rerror
                            else:
                                return result   # Returns True, if its online

                    else:
                        error = "Error when fetching, please try again! Status Code : " + str(resp.status)
                        return error


    async def getallsysinfo(self):
        """
        Fetches system info details from the data
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base) as resp:
                if resp.status == 200:
                    sysstats = await resp.json()
                    return sysstats
                else:
                    error = "Error when fetching, please try again! Status Code : " + str(resp.status)
                    return error


    async def getsysinfo(self, val=1):
        """
        Fetches a system information about a node
        ...
        Parameters
        ----------
        val : An int value, by default its set to 1
        here, the node number has to be passed. Example: getsysinfo(2) returns data for system of node 2
        """
        if isinstance(val, int) is False:
            raise ValueError("val parameter has to be integer only!")

        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.base) as resp:
                    if resp.status == 200:
                        cache = await resp.json()
                        if int(val) == 0:
                            error = "Node 0 wasn't  found!"
                            return error
                        elif int(val) < 0:
                            error = "Node number can't be a negative value!"
                            return error
                        elif int(val) > 0 and int(val) <= len(cache):
                            result = cache["Node"+ str(val)]
                            return result

                    else:
                        error = "Error when fetching, please try again! Status Code : " + str(resp.status)
                        return error


    async def getleaderboard(self):
        """
        Fetches the leaderboard in list format
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base) as resp:
                if resp.status == 200:
                    result = await resp.json()
                    return result

                else:
                    error = "Error when fetching, please try again! Status Code : " + str(resp.status)
                    return error
