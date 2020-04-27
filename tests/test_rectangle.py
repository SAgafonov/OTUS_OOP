import pytest
from to_be_tested.figures import Triangle, Rectangle, Square, Circle


def test_name():
    assert Rectangle(2, 3, 2, 3).name == "Rectangle"


def test_angles():
    assert Rectangle(2, 3, 2, 3).angles == 4


@pytest.mark.parametrize("sides, perimeter", [((2, 3, 2, 3), 10),
                                              ((2.3, 2.4, 2.4, 2.3), 9.4)])
def test_perimeter(sides, perimeter):
    a, b, c, d = sides
    rectangle = Rectangle(a, b, c, d)
    assert rectangle.perimeter == perimeter
    del rectangle


@pytest.mark.parametrize("sides, area", [((2, 3, 2, 3), 6),
                                         ((2.3, 2.4, 2.4, 2.3), 5.5)])
def test_area(sides, area):
    a, b, c, d = sides
    rectangle = Rectangle(a, b, c, d)
    assert rectangle.area == area
    del rectangle


@pytest.mark.parametrize("sides, class_to_sum, result_sum", [((1, 2, 1, 2), Triangle(2, 3, 4), 4.9),
                                                             ((1, 2, 1, 2), Square(2), 6),
                                                             ((1, 2, 1, 2), Circle(4), 14.6)])
def test_sum_areas(sides, class_to_sum, result_sum):
    a, b, c, d = sides
    rectangle = Rectangle(a, b, c, d)
    assert rectangle.add_square(class_to_sum) == result_sum
    del rectangle


@pytest.mark.parametrize("sides", [(-2, 3, 2, 3),
                                   (2, -3, 2, 3),
                                   (2, 3, -2, 3),
                                   (2, 3, 2, -3),
                                   (0, 2, 3, 4),
                                   (2, 0, 4, 1),
                                   (2, 3, 0, 1),
                                   (2, 3, 2, 0)])
def test_negative_value_of_side(sides, fixture_negative_side):
    a, b, c, d = sides
    with pytest.raises(ValueError) as excinfo:
        rectangle = Rectangle(a, b, c, d)
        del rectangle
    assert str(excinfo.value) == fixture_negative_side


@pytest.mark.parametrize("sides", [(1, 2, 3, 1)])
def test_not_rectangle(sides, fixture_rectangle_not_exists):
    a, b, c, d = sides
    with pytest.raises(ValueError) as excinfo:
        rectangle = Rectangle(a, b, c, d)
        del rectangle
    assert str(excinfo.value) == fixture_rectangle_not_exists


@pytest.mark.parametrize("sides", [(1, 2, 1, 2)])
def test_sum_with_incorrect_class(sides, fixture_incorrect_type, fixture_test_class):
    a, b, c, d = sides
    rectangle = Rectangle(a, b, c, d)
    print(fixture_test_class)
    with pytest.raises(TypeError) as excinfo:
        rectangle.add_square(fixture_test_class())
        del rectangle
    assert str(excinfo.value) == fixture_incorrect_type
