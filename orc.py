class Orc:
    def __init__(self, name, strength, weapon):
        self.name = name
        self.strength = strength
        self.weapon = weapon

    def __str__(self):
        return "{} {} {}".format(self.name, self.strength, self.weapon)

    def __gt__(self, other):
        if self.weapon and not other.weapon:
            return True
        elif self.strength > other.strength:
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

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, value):
        if type(value) != bool:
            print("type ERROR")
        else:
            self._weapon = value



