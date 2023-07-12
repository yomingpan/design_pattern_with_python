"""
這段程式碼展示了一個使用工廠模式（Factory Pattern）的遊戲環境。以下是重點和需要注意的事項：

重點：

1. 工廠模式：這個程式碼展示了如何使用工廠模式來創建不同的角色和障礙物，具體是FrogWorld和WizardWorld兩個具體工廠類別。
2. 角色和障礙物：程式碼中定義了Frog、Bug、Wizard和Ork四個類別，分別代表了遊戲中的角色和障礙物。
3. 遊戲環境：GameEnvironment類別負責創建遊戲的角色和障礙物，並讓它們進行互動。

注意事項：

1. 了解類別之間的關係：觀察各個類別之間的關聯關係，特別是FrogWorld和WizardWorld這兩個具體工廠類別，它們都實現了相同的介面，但創建的角色和障礙物不同。
2. 觀察方法的實現：注意每個類別中的方法實現，特別是interact_with和action方法，它們定義了角色和障礙物之間的交互行為。
3. 理解程式碼流程：main函數是程式的入口，它根據玩家的年齡判斷使用FrogWorld還是WizardWorld這兩個工廠來創建遊戲環境。
"""

class Frog:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Frog encounters {} and {}!'.format(self,
                                                         obstacle,
                                                         obstacle.action()))


class Bug:

    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld:

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Frog World ———'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {}!'.format(self, obstacle, obstacle.action()))


class Ork:

    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizardWorld:

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Wizard World ———'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnvironment:

    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = input('Welcome {}. How old are you? '.format(name))
        age = int(age)
    except ValueError as err:
        print("Age {} is invalid, please try \
        again…".format(age))
        return (False, age)
    return (True, age)


def main():
    name = input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()

if __name__ == '__main__':
    main()
