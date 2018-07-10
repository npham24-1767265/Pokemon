from Move import Move


class Pokemon(object):
    POKEDEX = {}
    IV = 31
    STAB = 1.5
    LEVEL = 50

    def __init__(self, pokemon_name):
        pokemonInfo = []
        if len(Pokemon.POKEDEX) == 0:
            file = open("Pokedex.csv", 'r')
            for line in file:
                line = line.strip()
                pokeList = line.split(",")
                # Creating key (Pokemon name) value (id info) pair
                Pokemon.POKEDEX[pokeList[1]] = pokeList
            file.close()
        # Creating an info list for the user-selected Pokemon containing all the Pokemon attributes
        for key in Pokemon.POKEDEX:
            if key.lower() == pokemon_name.lower():
                pokemonInfo = Pokemon.POKEDEX[key]

        # ATTRIBUTES
        # Referring to the pokemonInfo list to fill in the rest of the attributes
        # ID Info
        self.__id = pokemonInfo[0]
        self.name = pokemonInfo[1]
        self.level = Pokemon.LEVEL

        # Type
        self.type1 = pokemonInfo[2]
        self.type2 = pokemonInfo[3]

        # ABILITY
        self.ability = pokemonInfo[4]

        # BASE STATS
        self.__hp = int(pokemonInfo[5])
        self.__atk = int(pokemonInfo[6])
        self.__def = int(pokemonInfo[7])
        self.__spa = int(pokemonInfo[8])
        self.__spd = int(pokemonInfo[9])
        self.__spe = int(pokemonInfo[10])

        # EV STATS
        self.EV_hp = int(pokemonInfo[17])
        self.EV_atk = int(pokemonInfo[18])
        self.EV_def = int(pokemonInfo[19])
        self.EV_spa = int(pokemonInfo[20])
        self.EV_spd = int(pokemonInfo[21])
        self.EV_spe = int(pokemonInfo[22])

        # Holding Item
        self.item = pokemonInfo[15]

        # Nature
        self.nature = pokemonInfo[16]

        # In Battle Stats
        # The base stat is different from the in battle stat.
        # The base stat is just used for calculating the in-battle stat
        # The in battle stats are calculated based on a formula from the games
        # self.battleHP = int(self.__hp + (0.5 * Pokemon.IV) + (0.125 * self.EV_hp) + 60)
        self.battleHP = (2 * self.__hp + Pokemon.IV + (self.EV_hp / 4) * Pokemon.LEVEL) / 100 + Pokemon.LEVEL + 10
        # self.battleATK = self.__atk + (0.5 * Pokemon.IV) + (0.125 * self.EV_atk) + 5
        self.battleATK = self.processStat(self.__atk, self.EV_atk)
        self.battleDEF = self.processStat(self.__def, self.EV_def)
        self.battleSPA = self.processStat(self.__spa, self.EV_spa)
        self.battleSPD = self.processStat(self.__spd, self.EV_spd)
        self.battleSPE = self.processStat(self.__spe, self.EV_spe)
        self.processNature(self.battleATK, self.battleDEF, self.battleSPA,
                           self.battleSPD, self.battleSPE, self.nature)

        # These variables are used to just hold the values of the original stat for stat modification purposes
        self.originalATK = self.processStat(self.__atk, self.EV_atk)
        self.originalDEF = self.processStat(self.__def, self.EV_def)
        self.originalSPA = self.processStat(self.__spa, self.EV_spa)
        self.originalSPD = self.processStat(self.__spd, self.EV_spd)
        self.originalSPE = self.processStat(self.__spe, self.EV_spe)
        self.processNature(self.originalATK, self.originalDEF, self.originalSPA,
                           self.originalSPD, self.originalSPE, self.nature)

        # Moves
        # The Pokemon Spreadsheet has pre-determined movesets
        self.move1 = Move(pokemonInfo[11])
        self.move2 = Move(pokemonInfo[12])
        self.move3 = Move(pokemonInfo[13])
        self.move4 = Move(pokemonInfo[14])

        # A list containing all the moves; used for error-checking later
        self.moveList = [self.move1.name.lower(), self.move2.name.lower(), self.move3.name.lower(),
                         self.move4.name.lower()]

    def processNature(self, atk, defense, spa, spd, spe, nature):
        file = open("Nature.csv", 'r')
        for line in file:
            line = line.strip()
            natureList = line.split(",")
            if natureList[0] == nature:
                atk = (atk * natureList[1]) / 100
                defense = (defense * natureList[2]) / 100
                spa = (spa * natureList[3]) / 100
                spd = (spd * natureList[4]) / 100
                spe = (spe * natureList[5]) / 100
        file.close()
        # MIGHT BE CALL-BY-VALUE AND NOT CHANGES AT ALL

    def processStat(self, baseStat, EV):
        return (2 * baseStat + Pokemon.IV + (EV / 4) * Pokemon.LEVEL) / 100 + 5

    def __str___(self):
        return "Pokemon name: " + str(self.name) + "\nID: " + str(self.__id) + "\nType: " + str(self.type1) + \
               " Type: " + str(self.type2) + "\nBase HP: " + str(self.__hp) + "\nBase ATK: " + str(self.__atk) + \
               "\nBase DEF: " + str(self.__def) + "\nBase SPA: " + str(self.__spa) + \
               "\nBase SPD: " + str(self.__spd) + "\nBase SPE: " + str(self.__spe) + \
               "\nCurrent HP: " + str(self.battleHP) + "\nCurrent ATK: " + str(self.battleATK) + \
               "\nCurrent DEF: " + str(self.battleDEF) + "\nCurrent SPA: " + str(self.battleSPA) + \
               "\nCurrent SPD: " + str(self.battleSPD) + "\nCurrent SPE: " + str(self.battleSPE)

    #GET method

    def getName(self):
        return self.name

    # Get BASE STAT METHODS
    def getHP(self):
        return self.__hp

    def getATK(self):
        return self.__atk

    def getDEF(self):
        return self.__def

    def getSpATK(self):
        return self.__spa

    def getSpDEF(self):
        return self.__spd

    def getSpeed(self):
        return self.__spe


    # Get STAT STAGE Methods
    def getAtkStage(self):
        return self.atkStage

    def getDefStage(self):
        return self.defStage

    def getSpAtkStage(self):
        return self.spAtkStage

    def getSpDefStage(self):
        return self.spDefStage

    def getSpeedStage(self):
        return self.speedStage


    # Set STAT STAGE Methods
    def setAtkStage(self, atkStage):
        self.atkStage = atkStage

    def setDefStage(self, defStage):
        self.defStage = defStage

    def setSpAtkStage(self, spAtkStage):
        self.spAtkStage = spAtkStage

    def setSpDefStage(self, spDefStage):
        self.spDefStage = spDefStage

    def setSpeedStage(self, speedStage):
        self.speedStage = speedStage


    # MOVE Methods
    def getMove1(self):
        return self.move1

    def getMove2(self):
        return self.move2

    def getMove3(self):
        return self.move3

    def getMove4(self):
        return self.move4

    def setMove1(self, move1):
        self.move1 = Move(move1)

    def setMove2(self, move2):
        self.move2 = Move(move2)

    def setMove3(self, move3):
        self.move3 = Move(move3)

    def setMove4(self, move4):
        self.move4 = Move(move4)