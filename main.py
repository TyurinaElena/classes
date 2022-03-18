
class Colors:
    def __init__(self, name, r, g, b):
        self.name = name
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"{self.name} ({self.r}, {self.g}, {self.b})"
    def __eq__(self, other):
        if isinstance(other, Colors):
            return (self.r == other.r and
                    self.g == other.g and
                    self.b == other.b)
        return NotImplemented

red = Colors('красный', 255, 0, 0)
green = Colors('зеленый', 0, 255, 0)
other_red = Colors('другой красный', 255, 0, 0)

print(other_red)
print(red)
print(green)

print(red == green)
print(red == other_red)

class Trapeze:

    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def __str__(self):
        return f"Трапеция с основаниями {self.base1}, {self.base2} и высотой {self.height}"

    def __eq__(self, other):
        if isinstance(other, Trapeze):
            return (self.base1 == other.base1 and
                    self.base2 == other.base2 and
                    self.height == other.height)
        return NotImplemented

first = Trapeze(3, 4, 5)
second = Trapeze(3, 4, 5)
three = Trapeze(1, 2, 3)

print(first)
print(second)
print(three)

print(first == second)
print(second == three)