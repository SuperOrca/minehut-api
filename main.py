import minehut

if __name__ == '__main__':

    for plugin in minehut.getPlugins():
        if '2019' in str(plugin.getLastUpdatedDatetime()):
            print(plugin.getName(), plugin.getLastUpdatedDatetime())
