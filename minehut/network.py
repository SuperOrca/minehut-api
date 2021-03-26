import requests

from server import Server


def getServerCap():
    data = requests.get('https://api.minehut.com/network/simple_stats').json()
    return data['server_max']


def getPlayerCount():
    data = requests.get('https://api.minehut.com/network/simple_stats').json()
    return data['player_count']


def getServerCount():
    data = requests.get('https://api.minehut.com/network/simple_stats').json()
    return data['server_count']


def getTop5():
    servers = []
    data = requests.get('https://api.minehut.com/network/top_servers').json()
    for server in data['servers']:
        servers.append(Server(server['name']))
    return servers
