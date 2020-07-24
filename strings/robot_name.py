import random
from string import ascii_uppercase, digits

class Robot:
    existingBots = []
    
    def __init__(self):
        self.newName()
        self.__class__.existingBots.append(self)
            
    def newName(self):
        while True:
            newName = ''.join(random.choices(ascii_uppercase, k=2)) + ''.join(random.choices(digits, k=3))
            if (newName not in [bot.name for bot in Robot.existingBots]):
                self.name = newName
                break
               
    def reset(self):
        self.newName()
