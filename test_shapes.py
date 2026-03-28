import pytest
import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# ТЕСТЫ ДЛЯ КРУГА

def test_circle_creation_positive_radius():
    circle = Circle(5)
    assert circle.radius == 5


def test_circle_negative_radius():
    with pytest.raises(ValueError, match="Radius must be positive."):
        Circle(-1)


def test_circle_zero_radius():
    with pytest.raises(ValueError, match="Radius must be positive."):
        Circle(0)


@pytest.mark.parametrize("radius,expected_area", [
    (1, 3.14159),
    (2, 12.56637),
    (2.5, 19.63495),
    (10, 314.15927),
    (0.5, 0.78540),
])
def test_circle_area(radius, expected_area):
    circle = Circle(radius)
    assert round(circle.area(), 5) == expected_area


@pytest.mark.parametrize("radius,expected_perimeter", [
    (1, 6.28319),
    (2, 12.56637),
    (2.5, 15.70796),
    (10, 62.83185),
    (0.5, 3.14159),
])
def test_circle_perimeter(radius, expected_perimeter):
    circle = Circle(radius)
    assert round(circle.perimeter(), 5) == expected_perimeter


# ТЕСТЫ ДЛЯ ПРЯМОУГОЛЬНИКА

def test_rectangle_creation_positive_dimensions():
    rectangle = Rectangle(4, 5)
    assert rectangle.width == 4
    assert rectangle.height == 5


@pytest.mark.parametrize("width,height", [
    (-1, 5),
    (5, -1),
    (-2, -3),
    (0, 5),
    (5, 0),
])
def test_rectangle_negative_or_zero_dimensions(width, height):
    with pytest.raises(ValueError, match="Width and height must be positive."):
        Rectangle(width, height)


@pytest.mark.parametrize("width,height,expected_area", [
    (4, 5, 20),
    (2.5, 3, 7.5),
    (10, 10, 100),
    (1, 1, 1),
    (3.5, 2, 7.0),
])
def test_rectangle_area(width, height, expected_area):
    rectangle = Rectangle(width, height)
    assert rectangle.area() == expected_area


@pytest.mark.parametrize("width,height,expected_perimeter", [
    (4, 5, 18),
    (2.5, 3, 11.0),
    (10, 10, 40),
    (1, 1, 4),
    (3.5, 2, 11.0),
])
def test_rectangle_perimeter(width, height, expected_perimeter):
    rectangle = Rectangle(width, height)
    assert rectangle.perimeter() == expected_perimeter


# ТЕСТЫ С ФИКСТУРОЙ

@pytest.fixture
def circle():
    return Circle(1)


def test_circle_fixture_area(circle):
    assert circle.radius == 1
    assert round(circle.area(), 5) == 3.14159


def test_circle_fixture_perimeter(circle):
    assert round(circle.perimeter(), 5) == 6.28319


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
