import pytest
from to_be_tested.figures import Triangle, Rectangle, Square, Circle


def test_name():
    assert Triangle(2, 3, 4).name == "Triangle"


def test_angles():
    assert Triangle(2, 3, 4).angles == 3


def test_scalene_triangle(fixture_triangle_scalene):
    a, b, c = fixture_triangle_scalene
    triangle = Triangle(a, b, c)
    assert triangle.check_type_of_triangle() == "Scalene"
    del triangle


def test_equilateral_triangle(fixture_triangle_equilateral):
    a, b, c = fixture_triangle_equilateral
    triangle = Triangle(a, b, c)
    assert triangle.check_type_of_triangle() == "Equilateral"
    del triangle


def test_isosceles_triangle(fixture_triangle_isosceles):
    a, b, c = fixture_triangle_isosceles
    triangle = Triangle(a, b, c)
    assert triangle.check_type_of_triangle() == "Isosceles"
    del triangle


@pytest.mark.parametrize("sides, perimeter", [((2, 3, 4), 9),
                                              ((2.3, 2.4, 4.6), 9.3)])
def test_perimeter(sides, perimeter):
    a, b, c = sides
    triangle = Triangle(a, b, c)
    assert triangle.perimeter == perimeter
    del triangle


@pytest.mark.parametrize("sides, area", [((2, 3, 4), 2.9),
                                         ((2.3, 2.4, 4.6), 1.1)])
def test_area(sides, area):
    a, b, c = sides
    triangle = Triangle(a, b, c)
    assert triangle.area == area
    del triangle


@pytest.mark.parametrize("sides, class_to_sum, result_sum", [((2, 3, 4), Rectangle(1, 2, 1, 2), 4.9),
                                                             ((2.3, 2.4, 4.6), Square(2), 5.1),
                                                             ((2, 3, 4), Circle(4), 15.5)])
def test_sum_areas(sides, class_to_sum, result_sum):
    a, b, c = sides
    triangle = Triangle(a, b, c)
    assert triangle.add_square(class_to_sum) == result_sum
    del triangle


@pytest.mark.parametrize("sides", [(-2, 3, 4),
                                   (2, -3, 4),
                                   (2, 3, -4),
                                   (0, 3, 4),
                                   (2, 0, 4),
                                   (2, 3, 0)])
def test_negative_value_of_side(sides, fixture_negative_side):
    a, b, c = sides
    with pytest.raises(ValueError) as excinfo:
        triangle = Triangle(a, b, c)
        del triangle
    assert str(excinfo.value) == fixture_negative_side


@pytest.mark.parametrize("sides", [(1, 2, 3)])
def test_not_triangle(sides, fixture_triangle_not_exists):
    a, b, c = sides
    with pytest.raises(ValueError) as excinfo:
        triangle = Triangle(a, b, c)
        del triangle
    assert str(excinfo.value) == fixture_triangle_not_exists


@pytest.mark.parametrize("sides", [(2, 3, 4)])
def test_sum_with_incorrect_class(sides, fixture_incorrect_type, fixture_test_class):
    a, b, c = sides
    triangle = Triangle(a, b, c)
    print(fixture_test_class)
    with pytest.raises(TypeError) as excinfo:
        triangle.add_square(fixture_test_class())
        del triangle
    assert str(excinfo.value) == fixture_incorrect_type
