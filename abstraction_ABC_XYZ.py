from abc import ABC, abstractmethod


class School(ABC):

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def read(self):
        pass


class Student(School):

    def write(self):
        print("Everyday something new")

    def read(self):
        print("Minimum 20 pages per a day")


class Teacher(School):

    def write(self):
        print("Always true and deep things")

    def read(self):
        print("How to make learning a gift")


student = Student()
teacher = Teacher()