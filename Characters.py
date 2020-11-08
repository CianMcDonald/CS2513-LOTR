class Character:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def __str__(self):
        return "{} {}".format(self.name, self.strength)

    def __gt__(self, other):
        if self.strength > other.strength:
            return True
        else:
            return False

    def fight(self, other):
        if self > other:
            self.strength += 1
            print(self)
        elif other > self:
            other.strength += 1
            print(other)
        else:
            other.strength -= 0.5
            self.strength -= 0.5

    # getters and setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) != str:
            print("type ERROR")
        else:
            self._name = value

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, value):
        if type(value) != float:
            print("type ERROR")
        elif value < 0:
            self._strength = 0.0
        elif value > 5:
            self._strength = 5.0
        else:
            self._strength = value


class Human(Character):
    def __init__(self, name, strength, kingdom):
        super().__init__(name, strength)
        self.kingdom = kingdom

    def __str__(self):
        return "{} {} {}".format(self.name, self.strength, self.kingdom)

    def fight(self, other):
        if isinstance(other, Human):
            print("fight ERROR")
    # getter and setters
    @property
    def kingdom(self):
        return self._kingdom

    @kingdom.setter
    def kingdom(self, value):
        if type(value) != str:
            print("type ERROR")
        else:
            self._kingdom = value


class Orc:
    pass


class Knight:
    pass


class Archer:
    pass