class ServerProperties:
    def __init__(self, data):
        self.data = data

    def allowFlight(self):
        return self.data['allow_flight']

    def allowNether(self):
        return self.data['allow_nether']

    def announcePlayerAchievements(self):
        return self.data['announce_player_achievements']

    def getDifficulty(self):
        return self.data['difficulty']

    def enableCommandBlocks(self):
        return self.data['enable_command_block']

    def forceGamemode(self):
        return self.data['force_gamemode']

    def getGamemode(self):
        return self.data['gamemode']

    def generateStructures(self):
        return self.data['generate_structures']

    def generatorSettings(self):
        return self.data['generator_settings']

    def getHardcore(self):
        return self.data['hardcore']

    def levelName(self):
        return self.data['level_name']

    def levelSeed(self):
        return self.data['level_seed']

    def levelType(self):
        return self.data['level_type']

    def maxPlayers(self):
        return self.data['max_players']

    def getPvP(self):
        return self.data['pvp']

    def resourcePack(self):
        return self.data['resource_pack']

    def spawnAnimals(self):
        return self.data['spawn_animals']

    def spawnMobs(self):
        return self.data['spawn_mobs']

    def resourcePackSHA1(self):
        return self.data['resource_pack_sha1']

    def spawnProtection(self):
        return self.data['spawn_protection']

    def viewDistance(self):
        return self.data['view_distance']
