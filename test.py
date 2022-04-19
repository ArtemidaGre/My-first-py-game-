#тестовый вариант новой боевой системы


import time as t
from tokenize import Name
from unicodedata import name



def fight_n(hp, damage, ehp, edamage):
    start_hp=hp
    import time as t
    print('Бой начинается!')
    print('у вас', hp, 'hp, и', damage, 'урона\nу врага', ehp, 'hp, и', edamage, 'урона')
    t.sleep(0.5)
    import random as r
    while hp>=1 and ehp>=1:
        luck=r.randint(0, 100)
        if luck>=51:
            to_damage=r.randint(0, damage)
            ehp=ehp-to_damage
            print('вы ударили противника на', to_damage, 'урона, у него осталость', ehp, 'hp')
            t.sleep(0.5)
        elif luck<=50:
            print('Вы промахнулисть')
            t.sleep(0.5)
        luck2=r.randint(0, 100)
        if luck2>=51:
            to_damage2=r.randint(0, edamage)
            hp=hp-to_damage2
            print('враг вас ударил на', to_damage2, 'урона, у вас осталость', hp, 'hp')
            t.sleep(0.5)
        elif luck2<=50:
            print('враг промахнулся')
            t.sleep(0.5)
    if hp<=0:
        win=0
        print('вы проиграли')
    elif hp>>0:
        win=1
        print('Победа!!!')
    t.sleep(0.5)

fight_n(int(input('hp=')), int(input('damage=')), int(input('ehp=')), int(input('edamage=')))
t.sleep(10)

name='Амогус'
historylist=['amogus', 'gus', 'amo', 17]
fin=str(input('введите что нибудь, для завершения игры.\n'))
final=open('final.txt', 'a')
final.write(name, historylist)

