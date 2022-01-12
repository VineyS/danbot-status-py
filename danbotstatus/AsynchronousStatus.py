import aiohttp
from .errors import *


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
                    try:
                        cache = resp.json()
                    except Exception:
                        raise APIError("Incorrect JSON format! Perhaps the API Structure has changed!")
                    else:
                        return cache
                else:
                    raise APIError("Danbot API is down! A Status Code of" + str(resp.status) + " was returned!")


    async def getallnodestats(self):
        """
        Fetches the data related to nodes only, this method returns a dictionary
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base) as resp:
                if resp.status == 200:
                    try:
                        cache = await resp.json()
                    except Exception:
                        raise APIError("Incorrect JSON format! Perhaps the API Structure has changed!")
                    else:
                        nodestats = cache['nodestatus']
                        return nodestats
                else:
                    raise APIError("Danbot API is down! A Status Code of" + str(resp.status) + " was returned!")


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
                        try:
                            cache = await resp.json()
                        except Exception:
                            raise APIError("Incorrect JSON format! Perhaps the API Structure has changed!")
                        else:
                            nodestatus = cache['nodestatus']
                            if int(val) == 0:
                                raise NodeError("Node0 wasn't found!")
                            elif int(val) < 0:
                                raise NodeNegativeError("Node number can't be a negative value!")
                            elif int(val) > 0 and int(val) <= len(nodestatus):
                                result = nodestatus["Node" + str(val)]
                                return result                  # Returns Particular Node Status In Dictionary
                            else:
                                raise NodeError("Node" + str(val) + " wasn't found!")
                    else:
                        raise APIError("Danbot API is down! A Status Code of" + str(resp.status) + " was returned!")


    async def getmiscstats(self):
        """
        Fetches miscellaneous statistics
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base) as resp:
                if resp.status == 200:
                    try:
                        cache = await resp.json()
                    except Exception:
                        raise APIError("Incorrect JSON format! Perhaps the API Structure has changed!")
                    else:
                        misc = cache['misc']
                        return misc
                else:
                    raise APIError("Danbot API is down! A Status Code of" + str(resp.status) + " was returned!")


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
                        try:
                            cache = await resp.json()
                        except Exception:
                            raise APIError("Incorrect JSON format! Perhaps the API Structure has changed!")
                        else:
                            misc = cache['misc']
                            if int(val) == 0:
                                raise LavaError("Lava Node 0 wasn't found!")
                            elif int(val) < 0:
                                raise LavaNegativeError("Lava Node number can't be a negative value!")
                            elif int(val) > 0 and int(val) <= len(misc):
                                try:
                                    result = misc['Lava' + str(val)]
                                except KeyError as e:
                                    raise LavaError("Lava Node" + str(val) + " wasn't found!")
                                else:
                                    return result   # Returns True, if its online
                            else:
                                raise LavaError("Lava Node" + str(val) + " wasn't found!")

                    else:
                        raise APIError("Danbot API is down! A Status Code of" + str(resp.status) + " was returned!")


    async def getallsysinfo(self):
        """
        Fetches system info details from the data
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base) as resp:
                if resp.status == 200:
                    try:
                        sysstats = await resp.json()
                    except Exception:
                        raise APIError("Incorrect JSON format! Perhaps the API Structure has changed!")
                    else:
                        return sysstats
                else:
                    raise APIError("Danbot API is down! A Status Code of" + str(resp.status) + " was returned!")


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
                        try:
                            cache = await resp.json()
                        except Exception:
                            raise APIError("Incorrect JSON format! Perhaps the API Structure has changed!")
                        else:
                            if int(val) == 0:
                                raise NodeError("Node 0 wasn't found!")
                            elif int(val) < 0:
                                raise NodeNegativeError("Node number can't be a negative value!")
                            elif int(val) > 0 and int(val) <= len(cache):
                                result = cache["Node"+ str(val)]
                                return result
                            else:
                                raise NodeError("Node" + str(val) + " wasn't found!")

                    else:
                        raise APIError("Danbot API is down! A Status Code of" + str(resp.status) + " was returned!")


    async def getleaderboard(self):
        """
        Fetches the leaderboard in list format
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base) as resp:
                if resp.status == 200:
                    try:
                        result = await resp.json()
                    except Exception:
                        raise APIError("Incorrect JSON format! Perhaps the API Structure has changed!")
                    else:
                        return result

                else:
                    raise APIError("Danbot API is down! A Status Code of" + str(resp.status) + " was returned!")