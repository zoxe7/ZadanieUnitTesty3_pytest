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
