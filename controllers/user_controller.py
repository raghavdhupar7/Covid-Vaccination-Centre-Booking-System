import sys

sys.path.append(r"F:\main_folder")
from covid.services.user_service import UserService


class UserController(object):
    def __init__(self) -> None:
        self.userService = UserService()

    def addUser(self, id, name, gender, age, currentState, currentDistrict):
        self.userService.addUser(id, name, gender, age, currentState, currentDistrict)
