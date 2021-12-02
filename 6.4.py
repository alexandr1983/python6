class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} is started"

    def stop(self):
        return f"{self.name} is stopped"

    def turn_right(self):
        return f"{self.name} is turned right"

    def turn_left(self):
        return f"{self.name} is turned left"

    def show_speed(self):
        return f"Nice speed {self.name} is {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Normal speed {self.name} is {self.speed}")

        if self.speed > 40:
            return f"Speed of {self.name} is higher"
        else:
            return f"Speed of {self.name} is normal"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Speed of {self.name} is {self.speed}")

        if self.speed > 60:
            return f"Speed of {self.name} is higher"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"{self.name} is police"
        else:
            return f"{self.name} is not police"


towncar = TownCar(input("Enter speed: "), input("Enter color: "), input("Enter model: "), input("Is police? :"))
sportcar = SportCar(input("Enter speed: "), input("Enter color: "), input("Enter model: "), input("Is police? :"))
workcar = WorkCar(input("Enter speed: "), input("Enter color: "), input("Enter model: "), input("Is police? :"))
policecar = (int(input("Enter speed: ")), input("Enter color: "), input("Enter model: "), True)

print(sportcar.show_speed())
print(workcar.go)
print(towncar.stop)
print(policecar.turn_right)
