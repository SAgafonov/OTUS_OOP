import math


class Figure:

    def __init__(self, cls, **kwargs):
        self.cls_to_be_calculated = cls
        self.figure_characteristics = kwargs
        self.angles = self.set_angles()
        self.perimeter = self.set_perimeter()
        self.area = self.set_area()

    @staticmethod
    def check_if_figure_defined(cls):
        if not isinstance(cls, Figure):
            raise TypeError("Incorrect class is provided")

    def set_angles(self):
        angles_in_figures = {"Triangle": 3, "Rectangle": 4, "Square": 4, "Circle": 0}
        return angles_in_figures[self.cls_to_be_calculated.name]

    def set_perimeter(self):
        if isinstance(self.cls_to_be_calculated, (Triangle, Rectangle, Square)):
            return round(sum(self.figure_characteristics.values()), 1)
        else:
            return round(math.pi * self.figure_characteristics.get('diameter'), 1)

    def set_area(self):
        measurements = list(self.figure_characteristics.values())
        if isinstance(self.cls_to_be_calculated, Triangle):
            half_perimeter = self.perimeter / 2
            area = math.sqrt(half_perimeter *
                             (half_perimeter - measurements[0]) *
                             (half_perimeter - measurements[1]) *
                             (half_perimeter - measurements[2])
                             )
            return round(area, 1)
        elif isinstance(self.cls_to_be_calculated, (Rectangle, Square)):
            return round((measurements[0] * measurements[1]), 1)
        else:
            return round(math.pi * ((self.figure_characteristics.get('diameter')/2)**2), 1)


class Triangle(Figure):

    def __init__(self, first_side, second_side, third_side):
        self.name = "Triangle"
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side
        self.triangle_type = self.check_type_of_triangle()
        super().__init__(self, a=self.first_side, b=self.second_side, c=self.third_side)

    def check_type_of_triangle(self) -> str:
        """
        Check if triangle exists and returns its type.
        :return: str
        """
        if self.first_side <= 0 or self.second_side <= 0 or self.third_side <= 0:
            raise ValueError("Value must be greater than zero")
        if self.first_side + self.second_side <= self.third_side \
                or self.first_side + self.third_side <= self.second_side \
                or self.second_side + self.third_side <= self.first_side:
            raise ValueError("Triangle does not exist")
        elif self.first_side != self.second_side \
                and self.first_side != self.third_side \
                and self.second_side != self.third_side:
            return "Scalene"                                # Разносторонний треугольник
        elif self.first_side == self.second_side == self.third_side:
            return "Equilateral"                            # Равносторонний треугольник
        else:
            return "Isosceles"                              # Равнобедренный треугольник

    def add_square(self, figure_to_add):
        Figure.check_if_figure_defined(figure_to_add)
        return self.area + figure_to_add.area


class Rectangle(Figure):

    def __init__(self, first_side, second_side, third_side=None, fourth_side=None):
        self.name = "Rectangle"
        self.first_side = first_side
        self.second_side = second_side
        if third_side is not None:
            self.third_side = third_side
        else:
            self.third_side = self.first_side
        if fourth_side is not None:
            self.fourth_side = fourth_side
        else:
            self.fourth_side = self.second_side
        self.check_if_rectangle()
        super().__init__(self, a=self.first_side, b=self.second_side, c=self.third_side, d=self.fourth_side)

    def check_if_rectangle(self):
        if self.first_side <= 0 or self.second_side <= 0 or self.third_side <= 0 or self.fourth_side <= 0:
            raise ValueError("Value must be greater than zero")
        sorted_list_of_sides = sorted([self.first_side, self.second_side, self.third_side, self.fourth_side])
        if (sorted_list_of_sides[0], sorted_list_of_sides[2]) != (sorted_list_of_sides[1], sorted_list_of_sides[3]):
            raise ValueError("It's not a Rectangle")

    def add_square(self, figure_to_add):
        Figure.check_if_figure_defined(figure_to_add)
        return self.area + figure_to_add.area


class Square(Figure):

    def __init__(self, first_side, second_side=None, third_side=None, fourth_side=None):
        self.name = "Square"
        self.first_side = first_side
        if second_side is not None:
            self.second_side = second_side
        else:
            self.second_side = self.first_side
        if third_side is not None:
            self.third_side = third_side
        else:
            self.third_side = self.first_side
        if fourth_side is not None:
            self.fourth_side = fourth_side
        else:
            self.fourth_side = self.first_side
        self.check_if_square()
        super().__init__(self, a=self.first_side, b=self.second_side, c=self.third_side, d=self.fourth_side)

    def check_if_square(self):
        if self.first_side <= 0 or self.second_side <= 0 or self.third_side <= 0 or self.fourth_side <= 0:
            raise ValueError("Value must be greater than zero")
        if not self.first_side == self.second_side == self.third_side == self.fourth_side:
            raise ValueError("It's not a Square")

    def add_square(self, figure_to_add):
        Figure.check_if_figure_defined(figure_to_add)
        return self.area + figure_to_add.area


class Circle(Figure):

    def __init__(self, diameter):
        self.name = "Circle"
        self.diameter = diameter
        self.check_if_circle_exists()
        super().__init__(self, diameter=self.diameter)

    def check_if_circle_exists(self):
        if self.diameter <= 0:
            raise ValueError("Value must be greater than zero")

    def add_square(self, figure_to_add):
        Figure.check_if_figure_defined(figure_to_add)
        return self.area + figure_to_add.area
