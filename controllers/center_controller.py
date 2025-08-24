import sys

sys.path.append(r"r:/Github/Covid-Vaccination-Centre-Booking-System")
from services.center_service import CenterService


class CenterController(object):
    def __init__(self, centerService: CenterService) -> None:
        self.centerService = centerService

    def addCenter(self, stateName: str, districtName: str, id: str):
        if id in self.centerService.centerDetails:
            raise ValueError("Center ID already exists")
        else:
            return self.centerService.addCenter(stateName, districtName, id)

    def addCapacity(self, id: str, day: str, capacity: int) -> None:
        if id not in self.centerService.centerDetails:
            print(f"Center '{id}' does not exist.")
            return None
        self.centerService.addCapacity(id, day, capacity)

    def listVaccinationCenters(self, district: str) -> None:
        centers = []

        for centerId, center in self.centerService.centerDetails.items():  # check here
            if center.getDistrictName() == district:
                centers.append(center.getId())

        print("Centers in district " + district + " are:")
        for centerName in centers:
            print(centerName)

    def searchVaccincationCenter(self, day: str, district: str) -> None:

        centers = []

        for centerId, center in self.centerService.centerDetails.items():  # check here
            if center.getDistrictName() == district:  # and center.getCapacity(day) > 0:
                centers.append(center.getId())

        print("Centers in district " + district + " having capacity are:")
        for centerName in centers:
            print(centerName)
