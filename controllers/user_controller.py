import sys

sys.path.append(r"r:/Github/Covid-Vaccination-Centre-Booking-System")
from services.user_service import UserService


class UserController(object):
    def __init__(self, userService: UserService) -> None:
        self.userService = userService

    def addUser(self, id: str, name: str, gender: str, age: int, currentState: str, currentDistrict: str) -> None:
        self.userService.addUser(id, name, gender, age, currentState, currentDistrict)

    def listUsers(self) -> None:
        users = self.userService.getAllUsers()
        for user_id, user in users.items():
            print(f"User ID: {user.getId()}, Name: {user.getName()}, Gender: {user.getGender()}, Age: {user.getAge()}, State: {user.getCurrentState()}, City: {user.getCurrentDistrict()}")
