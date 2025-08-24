import sys
import logging

sys.path.append(r"r:/Github/Covid-Vaccination-Centre-Booking-System")
from models.user import User

logging.basicConfig(level=logging.INFO)


class UserService(object):
    userDetails = {}

    def addUser(self, id: str, name: str, gender: str, age: int, currentState: str, currentDistrict: str):
        logging.info(f"Adding user with id: {id}, name: {name}, age: {age}")
        if not isinstance(id, str):
            raise TypeError("id must be a string")
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(gender, str):
            raise TypeError("gender must be a string")
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        if not isinstance(currentState, str):
            raise TypeError("currentState must be a string")
        if not isinstance(currentDistrict, str):
            raise TypeError("currentDistrict must be a string")

        user = User()
        user.setId(id)
        user.setName(name)
        user.setGender(gender)

        if age < 18:
            raise ValueError("The User is not eligible for vaccination or uses this system.")

        user.setAge(age)
        user.setCurrentState(currentState)
        user.setCurrentDistrict(currentDistrict)

        self.__class__.userDetails[
            id
        ] = user  # adding user object in a class level dictionary for storing
        return user

    def getAllUsers(self):
        logging.info("Getting all users")
        return self.__class__.userDetails
