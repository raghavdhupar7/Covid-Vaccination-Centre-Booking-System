# Covid Vaccination Centre Booking System

Designed a vaccination appointment booking system with the below assumptions.

Assumptions:

- Vaccination centers are scattered across multiple states and multiple districts and each district can have multiple vaccination centers, but each vaccination center should be uniquely identifiable.
- Appointments will be booked for a Day (appointments are for 24 hours duration by default). The day can be taken in integer format eg. Book for day 3 or Book for day 5
- An appointment can be booked, given unless the capacity of the day is consumed.
- E.g: Day 2 had 5 as the capacity of appointments. So it can be booked until 5 bookings for day 2 are done for a particular vaccination center.
- 1 citizen can book his/her appointment only once per vaccination dose based on a unique citizen identification number. (Assume there is only one dose) Only if a person cancels the reservation, he/she will be able to book an appointment again
- Cancelation is allowed for an appointment.
- The user below 18 is not eligible for vaccination or uses this system.

## Getting Started

### Dependencies

- Python and an OS which can run python.

### Executing program

- use this as a main folder

- please use this folder path in sys.path.append(r"THIS_FOLDERs_PATH")

- for ex:

  ```py
  import sys
  sys.path.append(r"F:\covid_booking_system")
  ```

- Run driver.py
