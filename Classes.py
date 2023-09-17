import random

class Team:
    def __init__(self, name, condition) -> None:
        self.name = name
        self.condition = condition
    
    def conFunc(self):
        self.condition = random.randrange(1, 5)
        return self.condition


class Boon:
    def __init__(self, name, effect) -> None:
        self.name = name
        self.effect = effect
    
    def boonFunc(self):
        target = random.randrange(1, 5)
        return target
        
       