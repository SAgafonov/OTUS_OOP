import pytest


def pytest_generate_tests(metafunc):
    if "fixture_triangle_scalene" in metafunc.fixturenames:
        metafunc.parametrize("fixture_triangle_scalene", [
            (2, 3, 4)
        ])

    if "fixture_triangle_isosceles" in metafunc.fixturenames:
        metafunc.parametrize("fixture_triangle_isosceles", [
            (1, 3, 3)
        ])

    if "fixture_triangle_equilateral" in metafunc.fixturenames:
        metafunc.parametrize("fixture_triangle_equilateral", [
            (3, 3, 3)
        ])

    if "fixture_negative_side" in metafunc.fixturenames:
        metafunc.parametrize("fixture_negative_side", [
          "Value must be greater than zero"
        ])

    if "fixture_triangle_not_exists" in metafunc.fixturenames:
        metafunc.parametrize("fixture_triangle_not_exists", [
          "Triangle does not exist"
        ])

    if "fixture_rectangle_not_exists" in metafunc.fixturenames:
        metafunc.parametrize("fixture_rectangle_not_exists", [
          "It's not a Rectangle"
        ])

    if "fixture_square_not_exists" in metafunc.fixturenames:
        metafunc.parametrize("fixture_square_not_exists", [
          "It's not a Square"
        ])

    if "fixture_incorrect_type" in metafunc.fixturenames:
        metafunc.parametrize("fixture_incorrect_type", [
          "Incorrect class is provided"
        ])


class ToTestException:
    pass


@pytest.fixture()
def fixture_test_class():
    return ToTestException


#
# @pytest.fixture()
# def fixture_triangle_scalene():
#     return 2, 3, 4
#
#
# @pytest.fixture()
# def fixture_triangle_isosceles():
#     return 1, 3, 3
#
#
# @pytest.fixture()
# def fixture_triangle_equilateral():
#     return 3, 3, 3
