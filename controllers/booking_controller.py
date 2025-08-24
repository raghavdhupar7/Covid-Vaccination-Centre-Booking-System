import sys

sys.path.append(r"r:/Github/Covid-Vaccination-Centre-Booking-System")
from services.booking_service import BookingService
from services.center_service import CenterService
from services.user_service import UserService


class BookingController(object):
    def __init__(
        self,
        bookingService: BookingService,
        centerService: CenterService,
        userService: UserService,
    ) -> None:
        self.bookingService = bookingService
        self.centerService = centerService
        self.userService = userService

    def addBooking(self, bookingId: str, centerId: str, day: int, userId: str):
        if userId not in self.userService.userDetails:
            print(f"User '{userId}' does not exist.")
            return None

        if centerId not in self.centerService.centerDetails:
            print(f"Center '{centerId}' does not exist.")
            return None

        booking = self.bookingService.addBooking(bookingId, centerId, day, userId)

        if booking:
            print("Booking Added Successfully")
            return booking
        else:
            print("Booking Failed (maybe no capacity left?)")
            return None

    def listAllBookings(self, centerId: str, day) -> None:
        

        if centerId not in self.centerService.centerDetails:
            print(f"Center {centerId} not found.")
            return

        wanted_day = int(day)
        found = False

        print(f"Bookings for Center {centerId} on Day {day}:")

        for booking in self.bookingService.bookingDetails.values():
            b_center = booking.getCenterId()
            b_day = booking.getDay()
            user_id = booking.getUserId()
            # Skip if booking not for this center/day
            if b_center != centerId or int(b_day) != wanted_day:
                continue
            user = self.userService.userDetails.get(user_id)
            if not user:
                print(f"Skipping booking {booking.getId()} — user '{user_id}' not found in userService")
                continue

            user_name = user.getName()
            print(user_name)
            district = self.centerService.centerDetails[centerId].getDistrictName()
            print(f"Booking ID:{booking.getId()} | Username: {user_name} | CenterId: {centerId} | District: {district}")
            found = True

        if not found:
            print("No bookings found for this center/day.")


    def listAllBookings_V3(self, centerId: str, day: str) -> None:
        print(f"Bookings for Center {centerId} on Day {day}:")
        found = False

        for bookingId, booking in self.bookingService.bookingDetails.items():
            currentCenterId = booking.getCenterId()
            currentUserId = booking.getUserId()
            currentDay = booking.getday()
            # Only process bookings for the requested center and day
            if currentCenterId != centerId or str(currentDay) != day:
                continue

            # Defensive check: user must exist
            if currentUserId not in self.userService.userDetails:
                print(
                    f"Skipping booking {booking.getId()} — user '{currentUserId}' not found in userService"
                )
                continue

            currentUser = self.userService.userDetails[currentUserId]
            currentUsername = currentUser.getName()

            currentCenter = self.centerService.centerDetails[centerId]
            currentDistrict = currentCenter.getDistrictName()

            # Get users from center schedule
            # users = currentCenter.getUserList(day) # This line is not used

            print(
                f"{booking.getId()} | {currentUsername} | {centerId} | {currentDistrict}"
            )
            found = True

        if not found:
            print("No bookings found for this center/day.")

    def cancelBooking(self, centerId: str, bookingId: str, userId: str) -> None:
        if bookingId in self.bookingService.bookingDetails:
            self.bookingService.bookingDetails.pop(bookingId)
            print("Booking ID : " + bookingId + " removed successfully")
        else:
            print("Booking not found")
