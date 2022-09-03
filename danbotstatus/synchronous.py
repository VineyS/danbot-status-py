import requests
try:
    from .errors import APIError
except ImportError:
    from errors import APIError


class SynchronousState:
    """
    A Base Class For Handling Danbot API Requests Synchronously
    """
    def __init__(self):
        self.base = "https://status.danbot.host/json/stats.json"

    def fetch_all(self):
        """
        Fetches the basic json from base url, this method returns a dictionary
        """
        try:
            res = requests.get(self.base)
        except Exception as exc:
            raise APIError(exc) from exc
        else:
            if res.status_code == 200:
                return res.json()
            raise APIError("Danbot API is down! Code " + str(res.status_code) + " was returned!")

    def fetch_time(self):
        """
        Fetches the UNIX EPOCH of the last update

        returns a string
        """
        try:
            res = requests.get(self.base)
        except Exception as exc:
            raise APIError(exc) from exc
        else:
            if res.status_code == 200:
                return res.json()['updated']
            raise APIError("Danbot API is down! Code " + str(res.status_code) + " was returned!")

    def fetch_server_names(self):
        """
        Fetches the server names, this method returns a list of server names
        """
        try:
            res = requests.get(self.base)
        except Exception as exc:
            raise APIError(exc) from exc
        else:
            if res.status_code == 200:
                names = [ i["name"] for i in res.json()['servers'] ]
                return names
            raise APIError("Danbot API is down! Code " + str(res.status_code) + " was returned!")

    def fetch_server_stats(self, server_name : str = None, index : int = 0 ):
        """
        Fetches a specific server's stats either with server_name or by its positioning within the list of servers, this method returns a dictionary
        """
        if isinstance(server_name, str) is False :
            raise ValueError("server_name parameter has to be string only!")

        if (isinstance(server_name, str) is True) and (isinstance(index, int) is True):
            raise ValueError("Only one parameter can be passed at a time!")

        if isinstance(index, int) is False:
            raise ValueError("index parameter has to be integer only!")

        try:
            res = requests.get(self.base)
        except Exception as exc:
            raise APIError(exc) from exc
        else:
            if res.status_code == 200:
                if server_name is not None:
                    for i in res.json()['servers']:
                        if i['name'] == server_name:
                            return i
                elif index is not None:
                    return res.json()['servers'][index]
            else:
                raise APIError("Danbot API is down! Code " + str(res.status_code) + " was returned!")
