class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        if self.num_arrows == 0:
            print('out of arrows!')
        self.num_arrows -= 1
        print(f'attacking with bow, {self.num_arrows} left')

wizard = Wizard('Tim', 193)
archer = Archer('Bowman', 10)

wizard.attack()
archer.attack()
