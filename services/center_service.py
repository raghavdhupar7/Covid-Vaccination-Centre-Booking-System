import sys

sys.path.append(r"F:\Flipkart")
from covid.models.center import Center


class CenterService(object):
    centerDetails = {}

    def addCenter(self, stateName, districtName, id):
        center = Center()
        center.setStateName(stateName)
        center.setDistrictName(districtName)
        center.setId(id)

        self.__class__.centerDetails[
            id
        ] = center  # adding user object in a class level dictionary for storing
        return center

    def addCapacity(self, id, day, capacity):
        center = self.__class__.centerDetails[id]
        print(center)
        center.setCapacity(day, capacity)
        return center
