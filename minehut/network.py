import requests

from .server import Server

BASE_API_URL = "https://api.minehut.com"


def getServerCap():
    data = requests.get('{}/network/simple_stats'.format(BASE_API_URL)).json()
    return data['server_max']


def getPlayerCount():
    data = requests.get('{}/network/simple_stats'.format(BASE_API_URL)).json()
    return data['player_count']


def getServerCount():
    data = requests.get('{}/network/simple_stats'.format(BASE_API_URL)).json()
    return data['server_count']


def getTop5():
    data = requests.get('{}/network/top_servers'.format(BASE_API_URL)).json()
    return [Server(server['name']) for server in data['servers']]
