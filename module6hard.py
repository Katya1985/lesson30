class Figure:
    sides_count = 0
    __sides = []
    __color = []
    filled = False

    def __init__(self, colors, *side):  # Атрибуты(публичные): filled(закрашенный, bool)
        self.colors = list(colors)  # список цветов в формате RGB
        self.side = side[0]  # # список сторон (целые числа)
        self.filled = True  # закрашенный, bool

    def get_color(self):
        self.__color = self.color
        self.filled = True
        return self.__color  # возвращает список RGB цветов

    def __is_valid_color(self, r, g, b):  # проверяет корректность переданных значений перед установкой нового цвета
        self.r = r
        self.g = g
        self.b = b
        if 0 <= self.r and self.g and self.b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):  # предварительно проверив их на корректность
        if self.__is_valid_color(r, g, b):
            self.color = [self.r, self.g, self.b]
        else:  # Если введены некорректные данные, то цвет остаётся прежним
            return self.set_color()

    def __is_valid_sides(self, *number_of_sides):
        for side in self.sides:
            if len(self.sides) == self.sides_count and side > 0 and type(side) == int:  # возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим
                return True

        else:  # False - во всех остальных случаях
            return False

    def get_sides(self):  # возвращать значение я атрибута __sides
        self.__sides = self.sides
        return self.__sides

    def __len__(self):  # возвращать периметр фигуры
        return self.side * self.sides_count

    def set_sides(self, *sides):
        massive = []
        self.sides = list(sides)
        if self.__is_valid_sides(self, *sides):
            self.get_sides()
        else:
            for i in range(self.sides_count):
                massive.append(self.side)
            self.sides = massive
            self.get_sides()


class Circle(Figure):
    sides_count = 1
    __radius = None  # рассчитать исходя из длины окружности (одной единственной стороны)

    def get_square(self):  # возвращает площадь круга (можно рассчитать как через длину, так и через радиус)
        self.__radius = self.__len__() / (2 * 3.14)
        return self.__radius


class Triangle(Figure):
    sides_count = 3
    __height = None

    def get_square(self):  # возвращает площадь треугольника. (можно рассчитать по формуле Герона)
        return (self.side ** 2) * (3 ** 0.5) / 4

    def set_height(self):
        self.__height = self.side * (3 ** 0.5) / 2
        return self.__height


class Cube(Figure):
    sides_count = 12

    def new__sides(self):  # Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
        new__sides = []
        if element in range(self.sides_count):
            new__sides.append(self.side)
        self.__sides = new__sides
        return self.__sides

    def get_volume(self):  # возвращает объём куба
        return self.side ** 3


# ВАЖНО!
# При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
# Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
# Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
# Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
# Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
