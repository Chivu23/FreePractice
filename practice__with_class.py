from practice_class import Practice  # route from import => different type of file


class Complex:

    def __init__(self, real, imagine):
        self.r = real
        self.i = imagine


z = Complex(7.0, -2)

calc1 = Practice(a=2, b=3)
print(calc1.a)
print(calc1.b)
print(calc1.sum())
print(calc1.reduction())
print(calc1.multiplication())
print(calc1.division())

calc2 = Practice(a=20, b=0)
print(calc2.division())
