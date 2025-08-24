import sys

sys.path.append(r"r:/Github/Covid-Vaccination-Centre-Booking-System")

from controllers.booking_controller import BookingController
from controllers.center_controller import CenterController
from controllers.user_controller import UserController
from services.user_service import UserService
from services.center_service import CenterService
from services.booking_service import BookingService


def main():
    userService = UserService()
    userController = UserController(userService)
    centerService = CenterService()
    centerController = CenterController(centerService)
    bookingService = BookingService()
    bookingController = BookingController(bookingService, centerService, userService)

    while True:
        print("\n--- Covid Management System ---")
        print("1. Add User")
        print("2. Add Vaccination Center")
        print("3. Add Capacity to Center")
        print("4. Book a Slot")
        print("5. List All Bookings for a Center")
        print("6. Cancel Booking")
        print("7. Search Vaccination Center")
        print("8. List Users")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter User ID: ")
            name = input("Enter Name: ")
            gender = input("Enter Gender (Male/Female): ")
            age = int(input("Enter Age: "))
            state = input("Enter State: ")
            city = input("Enter City: ")
            user = userController.addUser(user_id, name, gender, age, state, city)
            print("User added:", user)

        elif choice == "2":
            state = input("Enter State: ")
            city = input("Enter City: ")
            center_id = input("Enter Center ID: ")
            center = centerController.addCenter(state, city, center_id)
            print("Center added:", center)

        elif choice == "3":
            center_id = input("Enter Center ID: ")
            day = int(input("Enter Day: "))
            capacity = int(input("Enter Capacity: "))
            centerController.addCapacity(center_id, day, capacity)
            print("Capacity added successfully.")

        elif choice == "4":
            booking_id = input("Enter Booking ID: ")
            center_id = input("Enter Center ID: ")
            day = input("Enter Day: ")
            user_id = input("Enter User ID: ")
            result = bookingController.addBooking(booking_id, center_id, int(day), user_id)
            if result:
                print(f"Booking Result: {result.getId()} for user {result.getUserId()}")
            else:
                print("Booking could not be created.")

            print("✅ Booking Result:", result)

        elif choice == "5":
            center_id = input("Enter Center ID: ")
            day = input("Enter Day: ")
            bookingController.listAllBookings(center_id, day)

        elif choice == "6":
            center_id = input("Enter Center ID: ")
            booking_id = input("Enter Booking ID: ")
            user_id = input("Enter User ID: ")
            bookingController.cancelBooking(center_id, booking_id, user_id)
            print("Booking cancelled successfully.")

        elif choice == "7":
            day = int(input("Enter day: "))
            city = input("Enter City: ")
            centerController.searchVaccincationCenter(day, city)

        elif choice == "8":
            userController.listUsers()

        elif choice == "0":
            print("Exiting Covid Management System...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
