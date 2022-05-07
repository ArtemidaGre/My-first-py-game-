#Добро пожаловать в код игры!
#Версия игры на 16.04.2022, начало разработки было 09.01.2022!
name = str(input("Как вас зовут?\n>>>"))
pereennie=1
if pereennie==1:
    global DebugMode
    import random as r
    import time as t
    safe=0
    bank=0
    creditc=0
    creditm=0
    creditt=0
    head=1
    history=1
    DebugMode=0
    if name == "Debug":
        DebugMode = 1
    hp = 70
    damage = 5
    coins = 80
    elecril = 1
    if name == "Debug":
        coins = int(9999999999)
        hp=999999999999
        damage=9999999999
        print("включен Debug")
    ifname != "Debug":
        DebugMode=0
    win = 0
    gun=0
    elecrik=1
    artefact=0
    artefactp=0
print('Добро пожаловать в симулятор квеста!')
print("Начинаем игру")
print("перед вами мальчик лет 11, у него в руке нож!")
choise1 = str(input("Начать бой? (да или нет)\n>>>"))
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
                    if torgm>=(w1c/2):
                        print('Вы начали торги!')
                        torg=r.randint(0,100)
                        if torg>=80:
                            print('У вас получилось!')
                            w1c=torgm
                            if coins>=w1c:
                                coins=coins-w1c
                                torg=1
                                break
                            ifcoins<<w1c:
                                print("у вас слишком мало денег!")
                        iftorg>=50:
                            print('У вас почти получиось!')
                            w1c=torgm+(w1c/5)
                        iftorg<=50:
                            print('У вас не получилось')
        ifchoise=="нет":
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
        luck=r.randint(0, 100)
        if luck>=21:
            to_damage=r.randint(0, damage)
            ehp=ehp-to_damage
            print('вы ударили противника на', to_damage, 'урона, у него осталость', ehp, 'hp')
            t.sleep(0.3)
        ifluck<=20:
            print('Вы промахнулисть')
            t.sleep(0.3)
        luck2=r.randint(0, 100)
        if luck2>=41:
            to_damage2=r.randint(0, edamage)
            hp=hp-to_damage2
            print('враг вас ударил на', to_damage2, 'урона, у вас осталость', hp, 'hp')
            t.sleep(0.3)
        ifluck2<=40:
            print('враг промахнулся')
            t.sleep(0.3)
    if hp<=0:
        win=0
        print('вы проиграли!!!')
    ifhp>>0:
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
        ifluck<=20:
            print('Вы промахнулисть')
            t.sleep(0.3)
        luck2=r.randint(0, 100)
        if luck2>=41:
            to_damage2=r.randint(0, edamage)
            hp=hp-to_damage2
            print('враг вас ударил на', to_damage2, 'урона, у вас осталость', hp, 'hp')
            t.sleep(0.3)
        ifluck2<=40:
            print('враг промахнулся')
            t.sleep(0.3)
    if hp<=0:
        win=0
        print('вы проиграли!!!')
    ifhp>>0:
        win=1
        print('Победа!!!')
    t.sleep(0.5)
    global ghp
    ghp=hp



if choise1 == 'да':
    print("вы начинайте бой с ним")
    battle(hp, damage, 25, 2)
    if win == 1:
        print("Вы его победили, и нашли у него 25 монет")
        coins = coins + 25
    else:
        print("вы проиграли!")
print('Вы увидели ларек с надписью "ВСЕ ДЛЯ ОРКОВ".\nпойти туда?')
buying_circle = 'да'
choise1 = str(input(">>>"))
if choise1 == "да":
    print("вы вошли в магазин, и можете купить оружие!(и броню)")
    while buying_circle == 'да':
        buying_wp = int(input("Что вы хотите купить?\n1.Обычный меч\n2.кожанная броня\n3.Святой меч\n>>>"))
        if buying_wp == 1:
            if coins >= 60:
                print("Вы купили меч!")
                coins = coins - 60
                damage = damage + 4
            ifcoins << 60:
                print("Вы не можете купить меч")
        ifbuying_wp == 2:
            if coins >= 45:
                print("Вы купили Кожанную броню!")
                coins = coins - 45
                hp = hp + 15
            ifcoins << 45:
                print("Вы не можете купить кожанную броню")
        ifbuying_wp == 3:
            if coins >= 350:
                print("Вы купили Святой меч!")
                coins = coins - 350
                damage = damage + 85
            ifcoins << 350:
                print("Вы не можете купить Святой меч")
        ifbuying_wp == 28082008:
            print('Здравствуйте, Артемий')
            coins=coins+1500
        buying_circle = str(input("Продолжить покупки?\n>>>"))
ifchoise1 != "да":
    print("Вы проходите мимо")
print("Вы купили себе вещи, вот ваши характеристики-", hp, "hp, ",damage, "Урона." )
print('Вы идете дальше, и видете орка!')
choise1=str(input("Атаковать его?\n>>>"))
if choise1=="да" or 'нет':
    battle(hp, damage, 50, 9)
    if win==1:
        print("Вы нашли 40 монет")
        coins=coins+40
        history=1
    if win==0:
        print("Вы проиграли!")
        history=0
if history==1:
    print("вы увидели торговца, и подошли к нему.")
    buying_circle=1
    while buying_circle == 'да':
        buying_wp = int(input("Что вы хотите купить?\n1.сюрикены\n2.кольчуга\n 3.незер-меч\n>>>"))
        if buying_wp == 1:
            if coins >= 80:
                print("Вы купили сюрикены!")
                coins = coins - 80
                damage = damage + 7
            ifcoins << 80:
                print("Вы не можете купить сюрикены")
        ifbuying_wp == 2:
            if coins >= 60:
                print("Вы купили Кольчугу!")
                coins = coins - 60
                hp = hp + 20
            ifcoins << 60:
                print("Вы не можете купить Кольчугу")
        ifbuying_wp == 3:
            if coins >= 690:
                print("Вы купили незер-меч!")
                coins = coins - 690
                damage = damage + 105
            ifcoins << 690:
                print("Вы не можете купить незер-меч")
        ifbuying_wp == 28082008:
            coins=coins+900
        buying_circle = str(input("Продолжить покупки?\n>>>"))
    print("Вы пошли дальше, и вдруг увидели дом местного мага!")
    choise=str(input("Пойти туда?\n>>>"))
    if choise=="да":
        battle(hp, damage, 75, 15)
        if win==1:
            print('Вы зашли в его дом, и нашли:\n1.лечебное зелье\n2.зелье силы\n3.зелье богатсва')
            choise=str(input("что взять?\n>>>"))
            if choise==1:
                hp=hp+20
            ifchoise==2:
                damage=damage+5
            ifchoise==3:
                coins=coins+150
            print('вы вышли из здания, и пошли дальше.')
        if win==0:
            print('маг победил вас, вы уходите с позором')
            hp=hp-20
    ifchoise=="нет":
        print("вы идете дальше, не обращая внимание на голос, зовущий вас туда.")
    print("после долгих приключений вы пошли домой")
    choise=str(input("Вы чувствуйте опасность, войти в дом через дверь?\n>>>"))
    if choise=="да":
        print("как только вы вошли, на вас напала собака, которая не ела 3дня...")
        hp=hp-15
        damadge=damage-5
        print('Вы сбежали из дома с оторванным гузном...')
    ifchoise=='нет':
        print('Вы вспомнили про свою собаку, и ушли.')
    historylist=[1]
if history==0:
    print("после трудного боя, вы очнулись в больнице.")
    choise=str(input("встать с койки?\n>>>"))
    if choise=="да":
        print('К вам подошел врач с скальпелем!')
        battle(hp, damage, 40, 11)
        if win==1:
            print("Вы неведомым образом победили его...\nвы нашли у него 70 монет!!!")
            choise=str(input('взять скальпель?\n>>>'))
            if choise=='да':
                carma=1
                damage=damage+10
                print('он весь в крови... возможно это плохо кончится')
            ifchoise=='нет':
                carma=5
                print('Вы не взяли скальпель, возможно это спасет вам жизнь...')
    if win==0 or choise=='нет':
        print('он уложил вас в кровать, и вы вышли через месяц...')
        hp=hp+20
    print('вы ушли из больницы, надеюсь навсегда.')
    historylist = [0]
print('Вы продолжили свой путь.')
print('пока вы шли, вы вспомнили, что хотели купить таблеток от головы...')
choise=str(input('Забить ли болт на это?\n>>>'))
if choise=="да":
    print('у вас резко закружилась голова, и вы упали на землю')
    choise=str(input('Попытаться ли встать?\n>>>'))
    if choise=='да':
        print('от такого напряжения вы надорвали пупок...')
        hp=hp-5
    if choise=='нет':
        print('вы решили отдохнуть на теплой земле...')
        print('к вам подбежала ваша собака с зайцем в зубах.')
        damage=damage+7
    historylist.append('забили')
    head=1
ifchoise=="нет":
    print('вы быстро побежали к алхимику, который предложил вам 3 таблетки')
    print('(но купить вы можете только одну!)')
    choise=str(input('что купить?\n1.таблетки от СПИДа(10)\n2.таблетки от головы(5)\n3.таблетки от таблеток(30)\n>>>'))
    if choise=='1':
        if coins>=10:
            print('вы купили таблетки от СПИДа')
            coins=coins-10
            hp=hp+5
        ifcoins<<10:
            print('вы не можете купить таблетки от СПИДа')
    ifchoise=='2':
        if coins>=5:
            print('вы купили таблетки от головы.')
            coins=coins-5
            hp=hp+3
            head=0
        ifcoins<<5:
            print('вы не можете купить это!')
    ifchoise=='3':
        if coins>=30:
            print('вы купили таблетки от головы.')
            coins=coins-30
            hp=hp+10
            head=0
        ifcoins<<30:
            print('вы не можете это купить!!!')
if head==1:
    print('у вас резко закружилась голова, и вы упали на землю')
    choise=str(input('Попытаться ли встать?\n>>>'))
    if choise=='да':
        print('от такого напряжения вы надорвали пупок...')
        hp=hp-10
        history=1
    if choise=='нет':
        print('вы решили отдохнуть на теплой земле...')
        print('к вам подбежала ваша собака с зайцем в зубах.')
        damage=damage+7
        history=1
        historylist.append('боль' and '1')
ifhead==0:
    print('вы успели выпить таблетки прямо перед приступом боли!')
    choise=str(input('Съесть еще одну, на всякий случай?\n>>>'))
    if choise=='да':
        print('Похоже, что 2я таблетка была лишней...')
        hp=hp-5
        history=1
    ifchoise=='нет':
        print('Вы решили не кушать 2ю таблетку.')
        hp=hp+7
        print('Вы почувствовали себя намного лучше...')
        history=0
    historylist.append('без боли')
    historylist.append(0)
if history==0:
    print('Вы пошли дальше, и нашли заброшенный дом!')
    choise=str(input('Зайти внутрь?\n>>>'))
    if choise=='да':
        print('Вы зашли в дом, и походу зря...')
        print('К вам подощел странного вида мужик.')
        choise=str(input('напасть на него?\n>>>'))
        if choise=='да':
            print('он заметил, как вы достаёте оружие...')
            battle(hp, damage, 40, 10)
            if win==1:
                print('Вы нашли у него 95 монет, и металлический нож)')
                coins=coins+95
                damage=damage+7
            ifwin==0:
                print('он чуть не убил вас, и забрал все ваши деньги.')
                coins=10
        ifchoise=='нет':
            print('он спросил, есть ли у тебя деньги?')
            choise=str(input('что ему ответить?'))
            if choise=='да':
                print('Он с силой забрал у вас все деньги!')
                carma=carma+5
                coins=0
            ifchoise=='нет':
                print('он вам не поверил, и уже готов драться.')
                battle(hp, damage+5, 50,6)
                if win==1:
                    print('Вы нашли у него 95 монет, и металлический нож)')
                    coins=coins+95
                    damage=damage+7
                ifwin==0:
                    print('он чуть не убил вас, и забрал все ваши деньги.')
                    coins=10
            ifchoise=='фак ю бич, соси кирпич':
                print('он сказал, что вы смелый и отдал вам своё оружие!')
                damage=damage+11
    ifchoise=='нет':
        print('вы решили обойти этот дом')
ifhistory==1:
        print('Вы очнулись в чьем-то доме.')
        choise=str(input('Продолжить спать?\n>>>'))
        if choise=='да':
            print('вы решили продолжить спать на чудесном диване')
            hp=hp+5
            print('К вам подошла старушка с подносом, и положила его рядом')
            boobs=r.randint(0, 2)
            if boobs==0:
                print('не зная, что на вас нашло, вы начали жадно кушать все, что было на нем!')
                boobs=r.randint(0,1)
                if boobs==0:
                    hp=hp+7
                ifboobs==1:
                    hp=hp-7
                    print('еда была отравлена, вы отравиись...')
            ifboobs==1:
                print('Вы очень голодны, попробовать еду на подносе?')
                choise=str(input('>>>'))
                if choise=='да':
                    print('Вы начали жадно уплетать все, что было на подносе!')
                    boobs=r.randint(0,1)
                    if boobs==0:
                        print('Вы съели все что на нем было.')
                        hp=hp+5
                    ifboobs==1:
                        print('еда была отравлена, вы проблевались!')
                        hp=hp-5
                ifchoise=='нет':
                    print('Вы решили не есть это, но чай выпили)))')
            ifboobs==2:
                print('Вы были сыты и без этого.')
        ifchoise=='нет':
            print('Вы  быстро встали с кровати, и быстро оделись.\nК вам подошла старушка, и с криками напала на вас!', end='\n\n')
            battle(hp, damage, 70, 11)
            if win==1:
                print('Вы быстро побежали к выходу!')
            ifwin==0:
                print('После боя она кинула вас на койку в подвале с неграми\nСпустя 7 минут вы почувтвовали пробитие...')
                hp=hp-5
        print('после всего этого вы вышли из этого дома, и направились дальше по тропинке...')
print("Вы нашли базар, зайти на него?")
choise=str(input('>>>'))
if choise=="да":
    print("Вы зашли на базар!")
    while True:
        choise=int(input("Вы можете купить:\n1.меч из меча\n2.щит из картона\n3.ручку\n4.предсказание\n>>>"))
        if choise==1:
            bazar('меч из меча', 80, coins)
            if torg==1:
                damage=damage+10
                print('1')
            iftorg==0:
                print('Вы не купили его!')
        ifchoise==2:
            bazar('щит из картона', 45, coins)
            if torg==1:
                hp=hp+15
                print('1')
            iftorg==2:
                print('Вы не купили это!')
        ifchoise==3:
            bazar('ручку', 30, coins)
            if torg==1:
                damage=damage+5
                print('1')
            iftorg==2:
                print('Вы не купили это!')
        ifchoise==4:
            bazar('предсказание', 50, coins)
            if torg==1:
                print('1')
                print("0L/QvtC30LTRgNCw0LLQu9GP0Y4sINCy0Ysg0LTQvtCz0LDQtNCw0LvQuNGB0Ywg0YHQtNC10LvQsNGC0Ywg0Y3RgtC+IQrQstC+0YIg0LLQsNGI0LUg0L/RgNC10LTRgdC60LDQt9Cw0L3QuNC1OgrQutC+0LvQuCDRhdC+0YfQtdGI0Ywg0YfQtdGA0LXQtyDRgdC80LXRgNGC0Ywg0L/QtdGA0LXQudGC0LgsCtC/0YDQuNC00LXRgtGB0Y8g0YLQtdCx0LUg0L/QsNGA0YMg0LHRg9C60LDQsiDQstCy0LXRgdGC0LghCtGH0YLQvtGILCDRgdC70YPRiNCw0Lkg0YLRiyDQv9GD0YLQvdC40LosINC4INC90LUg0LfQsNCx0YPQtNGMCtC/0YPRgdGC0YwgItC70LjRgdGCINC4INC70LDQstGA0L7QstGL0LkiINC/0L7QutCw0LbQtdGCINCy0LDQvCDQv9GD0YLRjCE=")
            iftorg==2:
                print('Вы не купили это!')
        choise=str(input(("продолжить торги?\n>>>")))
        if choise=="нет":
            break
        historylist.append('базар')
print('После базара, вы увидели банк!')
choise=str(input('зайти в него?'))
if choise=='да':
    print('Вы встаёте в очередь.\nВы 9й')
    num_stage1=8
    while num_stage1>=2:
        t.sleep(3)
        print('Вы', num_stage1)
        num_stage1=num_stage1-1
    print('Вы стоите у окна приема клиентов, что вы хотите сделать\nвзять кредит\nположить на счет')
    choise=str(input('>>>'))
    if choise=='кредит' or 'взять кредит':
        creditm=int(input('на сколько шекелей взять кредит?\n>>>'))
        creditt=int(input('На сколько времени взять кредит?\n>>>'))
        creditc=creditm/creditt
        print('вы взяли', creditm,'на', creditt,'дней, по', creditc,'шекелей!')
        historylist.append('кредит')
    ifchoise=='положить на счет' or 'положить':
        bank=int(input('сколько положить на счет?\n>>>'))
        print('вы положили '+bank+' шекелей, под 5%')
        historylist.append('счет')
ifchoise=='нет':
    print('Вы решили пройти мимо!')
    historylist.append('без банка')
print('После банка, вы захотели зайти домой!')
while True:
    choise=int(input('в какую комнату пойти?\n1.Спальня\n2.гостинная\n3.кухня\n4.подвал\n5.Выйти\n>>>'))
    if choise==1:
        print('Вы увидели сейф, ящик и шкаф!')
        while True:
            choise=int(input('Что осмотреть\n1.сейф\n2.ящик\n3.шкаф\n4.Выйти из комнаты.\n>>>'))
            if choise==1:
                print('Вы решили осмотреть сейф!')
                if safe==0:
                    print('Вы е смогли открыть его')
                ifsafe==1:
                    print('Вы вводите пароль')
                    choise=int(input('Что взять?\n1.пистолет и патроны\n2.записку с текстом\n3.Артефакт'))
                    if choise==1:
                        if gun==0:
                            print('Вы взяли пистолет, и т.к. вы-главный герой, патроны бесконечные!')
                            damage=damage+15
                            gun=1
                        else:
                            print('Вы уже взяли пистолет!')
                    ifchoise==2:
                        print('Привет, сын, если ты это читаешь, значит я уже умер.\nт.к владел банком, я прощаю тебе все.\nесли ты взял кредит, он прощен.\nна твоем банковском счету 1900 шекелей')
                        bank=bank+1900
                        creditc=0
                        creditm=0
                        creditt=0
                    ifchoise==3:
                        print('Вы взяли Артефакт')
                        artefact=1
                        historylist.append('артефакт')
                historylist.append('сейф')
            ifchoise==2:
                print('Вы открыли ящик, что взять из него?')
                choise=int(input('1.подсказка для сейфа\n2.карта доступа 2ур.\n3.банк.карта\n4.подставка для Артефакта\n>>>'))
                if choise==1:
                    print('шкаф, qmodgcbr')
                ifchoise==2:
                    print('Вы взяли карту доступа!')
                    dos_card=1
                ifchoise==3:
                    print('Вы взяли банковскую карту своего отца...')
                    bank=bank+1200
                ifchoise==4:
                    print('Вы взяли подставку для Артефакта')
                    artefactp=1
            ifchoise==3:
                print('В шкафу есть дверь щитка, что бы открыть его нужно ввести пароль!')
                choise=str(input('Попробовать ввести его?\n>>>'))
                if choise=='да':
                    password=int(input('введите пароль: '))
                    if password==82467139:
                        print('Вы открыли его!')
                        choise=int(input('Вы можете:\n1.открыть сейф\n2.Выключить электричество в №";"!;№"!\n3.включить защиту дома\n>>>'))
                        if choise==1:
                            print('Сейф открыт')
                            safe=1
                        ifchoise==2:
                            print('Электричество отключено!')
                            elecrik=0
                        ifchoise==3:
                            print('Защита активирована!')
                            safe_house=1
                    ifpassword!=82467139:
                        print('Ошибка доступа')
                ifchoise=='нет':
                    print('...')
            ifchoise==4:
                break
    ifchoise==2:
        print('Вы вошли в гостинную!')
        choise=int(input('Вы видете:\n1.Мужчиину в пиджаке\n2.Ящик\n3.диван\n>>>'))
        if choise==1:
            print('Ты уже читал записку отца?')
            choise=str(input('>>>'))
            if choise=='да':
                print('Соболезную')
            ifchoise=='нет':
                print('Она в сейфе, а сейф в комнате.')
        ifchoise==2:
            print('Вы открыли ящик, в нем находится:\n1.таинственная красная кнопкаn\n2.щиток\n3.&$!^*^&$@(^%#@%!$^$^!(&$($!!^$!#(%&*')
            choise=int(input('>>>'))
            if choise==1:
                print('На неё лучше не нажимать!')
            ifchoise==2:
                print('Вы увидели 4 рубильника.')
                choise=int(input('1.спальня\n2.гостинная\n3.кухня\n4.подвал'))
            ifchoise==3:
                print('need decode: &$!^*^&$@(^%#@%!$^$^!(&$($!!^$!#(%&*')
        ifchoise==3:
            print('Вы решили отдохнуть')
            t.sleep(10)
    ifchoise==3:
        print('Вы зашли на кухню')
        choise=int(input('Вы видите:\n1.тортик(тортик твою мать!)\n2.адамантиевый стул\n3.очеть крепкая дверь'))
        if choise==1:
            print('съесть его?')
            choise=str(input('>>>'))
            if choise=='да':
                print('Вы съели тортик!')
                hp=hp+r.randint(5, 16)
            ifchoise=='нет':
                print('Вы не съели торт')
        ifchoise==2:
            print('Вы сели на него, на удивление он был удобный.')
            hp=hp*r.randint(5, 10)
        ifchoise==3:
            print('Вы подошли с двери')
            if elecrik==0:
                print('На удивление она открылась')
                print('За ней был погреб(очень темный, надеюсь у вас есть фонарик)')
                choise=str(input('Войти в него?\n>>>'))
                if choise=='да':
                    print('Сработала магия гг и у вас оказался фонарик, вы спускайтесь вниз.')
                    t.sleep(2)
                    print('НЕОЖИДАННО ПЕРЕД ВАМИ ПОЯВИЛСЯ МОНСТР!')
                    battle(hp, damage, 100, 15)
                    if win==1:
                        print('Вы одолели его, и забрали все что у него было (жену и детей в том числе)')
                    ifwin==0:
                        print('Хоть вы и проиграли, но монстр простил вас и выпустил из погреба')
                        hp=hp-5
                if choise=='нет':
                    print('Вы решили не идти туда.')
            ifelecrik==1:
                print('Вы не смогли открыть дверь.')
    ifchoise==4:
        print('Вы решили зайти в подвал и увидели 5 злых детей!')
        battlebig(hp, damage, 15, 10)
        battlebig(hp, damage, 20, 5)
        battlebig(hp, damage, 10, 12)
        battlebig(hp, damage, 50, 2)
        battlebig(hp, damage, 5, 5)
    ifchoise==5:
        break


fin=str(input('введите что нибудь, для завершения игры.\n'))
final=open('final.txt', 'a')
final.write(name and historylist)