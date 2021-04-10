from datetime import datetime

import requests

from .manager import ServerManager, Credentials
from .plugin import Plugin

BASE_API_URL = "https://api.minehut.com"


class IllegalArgumentError(ValueError):
    pass


class Server:
    def __init__(self, name: str = None, id: str = None):
        base_url = ''
        if name is not None:
            base_url = '{}/server/{}?byName=true'.format(BASE_API_URL, name)
        elif id is not None:
            base_url = '{}/server/{}'.format(BASE_API_URL, id)
        else:
            raise IllegalArgumentError("Server does not exist.")
        self.data = requests.get(base_url).json()
        if 'ok' not in data:
            return self
        else:
            raise IllegalArgumentError("Server does not exist.")

    def getServerProperties(self):
        return self.data['server_properties']

    def getPlugins(self):
        return [Plugin(id=indentifier) for indentifier in self.data['active_plugins']]

    def getId(self):
        return self.data['_id']

    def getMOTD(self):
        return self.data['motd']

    def isVisible(self):
        return self.data['visibility']

    def getServerPlan(self):
        return self.data['server_plan']

    def getName(self):
        return self.data['name']

    def getCreation(self):
        return self.data['creation']

    def getCreationDatetime(self):
        return datetime.fromtimestamp(self.data['creation'] / 1000.0)

    def getPlatform(self):
        return self.data['platform']

    def getCreditsPerDay(self):
        return self.data['credits_per_day']

    def getPort(self):
        return self.data['port']

    def getLastOnline(self):
        return self.data['last_online']

    def getLastOnlineDatetime(self):
        return datetime.fromtimestamp(self.data['last_online'] / 1000.0)

    def getIcon(self):
        return self.data['icon'] if 'icon' in self.data else None

    def isOnline(self):
        return self.data['online']

    def getMaxPlayers(self):
        return self.data['maxPlayers']

    def getPlayerCount(self):
        return self.data['playerCount']

    def getPlayers(self):
        return self.data['players']

    def admin(self, credentials: Credentials):
        return ServerManager(self.getId(), credentials)


def getServers():
    data = requests.get('{}/servers'.format(BASE_API_URL)).json()['servers']
    return [Server(server['name']) for server in data]


def getServer(name: str):
    return Server(name)
