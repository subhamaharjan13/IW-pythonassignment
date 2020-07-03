# Imagine you are creating a Super Mario game. You need to define a class to represent Mario. 
# What would it look like? If you aren't familiar with SuperMario, use your own favorite video 
# or board game to model a player.

class SuperMario:

    name = "Mario"
    color = "Red"

    def __init__(self):
        self.level = 3
        self.move = self.Movements()

    def display(self):
        maxlevel = 5
        if self.level < maxlevel:
            print("Welcome to Level ",self.level)
        else:
            print("Sorry, We have only upto level ",maxlevel)

        self.move.displayMovements()
        self.move.levelComplete()

    @classmethod
    def characterInfo(cls):
        print("Your character name is",cls.name)
        print("Your character color is",cls.color)


    class Movements:                                                    #Inner Class
        def __init__(self):
            self.move_right = 3
            self.move_left = 4
            self.go_up = 2
            self.go_down = 1

        def displayMovements(self):
            print("Move Right =",self.move_right)
            print("Move Left =",self.move_left)
            print("Jump =",self.go_up)
            print("Down =",self.go_down)

        def levelComplete(self):
            if self.move_right + self.move_left + self.go_down + self.go_up >= 10:
                print("Level Completed")



mario = SuperMario()
SuperMario.characterInfo()
mario.display()
