# Imagine you are creating a Super Mario game. You need to define a class to represent Mario. 
# What would it look like? If you aren't familiar with SuperMario, use your own favorite video 
# or board game to model a player.

class SuperMario:

    name = "Mario"
    color = "Red"

    def __init__(self):
        self.level = 3
        self.move = self.Movements()

    # display level and movements of character
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
        print("Your character name is {} \nYour character color is {}"
                .format(cls.name,cls.color))

    #Inner Class
    class Movements:
        def __init__(self):
            self.move_right,self.move_left = 3, 4
            self.go_up, self.go_down = 2, 1

        def displayMovements(self):
            print("Move Right = {} \nMove Left = {} \nJump = {} \nDown = {}"
                        .format(self.move_right,self.move_left,self.go_up,self.go_down))

        def levelComplete(self):
            if self.move_right + self.move_left + self.go_down + self.go_up >= 15:
                print("Level Completed")
            elif self.move_right + self.move_left + self.go_down + self.go_up < 15:
                print("You need to go a little bit further to complete the level")


mario = SuperMario()
SuperMario.characterInfo()
mario.display()
