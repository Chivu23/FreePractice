class School:
    def __init__(self, _name, study, year):
        self._name = "Raul"      # ---> protected - accessible within the class and it's subclasses
        self.__study = "math"    # ---> private - accessible only within a class
        self.year = year         # ---> public - accessible with or outside a class

    def read(self):
        print("Name:", self._name, 'study', self.__study)

    # method
    def write(self):
        print(self._name, 'was born in', self.year)


# creating object of a class
student = School('Maria', "math", 2000)

# calling public method of the class
student.read()
student.write()
