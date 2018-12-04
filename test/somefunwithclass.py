class Animal():
    test = "a"
    def __init__(self) -> None:
        self.name = "a"
        self.numberLeg = 2
        self.old = 2
        self.kind = None
        self.test

    def getNumberOfLeg(self):
        if (self.kind == 1):
            return 2 * self.numberLeg
        else:
            return 4 * self.numberLeg
    @property
    def sound(self):
        return "a"
    def __info(self):
        print(self.name + "a")

class Dog(Animal):
    color = "white"

    def __init__(self) -> None:
        super().__init__()
        self.name = "dog"
        self.kind = 1
        self.numberLeg = self.getNumberOfLeg()
        self.old = 20
    def __info(self):
        print (self.name)

dog = Dog()
print(dog.sound)
dog._Animal__info()
dog._Dog__info()
print(dog.getNumberOfLeg())