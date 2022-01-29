class Booking(object):
    def __init__(self) -> None:
        self.id = None
        self.centerId = None
        self.userId = None
        self.day = None

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setCentreId(self, centreId):
        self.centreId = centreId

    def getCenterId(self):
        return self.centerId

    def setUserId(self, userId):
        self.userId = userId

    def getUserId(self):
        return self.userId

    def setDay(self, day):
        self.day = day

    def getday(self):
        return self.day
