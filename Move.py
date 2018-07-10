class Move(object) :

    MOVELIST = {}

    def __init__(self, move_name):
        moveInfo = []
        if len(Move.MOVELIST) == 0 :
            file = open("PokemonMoves.csv", 'r')
            for line in file :
                line = line.strip()
                moveList = line.split(",")
                Move.MOVELIST[moveList[1]] = moveList
            file.close()

        for key in Move.MOVELIST :
            if key.lower() == move_name.lower() :
                moveInfo = Move.MOVELIST[key]

        # ATTRIBUTES

        # self.moveInfo = moveInfo
        self.id = moveInfo[0]
        self.name = moveInfo[1]

        self.type = moveInfo[2]
        self.kind = moveInfo[3]

        self.power = moveInfo[4]
        self.accuracy = moveInfo[5]
        self.pp = moveInfo[6]

        self.contact = moveInfo[7]
        self.moveFlag = moveInfo[8]

        self.description = moveInfo[9]

    # METHOD

    def __str__(self) :
        return self.name

    # GET Methods
    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getType(self):
        return self.type

    def getKind(self):
        return self.kind

    def getPower(self):
        return self.power

    def getAccuracy(self):
        return self.accuracy

    def getPP(self):
        return self.pp

    # SET Methods
    def setName(self, name):
        self.name = name

    def setType(self, type):
        self.type = type

    def setPower(self, power):
        self.power = power

    def setAccuracy(self, accuracy):
        self.accuracy = accuracy

    def setPP(self, pp):
        self.pp = pp
