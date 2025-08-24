import sys
import logging

sys.path.append(r"r:/Github/Covid-Vaccination-Centre-Booking-System")
from models.booking import Booking

logging.basicConfig(level=logging.INFO)


class BookingService(object):
    bookingDetails = {}

    def addBooking(self, bookingId: str, centerId: str, day: int, userId: str) -> Booking:
        logging.info(
            f"Adding booking with id: {bookingId}, centerId: {centerId}, userId: {userId}, day: {day}"
        )
        booking = Booking()
        booking.setId(bookingId)
        booking.setCenterId(centerId)
        booking.setUserId(userId)
        booking.setDay(day)
        print(f"{centerId} this is a center" )
        self.__class__.bookingDetails[
            bookingId
        ] = booking  # adding user object in a class level dictionary for storing
        return booking
