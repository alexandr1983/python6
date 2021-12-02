class Road:
    area = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, thickness):
        return thickness * self.area * self._width * self._length


road = Road(int(input("Enter length: ")), int(input("Enter width: ")))
thickness = int(input("Enter thickness: "))
print(road.weight(thickness))
