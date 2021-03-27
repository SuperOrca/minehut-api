from datetime import datetime

import requests

from .manager import ServerManager, Credentials
from .plugin import Plugin

BASE_API_URL = "https://api.minehut.com"


class IllegalArgumentError(ValueError):
    pass


class Server:
    def __init__(self, name: str = None, id: str = None):
        if name is not None:
            self.base_url = '{}/server/{}?byName=true'.format(BASE_API_URL, name)
        elif id is not None:
            self.base_url = '{}/server/{}'.format(BASE_API_URL, id)
        else:
            raise IllegalArgumentError("Server does not exist.")

    def getData(self):
        data = requests.get(self.base_url).json()
        if 'ok' not in data:
            return data['server']
        else:
            raise IllegalArgumentError("Server does not exist.")

    def getServerProperties(self):
        return self.getData()['server_properties']

    def getPlugins(self):
        return [Plugin(id=indentifier) for indentifier in self.getData()['active_plugins']]

    def getId(self):
        return self.getData()['_id']

    def getMOTD(self):
        return self.getData()['motd']

    def isVisible(self):
        return self.getData()['visibility']

    def getServerPlan(self):
        return self.getData()['server_plan']

    def getName(self):
        return self.getData()['name']

    def getCreation(self):
        return self.getData()['creation']

    def getCreationDatetime(self):
        return datetime.fromtimestamp(self.getData()['creation'] / 1000.0)

    def getPlatform(self):
        return self.getData()['platform']

    def getCreditsPerDay(self):
        return self.getData()['credits_per_day']

    def getPort(self):
        return self.getData()['port']

    def getLastOnline(self):
        return self.getData()['last_online']

    def getLastOnlineDatetime(self):
        return datetime.fromtimestamp(self.getData()['last_online'] / 1000.0)

    def getIcon(self):
        data = self.getData()
        return data['icon'] if 'icon' in data else None

    def isOnline(self):
        return self.getData()['online']

    def getMaxPlayers(self):
        return self.getData()['maxPlayers']

    def getPlayerCount(self):
        return self.getData()['playerCount']

    def getPlayers(self):
        return self.getData()['players']

    def admin(self, credentials: Credentials):
        return ServerManager(self.getId(), credentials)


def getServers():
    data = requests.get('{}/servers'.format(BASE_API_URL)).json()['servers']
    return [Server(server['name']) for server in data]


def getServer(name: str):
    return Server(name)
