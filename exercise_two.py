# Create a Bus, Taxi, Train child classes that inherits from the Vehicle class.
# Implement at least five methods in a superclass what would describe those vehicles.
# The default fare charge of any vehicle is seating capacity * 100 . If Vehicle is Bus
# instance, we need to add an extra 10% on full fare as a maintenance charge.

class Vehicle:
    def __init__(self, seats: int, consumption: float, color: str,
                 max_speed: float, manufacturer: str) -> None:
        self.seats = seats
        self.consumption = consumption
        self.color = color
        self.max_speed = max_speed
        self.manufacturer = manufacturer

    def get_seats(self) -> int:
        return self.seats

    def get_consumption(self) -> float:
        return self.consumption

    def get_color(self) -> str:
        return self.color

    def get_max_speed(self) -> float:
        return self.max_speed

    def get_manufacturer(self) -> str:
        return self.manufacturer

    def seat_charge(self) -> float:
        return self.seats * 100


class Bus(Vehicle):
    def __init__(self) -> None:
        super().__init__(seats=50, consumption=25,
                         color="red", max_speed=90, manufacturer="Solaris")

    def seat_charge(self):
        maintenance_charge_rate = 1.1
        return self.seats * 100 * maintenance_charge_rate


class Taxi(Vehicle):
    def __init__(self) -> None:
        super().__init__(seats=4, consumption=8,
                         color="blue", max_speed=120, manufacturer="BMW")


class Train(Vehicle):
    def __init__(self) -> None:
        super().__init__(seats=250, consumption=50,
                         color="white", max_speed=150, manufacturer="Goodwin")


if __name__ == "__main__":
    vehicle = Train()
    print("Charge: ", vehicle.seat_charge())
    print("Seats: ", vehicle.get_seats())
    print("Consumption: ", vehicle.get_consumption())
    print("Color: ", vehicle.get_color())
    print("Max speed: ", vehicle.get_max_speed())
    print("Manufacturer: ", vehicle.get_manufacturer())
