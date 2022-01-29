import sys

sys.path.append(r"F:\Flipkart")
from covid.services.center_service import CenterService


class CenterController(object):
    def __init__(self) -> None:
        self.centerService = CenterService()

    def addCenter(self, stateName, districtName, id):
        if id in self.centerService.centerDetails:
            print("Center ID already exists")
        else:
            return self.centerService.addCenter(stateName, districtName, id)

    def addCapacity(self, id, day, capacity):
        self.centerService.addCapacity(id, day, capacity)

    def listVaccinationCenters(self, district):
        centers = []

        for centerId, center in self.centerService.centerDetails.items():  # check here
            if center.getDistrictName() == district:
                centers.append(center.getId())

        print("Centers in district " + district + " are:")
        for centerName in centers:
            print(centerName)

    def searchVaccincationCenter(self, day, district):

        centers = []

        for centerId, center in self.centerService.centerDetails.items():  # check here
            if center.getDistrictName() == district: #and center.getCapacity(day) > 0:
                centers.append(center.getId())

        print("Centers in district " + district + " having capacity are:")
        for centerName in centers:
            print(centerName)
