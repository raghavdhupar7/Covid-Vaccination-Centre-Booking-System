class User(object):
    def __init__(self) -> None:
        self.Id = None
        self.name = None
        self.gender = None
        self.age = None
        self.currentState = None
        self.currentDistrict = None

    def setId(self, Id):
        self.Id = Id

    def getId(self):
        return self.Id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setGender(self, gender):
        self.gender = gender

    def getGender(self):
        return self.gender

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setCurrentState(self, currentState):
        self.currentState = currentState

    def getCurrentState(self):
        return self.currentState

    def setCurrentDistrict(self, currentDistrict):
        self.currentDistrict = currentDistrict

    def getCurrentDistrict(self):
        return self.currentDistrict
