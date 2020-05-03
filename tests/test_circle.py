import pytest
from to_be_tested.figures import Triangle, Rectangle, Square, Circle


def test_name():
    assert Circle(2).name == "Circle"


def test_angles():
    assert Circle(2).angles == 0


@pytest.mark.parametrize("diameter, length", [(4, 12.6),
                                              (4.2, 13.2)])
def test_perimeter(diameter, length):
    circle = Circle(diameter)
    assert circle.perimeter == length
    del circle


@pytest.mark.parametrize("diameter, area", [(4, 12.6),
                                            (2.34, 4.3)])
def test_area(diameter, area):
    circle = Circle(diameter)
    assert circle.area == area
    del circle


@pytest.mark.parametrize("diameter, class_to_sum, result_sum", [(4, Triangle(2, 3, 4), 15.5),
                                                             (4, Rectangle(1, 2, 1, 2), 14.6),
                                                             (4, Square(4), 28.6)])
def test_sum_areas(diameter, class_to_sum, result_sum):
    circle = Circle(diameter)
    assert circle.add_square(class_to_sum) == result_sum
    del circle


@pytest.mark.parametrize("diameter", [-2, 0])
def test_negative_value_of_side(diameter, fixture_negative_side):
    with pytest.raises(ValueError) as excinfo:
        circle = Circle(diameter)
        del circle
    assert str(excinfo.value) == fixture_negative_side


@pytest.mark.parametrize("diameter", [2])
def test_sum_with_incorrect_class(diameter, fixture_incorrect_type, fixture_test_class):
    circle = Circle(diameter)
    print(fixture_test_class)
    with pytest.raises(TypeError) as excinfo:
        circle.add_square(fixture_test_class())
        del circle
    assert str(excinfo.value) == fixture_incorrect_type
