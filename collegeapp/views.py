from django.shortcuts import render

# Create your views here.
class food():

    
    
    def __init__(s, fruit, color):
        s.fruit = fruit
        s.color = color
        # print("fruit is", fruit)
        # print("color is", self.color )

    def show(self):
        print("fruit is", self.fruit)
        print("color is", self.color )


apple = food("apple", "red")
grapes = food("grapes", "green")
apple.show()
grapes.show()

class this_is_class:

    def show(in_place_of_self):
        print("It is not a keyword "
        "and you can use a different keyword")
   
object = this_is_class()
object.show()

    