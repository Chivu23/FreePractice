"""
define a class name "Practice", that:
- have 2 attribute on object ( init): a. b
-method:
    - sum
    - reduction
    - multiplication
    - division
"""


class Practice:

    # initialization method /  construct
    def __init__(self, a, b):
        self.a = a          # def attrib a take val a from constructor
        self.b = b          # def attrib b take val from b value from constructor

    def sum(self):
        return self.a + self.b

    def reduction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            return "Life is good with or without division to 0 (ZERO)!"


