import sys
import logging

sys.path.append(r"r:/Github/Covid-Vaccination-Centre-Booking-System")
from models.center import Center

logging.basicConfig(level=logging.INFO)


class CenterService(object):
    centerDetails = {}

    def addCenter(self, stateName: str, districtName: str, id: str) -> Center:
        logging.info(f"Adding center with id: {id}, state: {stateName}, district: {districtName}")
        center = Center()
        center.setStateName(stateName)
        center.setDistrictName(districtName)
        center.setId(id)

        self.__class__.centerDetails[
            id
        ] = center  # adding user object in a class level dictionary for storing
        return center

    def addCapacity(self, id: str, day: str, capacity: int) -> Center:
        logging.info(f"Adding capacity to center with id: {id}, day: {day}, capacity: {capacity}")
        center = self.__class__.centerDetails[id]
        print(center)
        center.setCapacity(day, capacity)
        return center
