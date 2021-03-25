from datetime import datetime

import requests

PLUGINS = requests.get('https://api.minehut.com/plugins_public').json()['all']


class IllegalArgumentError(ValueError):
    pass


class Plugin(object):
    def __init__(self, name=None, id=None):
        if name is None and id is None:
            raise IllegalArgumentError("Plugin does not exist.")
        else:
            self.data = None
            for plugin in PLUGINS:
                if id == plugin['_id']:
                    self.data = plugin
                    break
                elif name == plugin['name']:
                    self.data = plugin
                    break
            if self.data is None:
                raise IllegalArgumentError("Plugin does not exist.")

    def getId(self):
        return self.data['_id']

    def getName(self):
        return self.data['name']

    def getPlatform(self):
        return self.data['platform']

    def getDescription(self):
        return self.data['desc']

    def getLongDescription(self):
        return self.data['desc_extended']

    def getLongDescriptionHTML(self):
        return self.data['html_desc_extended']

    def getVersion(self):
        return self.data['version']

    def isDisabled(self):
        return self.data['disabled']

    def getCreated(self):
        return self.data['created']

    def getCreatedDatetime(self):
        return datetime.fromtimestamp(self.data['created'] / 1000.0)

    def getLastUpdated(self):
        return self.data['last_updated']

    def getLastUpdatedDatetime(self):
        return datetime.fromtimestamp(self.data['last_updated'] / 1000.0)
