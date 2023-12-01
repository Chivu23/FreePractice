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


def get_healty_life(fruits_vegeta):
    fruits_vegeta.healty()


get_healty_life(life_fruits)
get_healty_life(life_vegetables)
