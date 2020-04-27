import pytest
from to_be_tested.figures import Triangle, Rectangle, Square, Circle


def test_name():
    assert Square(2, 2).name == "Square"


def test_angles():
    assert Square(2, 2).angles == 4


@pytest.mark.parametrize("sides, perimeter", [(2, 8),
                                              (2.3, 9.2)])
def test_perimeter(sides, perimeter):
    square = Square(sides)
    assert square.perimeter == perimeter
    del square


@pytest.mark.parametrize("sides, area", [((2, 2, 2, 2), 4),
                                         ((2.3, 2.3, 2.3, 2.3), 5.3)])
def test_area(sides, area):
    a, b, c, d = sides
    square = Square(a, b, c, d)
    assert square.area == area
    del square


@pytest.mark.parametrize("sides, class_to_sum, result_sum", [(2, Triangle(2, 3, 4), 6.9),
                                                             (2, Rectangle(1, 2, 1, 2), 6),
                                                             (2, Circle(4), 16.6)])
def test_sum_areas(sides, class_to_sum, result_sum):
    square = Square(sides)
    assert square.add_square(class_to_sum) == result_sum
    del square


@pytest.mark.parametrize("sides", [(-2, 2, 2, 2),
                                   (2, -2, 2, 2),
                                   (2, 2, -2, 2),
                                   (2, 2, 2, -2),
                                   (0, 2, 2, 2),
                                   (2, 0, 2, 2),
                                   (2, 2, 0, 2),
                                   (2, 2, 2, 0)])
def test_negative_value_of_side(sides, fixture_negative_side):
    a, b, c, d = sides
    with pytest.raises(ValueError) as excinfo:
        square = Square(a, b, c, d)
        del square
    assert str(excinfo.value) == fixture_negative_side


@pytest.mark.parametrize("sides", [(1, 2, 3, 1),
                                   (1, 2, 1, 2)])
def test_not_square(sides, fixture_square_not_exists):
    a, b, c, d = sides
    with pytest.raises(ValueError) as excinfo:
        square = Square(a, b, c, d)
        del square
    assert str(excinfo.value) == fixture_square_not_exists


@pytest.mark.parametrize("sides", [(2)])
def test_sum_with_incorrect_class(sides, fixture_incorrect_type, fixture_test_class):
    square = Square(sides)
    print(fixture_test_class)
    with pytest.raises(TypeError) as excinfo:
        square.add_square(fixture_test_class())
        del square
    assert str(excinfo.value) == fixture_incorrect_type
