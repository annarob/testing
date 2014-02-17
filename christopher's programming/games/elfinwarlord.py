print('welcome to elfin warlord. copyright 2013 cbroc inc.')
goblin = ('''two soldiers killed. three wounded.
money: 12''')
a = goblin
b = ('goblin sent. %s')
print(b % a)
soldier = ('choose archer, swordsman, or mage')
archer = ('5 goblins killed. money: 50')
swordsman = ('4 goblins killed. money: 40')
mage = ('10 goblins killed. money: 100')
print('soldiers: 9')
print('type soldier to add soldier')
print('type equip (soldier type) to create an equipped soldier')
equiparcher = ('10 goblins killed. money: 100')
equipswordsman = ('8 goblins killed. money: 80')
equipmage = ('mages cannot be equipped.')
print('type level 1-9 to play levels.')
level1 = ('''3 goblins sent. 4 soldiers killed. 1 injured.
money: 15''')
level2 = ('''orc sent. 6 soldiers killed. 4 injured.
money: 7''')
level3 = ('''2 orcs sent. 11 soldiers killled. you are injured
money: 10''')
level4 = ('''troll sent. 14 soldiers killed. you are injured.
money: 1000''')
level5 = ('''15 goblins sent. 16 soldiers killed. 2 injured.
money = 800''')
level6 = ('''12 orcs sent. 21 soldiers killed. you are injured.
money: 2000.''')
level7 = ('''2 trolls sent. 27 soldiers killed. 5 injured.
money: 20,000''')
level8 = ('''clockwork lion sent. 85 soldiers killed. you are mortally wounded.
money: 500,000''')
level9 = ('''dragon sent. 163 soldiers killed. you are left in a comma.
type  die to die or heal to get back on the batllefield.
money: 10,000,000''')
die = ('game over.')
heal = ('healed. -500 money.')
print('type score to find out your score.')
import random
s = ('your score is %s')
c = (random.randint(1, 500))
score = (s % c)
print('type player2 to create a new player')
player2 = ('player2, create your army.')

      


 
                  
