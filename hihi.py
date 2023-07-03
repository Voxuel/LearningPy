# OOP


class PlayerCharacter:
    # Class obj attribute
    membership = True

# self used as instance specific attribute and is a bit comparable to C# "this"
    def __init__(self, name):
        self.name = name

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('Joe')
player2 = PlayerCharacter('Bob')
print(player1.name)
print(player2.name)

