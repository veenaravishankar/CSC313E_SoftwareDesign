import math


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_area(self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * pow(self.radius, 2)

    def get_volume(self):
        return math.pi * pow(self.radius, 2) * self.height

    def set_radius(self, radius):
        self.radius = radius

    def set_height(self, height):
        self.height = height


# The test function to be executed by PyTest
def test_normal_case():
    cylinder = Cylinder(5.2, 8.1)
    assert cylinder.get_area() == 434.5450958445402, "incorrect area"

#volume 688.08