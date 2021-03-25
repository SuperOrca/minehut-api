import requests

from .Plugin import Plugin
from .Server import Server

PLUGINS = requests.get('https://api.minehut.com/plugins_public').json()['all']
PLUGIN_LIST = [Plugin(id=plugin['_id']) for plugin in PLUGINS]


def getServers():
    servers = []
    for server in requests.get('https://api.minehut.com/servers').json()['servers']:
        servers.append(Server(server['name']))
    return servers


def getPlugins():
    return PLUGIN_LIST


def getServer(name):
    return Server(name)


def getPlugin(name):
    return Plugin(name)
