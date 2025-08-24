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

    def setCenterId(self, centerId):
        self.centerId = centerId

    def getCenterId(self):
        return self.centerId

    def setUserId(self, userId):
        self.userId = userId

    def getUserId(self):
        return self.userId

    def setDay(self, day):
        self.day = day

    def getDay(self):
        return self.day

    def __str__(self):
        return f"Booking(id={self.id}, centerId={self.centerId}, userId={self.userId}, day={self.day})"
