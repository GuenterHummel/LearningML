class Car:
    static_info = "Car class wide info"

    def __init__(self, brand, color, horse_power):
        self.brand = brand
        self.color = color
        self.horse_power = horse_power
        self.is_tuned = False

    def __str__(self) -> str:
        return f"Marke: {self.brand} / Farbe: {self.color} /" + \
               f" PS: {self.horse_power} / Tuning: {self.is_tuned}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return self.brand == other.brand and \
               self.color == other.color and \
               self.horse_power == other.horse_power and \
               self.is_tuned == other.is_tuned

    def paint_with(self, new_color):
        self.color = new_color

    def apply_tuning_kit(self) -> bool:
        if not self.is_tuned:
            self.horse_power += 150
            self.is_tuned = True
            return True

        return False

    @staticmethod
    def generate_info():
        print("static methods can be called without creating objects")
        return "Special Information"


    def object_method(self):
        print("object methods must be called on objects")
        print("static methods/variables are accessible")
        return Car.static_info


class CarManagementApplication:
    def __init__(self):
        self.available_cars = [Car("Renault", "BLUE", 75),
                               Car("Renault", "PETROL", 175),
                               Car("Ferrari", "RED", 455),
                               Car("BMW", "GREEN", 255),
                               Car("BMW", "YELLOW", 125),
                               Car("VW", "WHITE", 65),
                               Car("VW", "BLUE", 105)]

    def filter_by_brand(self, brand):
        for current_car in self.available_cars:
            if current_car.brand == brand:
                print(current_car)


    def filter_by_horse_power_greater_than(self, min_horse_power):
        for i in range(len(self.available_cars)):
            if self.available_cars[i].horse_power > min_horse_power:
                print(self.available_cars[i])


def main():
    app = CarManagementApplication()

    print("Alle Renaults im Angebot:")
    app.filter_by_brand("Renault")
    print()

    print("Alle Autos mit mehr als 150 PS:")
    app.filter_by_horse_power_greater_than(150)


if __name__ == "__main__":
    main()