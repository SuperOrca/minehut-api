import minehut

if __name__ == '__main__':
    for plugin in minehut.getPlugins():
        print(plugin.getName() + " | " + plugin.getDescription())
