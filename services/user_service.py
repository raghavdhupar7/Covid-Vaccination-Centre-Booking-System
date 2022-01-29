import sys

sys.path.append(r"F:\main_folder")
from covid.models.user import User


class UserService(object):
    userDetails = {}

    def addUser(self, id, name, gender, age, currentState, currentDistrict):
        user = User()
        user.setId(id)
        user.setName(name)
        user.setGender(gender)

        if age < 18:
            return "The User is not eligible for vaccination or uses this system."

        user.setAge(age)
        user.setCurrentState(currentState)
        user.setCurrentDistrict(currentDistrict)

        self.__class__.userDetails[
            id
        ] = user  # adding user object in a class level dictionary for storing
        return user
