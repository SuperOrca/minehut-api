from datetime import datetime

import requests

from .manager import ServerManager
from .plugin import Plugin

BASE_API_URL = "https://api.minehut.com"


class IllegalArgumentError(ValueError):
    pass


class Server:
    def __init__(self, name: str = None, id: str = None):
        if name is None:
            self.base_url = '{}/server/{}?byName=true'.format(BASE_API_URL, name)
        elif id is None:
            self.base_url = '{}/server/{}'.format(BASE_API_URL, id)
        else:
            raise IllegalArgumentError("Server does not exist.")

    def toJSON(self):
        data = requests.get(self.base_url).json()
        if 'ok' not in data:
            return data['server']
        else:
            raise IllegalArgumentError("Server does not exist.")

    def getServerProperties(self):
        return self.toJSON()['server_properties']

    def getPlugins(self):
        return [Plugin(id=indentifier) for indentifier in self.toJSON()['active_plugins']]

    def getId(self):
        return self.toJSON()['_id']

    def getMOTD(self):
        return self.toJSON()['motd']

    def isVisible(self):
        return self.toJSON()['visibility']

    def getServerPlan(self):
        return self.toJSON()['server_plan']

    def getName(self):
        return self.toJSON()['name']

    def getCreation(self):
        return self.toJSON()['creation']

    def getCreationDatetime(self):
        return datetime.fromtimestamp(self.toJSON()['creation'] / 1000.0)

    def getPlatform(self):
        return self.toJSON()['platform']

    def getCreditsPerDay(self):
        return self.toJSON()['credits_per_day']

    def getPort(self):
        return self.toJSON()['port']

    def getLastOnline(self):
        return self.toJSON()['last_online']

    def getLastOnlineDatetime(self):
        return datetime.fromtimestamp(self.toJSON()['last_online'] / 1000.0)

    def getIcon(self):
        data = self.toJSON()
        return data['icon'] if 'icon' in data else None

    def isOnline(self):
        return self.toJSON()['online']

    def getMaxPlayers(self):
        return self.toJSON()['maxPlayers']

    def getPlayerCount(self):
        return self.toJSON()['playerCount']

    def getPlayers(self):
        return self.toJSON()['players']

    def admin(self, credentials):
        return ServerManager(self, credentials)


def getServers():
    servers = []
    for server in requests.get('{}/servers'.format(BASE_API_URL)).json()['servers']:
        servers.append(Server(server['name']))
    return servers


def getServer(name: str):
    return Server(name)
