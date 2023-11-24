from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Ham ham")

    def sleep(self):
        print('ZZZZ')


class Cat(Animal):

    def sound(self):
        print("Miau miau")

    def sleep(self):
        print("Prrrr")


cat = Cat()
dog = Dog()