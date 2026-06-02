# Online Cab Booking Application
class Ride:
    def book_ride(self):
        print("Ride booked successfully!")

    def calculate_fare(self, distance):
        raise NotImplementedError("Subclass must implement fare calculation")


class BikeRide(Ride):
    def calculate_fare(self, distance):
        return distance * 10


class AutoRide(Ride):
    def calculate_fare(self, distance):
        return distance * 15


class CabRide(Ride):
    def calculate_fare(self, distance):
        return distance * 20

ride = AutoRide()
ride.book_ride()
print("Fare:", ride.calculate_fare(10))