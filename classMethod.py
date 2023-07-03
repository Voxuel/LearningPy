class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):

        @classmethod
        def adding_things(cls, num1, num2):
            return cls('Joe', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


print(PlayerCharacter.adding_things2(2, 3))
