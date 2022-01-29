import sys

sys.path.append(r"F:\main_folder")
from covid.services.booking_service import BookingService
from covid.services.center_service import CenterService
from covid.services.user_service import UserService


class BookingController(object):
    def __init__(self) -> None:
        self.bookingService = BookingService()
        self.centerService = CenterService()
        self.userService = UserService()

    def addBooking(self, bookingId, centerId, day, userId):
        center = self.centerService.centerDetails[centerId]
        if center.getCapacity(day) < 1:
            return (
                "There is not enought capacity on this day"
                + str(day)
                + " in the center you are looking: "
                + centerId
            )

        else:
            if bookingId in self.bookingService.bookingDetails:
                return "This Booking ID is already present"
            self.bookingService.addBooking(bookingId, centerId, day, userId)
            currentCapacity = center.getCapacity(day)
            center.setCapacity(day, currentCapacity - 1)
            print("Booking Added Successfully")

    def listAllBookings(self, centerId, day):
        print("Below down is the list of All the bookings: ")
        for bookingId in self.bookingService.bookingDetails.values():
            # print(bookingId)
            currentCenterId = bookingId.getCenterId()
            currentUserId = bookingId.getUserId()

            currentUser = self.userService.userDetails[currentUserId]
            currentUsername = currentUser.getName()
            print(currentUsername)

            currentCenter = self.centerService.centerDetails[centerId]
            currentDistrict = currentCenter.getDistrictName()
            users = currentCenter.getUserList(day)

            for user in users:
                print(bookingId.getId() + " " + user + " " + centerId + currentDistrict)

    def cancelBooking(self, centerId, bookingId, userId):
        if bookingId in self.bookingService.bookingDetails:

            self.bookingService.bookingDetails.pop(bookingId)
            print("Booking ID : " + bookingId + " removed successfully")
        else:
            print("Booking not found")
