import sys

sys.path.append(r"F:\main_folder")
from covid.models.booking import Booking


class BookingService(object):
    bookingDetails = {}

    def addBooking(self, bookingId, centerId, day, userId):
        booking = Booking()
        booking.setId(bookingId)
        booking.setCentreId(centerId)
        booking.setUserId(userId)
        booking.setDay(day)

        self.__class__.bookingDetails[
            bookingId
        ] = booking  # adding user object in a class level dictionary for storing
        return booking
    


