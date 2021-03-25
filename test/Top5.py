import minehut

if __name__ == '__main__':
    for server in minehut.getTop5():
        print(server.getName(), server.getPlayerCount())
