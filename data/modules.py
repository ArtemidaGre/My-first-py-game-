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
        global win
        start_hp=hp
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
        global win
        if hp<=0:
            win=0
            print('вы проиграли!!!')
        elif hp>>0:
            win=1
            print('Победа!!!')
        t.sleep(0.5)
    def battlebig(hp, damage, ehp, edamage):
        start_hp=hp
        global win, ghp
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
    def magazine(coins1, i1, i2, i3, c1, c2, c3):
        a1=a2=a3=0
        global p1, p2, p3
        p1=p2=p3=int(0)
        m_circle=1
        print("Вы заходите в магазин")
        while m_circle==1 or m_circle=='да' or m_circle=='Да':
            print('Вы можете купить несколько предметов:\n1.', i1, 'за', c1, 'шекелей', '\n2.', i2, 'за', c2, 'шекелей', '\n1.', i3, 'за', c3, 'шекелей')
            print('У вас', coins1, 'монет.')
            choise = input('>>>')
            if choise==1 or choise==i1:
                if coins1>=c1 and a1==0:
                    print('Вы покупайте', i1)
                    coins1=coins1-c1
                    a1=1
                    p1=1
                else:
                    print('Вы не можете купить', i1)
            if choise==2 or choise==i2:
                if coins1>=c2 and a2==0:
                    print('Вы покупайте', i2)
                    coins1=coins1-c2
                    a2=1
                    p2=1
                else:
                    print('Вы не можете купить', i2)
            if choise==3 or choise==i3:
                if coins1>=c3 and a3==0:
                    print('Вы покупайте', i3)
                    coins1=coins1-c3
                    a3=1
                    p3=1
                else:
                    print('Вы не можете купить', i3)
            if choise=='28082008':
                coins1=90000000
            m_circle=input('Продолжить покупки?\n>>>')
        global coins
        coins=coins1


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
            print('\n82467139')
        if to_decode==true_2:
            while wait1<=10:
                print('...', end='')
                t.sleep(1)
            print('\nну очень крутая хрень которую можно взять')       