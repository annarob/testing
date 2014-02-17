import random
print('Welcome to Cheeseland')
money = 25
print('Buy mousies and fight kitties!')
print('Mousie price: 5$.')
print('money: 25$')
print('get 5 mousies to fight a kitty')
chance = ['win', 'lose']
print('type buy(item) to buy something')
yes = 1
class charachter():
    pass
class mousie(charachter):
    def attack(mousies):
        if mousies == chance:
            print('fighting kitty')
            status = random.choice(mousies)
            if status == 'win':
                print('you win')
                money2 = random.randint(50, 100)
                print(str(money2))
            if status == 'lose':
                print('you lose')
def buy(item):
    if item == mousie:
        print('bought 5 mousies')
        m = mousie()
        money2 = (money - 25)
        print(str(money2))
        print('want to attack?')
        response = input()
        if response == yes:
            m.attack(chance)

                

        
        
    
