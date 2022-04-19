#Хватит читать коды игры!
#Я серьезно, хватит!
#ладно...
#если ты все еще читаешь, ПРЕКРАТИ!
#ну если ты НАСТОЛЬКО хочешь увидеть код игры...
#я дам только несколько функций из игры)))

class Game():
    def bazar(wish1, w1c, coins):
        import random as r
        global torg
        torg=0
        print('Вы можете купить', wish1, 'за', w1c,'рублей!')
        choise=str(input('Купить '+wish1+'?\n>>>'))
        if choise=='да':
            if coins>=w1c:
                print('Вы можете купить это!')
                choise=str(input('торговаться?\n>>>'))
                if choise=='да':
                    while True:
                        torgm=int(input('до скольки вы хотите скинуть цену?\n>>>'))
                        if torgm>=(w1c/2.1):
                            print('Вы начали торги!')
                            torg=r.randint(0,100)
                            if torg>=80:
                                print('У вас получилось!')
                                w1c=torgm
                                if coins>=w1c:
                                    coins=coins-w1c
                                    torg=1
                                    break
                                elif coins<<w1c:
                                    print("у вас слишком мало денег!")
                            elif torg>=50:
                                print('У вас почти получиось!')
                                w1c=torgm+(w1c/5)
                            elif torg<=50:
                                print('У вас не получилось')
                elif choise=="нет":
                    print("♂fuck you♂")
        elif choise=="нет":
            print("♂fuck you♂") 
    def battle(hp, damage, ehp, edamage):
        start_hp=hp
        global win
        import time as t
        print('Бой начинается!')
        print('у вас', hp, 'hp, и', damage, 'урона\nу врага', ehp, 'hp, и', edamage, 'урона')
        t.sleep(0.5)
        import random as r
        while hp>=1 and ehp>=1:
            if hp>=1:
                luck=r.randint(0, 100)
                if luck>=21:
                    to_damage=r.randint(0, damage)
                    ehp=ehp-to_damage
                    print('вы ударили противника на', to_damage, 'урона, у него осталость', ehp, 'hp')
                    t.sleep(0.3)
                elif luck<=20:
                    print('Вы промахнулисть')
                    t.sleep(0.3)
                luck2=r.randint(0, 100)
            if ehp>=1:
                if luck2>=41:
                    to_damage2=r.randint(0, edamage)
                    hp=hp-to_damage2
                    print('враг вас ударил на', to_damage2, 'урона, у вас осталость', hp, 'hp')
                    t.sleep(0.3)
                elif luck2<=40:
                    print('враг промахнулся')
                    t.sleep(0.3)
        if hp<=0:
            win=0
            print('вы проиграли!!!')
        elif hp>>0:
            win=1
            print('Победа!!!')
        t.sleep(0.5)
    def battlebig(hp, damage, ehp, edamage):
        start_hp=hp
        global win
        import time as t
        print('Бой начинается!')
        print('у вас', hp, 'hp, и', damage, 'урона\nу врага', ehp, 'hp, и', edamage, 'урона')
        t.sleep(0.5)
        import random as r
        while hp>=1 and ehp>=1:
            luck=r.randint(0, 100)
            if luck>=21:
                to_damage=r.randint(0, damage)
                ehp=ehp-to_damage
                print('вы ударили противника на', to_damage, 'урона, у него осталость', ehp, 'hp')
                t.sleep(0.3)
            elif luck<=20:
                print('Вы промахнулисть')
                t.sleep(0.3)
            luck2=r.randint(0, 100)
            if luck2>=41:
                to_damage2=r.randint(0, edamage)
                hp=hp-to_damage2
                print('враг вас ударил на', to_damage2, 'урона, у вас осталость', hp, 'hp')
                t.sleep(0.3)
            elif luck2<=40:
                print('враг промахнулся')
                t.sleep(0.3)
        if hp<=0:
            win=0
            print('вы проиграли!!!')
        elif hp>>0:
            win=1
            print('Победа!!!')
        t.sleep(0.5)
        global ghp
        ghp=hp


class subfunc():
    def decode(to_dec):
        #decode file
        import time as t
        wait1=0
        true_1='qmodgcbr'
        true_2='&$!^*^&$@(^%#@%!$^$^!(&$($!!^$!#(%&*'
        to_decode=str(input('what i must decode?\n>>>'))
        if to_decode==true_1:
            while wait1<=10:
                print('...', end='')
                t.sleep(1)
            print('82467139')
        if to_decode==true_2:
            while wait1<=10:
                print('...', end='')
                t.sleep(1)
            print('ну очень крутая хрень которую можно взять')