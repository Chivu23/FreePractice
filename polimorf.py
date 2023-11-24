# Polymorphism

class Fruits:
    def healty(self):
        print("apple", "bananas", "music")


class Vegetables:
    def healty(self):
        print("sun", "avocado", "goodLife")


life_fruits = Fruits()
life_vegetables = Vegetables()

life_fruits.healty()
life_vegetables.healty()