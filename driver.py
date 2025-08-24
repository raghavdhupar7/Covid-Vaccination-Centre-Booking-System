import sys

sys.path.append(r"F:\CovidManagementCentre")


from covid.controllers.booking_controller import BookingController
from covid.controllers.center_controller import CenterController
from covid.controllers.user_controller import UserController


userController = UserController()
centerController = CenterController()
bookingController = BookingController()

user1 = userController.addUser("user1", "Raghav", "Male", 22, "Punjab", "Jalandhar")
user2 = userController.addUser("user2", "Akshit", "Male", 23, "Punjab", "Barnala")
user3 = userController.addUser("user3", "Sumeet", "Male", 21, "Punjab", "Ludhiana")
# user4 = userController.addUser("user4", "Sahib", "Male", 22, "Punjab", "Ludhiana")
# user5 = userController.addUser("user5", "Vinamer", "Male", 22, "Punjab", "Amritsar")


center1 = centerController.addCenter("Punjab", "Ludhiana", "C001")
center2 = centerController.addCenter("Punjab", "Jalandhar", "C002")
center3 = centerController.addCenter("Punjab", "Jalandhar", "C003")

centerController.addCapacity("C002", 1, 3)


# centerController.listVaccinationCenters("Ludhiana")

print(bookingController.addBooking("B001", "C002", 1, "user1"))
print(bookingController.addBooking("B002", "C002", 1, "user2"))
print(bookingController.addBooking("B003", "C002", 1, "user3"))

# bookingController.addBooking("B001", "C002", 1, "user4")

bookingController.listAllBookings("C002", 1)

# ookingController.cancelBooking("C002", "B001", "user1")
# bookingController.cancelBooking("C002", "B001", "user2")

# bookingController.listAllBookings("C002", 1)

centerController.searchVaccincationCenter(1, "Jalandhar")
