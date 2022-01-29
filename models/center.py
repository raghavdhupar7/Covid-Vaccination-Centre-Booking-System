from collections import defaultdict


class Center(object):
    def __init__(self) -> None:
        self.id = None
        self.stateName = None
        self.districtName = None
        self.capacity = {}  # key-value pair for day and capacity
        self.userList = defaultdict(list)  # key-value pair for day and users

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setStateName(self, stateName):
        self.stateName = stateName

    def getStateName(self):
        return self.stateName

    def setDistrictName(self, districtName):
        self.districtName = districtName

    def getDistrictName(self):
        return self.districtName

    def setCapacity(self, day, capacity=0):
        self.capacity[
            day
        ] = capacity  # for a perticular day, X. we have Y amount of capacity

    def getCapacity(self, day):
        return self.capacity[day]

    def addUser(self, user, day):
        if user != None:
            self.userList[day].append(user)

    def getUserList(self, day):
        return self.userList[day]
