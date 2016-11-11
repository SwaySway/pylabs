

class Rectangle:
    width = None
    length = None

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def set_length(self, length):
        self.length = length

    def set_width(self, width):
        self.width = width

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width

    def get_area(self):
        return self.length * self.width


class Cube(Rectangle):
    height = None

    def __init__(self, length, width, height):
        Rectangle(width, length)
        self.height = height

    def get_volume(self):
        return self.width * self.length * self.height


def main():
    square = Rectangle(4, 9)
    box = Cube()
    print(square.get_area())

if __name__ == "__main__":
    main()
