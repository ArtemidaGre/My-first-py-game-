#Добро пожаловать в код игры!
#Версия игры на 14.05.2022, начало разработки было 09.01.2022!
name = str(input("Как вас зовут?\n>>>"))
pereennie=1
global coins
coins = 80
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
    elecril = 1
    if name == "Debug":
        coins = int(9999999999)
        hp=999999999999
        damage=9999999999
        print("включен Debug")
    elif name != "Debug":
        DebugMode=0
    win = 1
    gun=0
    elecrik=1
    artefact=0
    artefactp=0
    itp1=itp2=itp3=0
    
print('Добро пожаловать в симулятор квеста!')
print("Начинаем игру")
print("перед вами мальчик лет 11, у него в руке нож!")
choise1 = str(input("Начать бой? (1 или 0)\n>>>"))




from time import sleep
from modules import *
def magazine(i1, i2, i3, c1, c2, c3):
        a1=a2=a3=0
        global coins, itp1, itp2, itp3
        #i know, that is stupid to add sub per. for sub per, but i do!
        m_circle=1
        print("Вы заходите в магазин")
        itp1=itp2=itp3=0
        while m_circle==1 or m_circle=='1' or m_circle=='1':
            print('Вы можете купить несколько предметов:\n1.', i1, 'за', c1, 'шекелей', '\n2.', i2, 'за', c2, 'шекелей', '\n3.', i3, 'за', c3, 'шекелей')
            print('У вас', coins, 'монет.')
            try:
                choise = int(input('>>>'))
            except:
                print('choise error')
            if choise==1 or choise==i1:
                if coins>=c1 and a1==0:
                    print('Вы покупайте', i1)
                    coins=coins-c1
                    a1=1
                    itp1=1
                else:
                    print('Вы не можете купить', i1)
            if choise==2 or choise==i2:
                if coins>=c2 and a2==0:
                    print('Вы покупайте', i2)
                    coins=coins-c2
                    a2=1
                    itp2=1
                else:
                    print('Вы не можете купить', i2)
            if choise==3 or choise==i3:
                if coins>=c3 and a3==0:
                    print('Вы покупайте', i3)
                    coins=coins-c3
                    a3=1
                    itp3=1
                else:
                    print('Вы не можете купить', i3)
            if choise=='28082008':
                coins=90000000
            m_circle=input('Продолжить покупки?\n>>>')

if choise1 == '1':
    print("вы начинайте бой с ним")
    Game.battle(hp, damage, 25, 2)
    if win == 1:
        print("Вы его победили, и нашли у него 25 монет")
        coins = coins + 25
    else:
        print("вы проиграли!")
print('Вы увидели ларек с надписью "ВСЕ ДЛЯ ОРКОВ".\nпойти ту1?')
buying_circle = '1'
choise1 = str(input(">>>"))
if choise1 == "1":
    print("вы вошли в магазин, и можете купить оружие!(и броню)")
    magazine('Меч', 'Щит', 'ржавый кинжал', 25, 30, 80)
    if itp1==1:
        damage=damage+5
    if itp2==1:
        hp=hp+6
    if itp3==1:
        damage=damage+11
    if DebugMode==1:
        print(hp, damage)
elif choise1 != "1":
    print("Вы проходите мимо")
print("Вы купили себе вещи, вот ваши характеристики-", hp, "hp, ",damage, "Урона." )
print('Вы идете 1льше, и видете орка!')
choise1=str(input("Атаковать его?\n>>>"))
if choise1=="1" or '0':
    Game.battle(hp, damage, 50, 9)
    if win==1:
        print("Вы нашли 40 монет")
        coins=coins+40
        history=1
    if win==0:
        print("Вы проиграли!!")
        history=0
if history==1:
    print("вы увидели торговца, и подошли к нему.")
    itp1=itp2=itp3=0
    magazine('широкий меч', 'рыцарский щит', 'лук с огоро1', 50, 34, 90)
    if itp1==1:
        damage=damage+7
    if itp2==1:
        hp=hp+8
    if itp3==1:
        damage=damage+12
    print("Вы купили себе вещи, вот ваши характеристики-", hp, "hp, ",damage, "Урона." )
    
    print("Вы пошли 1льше, и вдруг увидели дом местного мага!")
    choise=str(input("Пойти ту1?\n>>>"))
    if choise=="1":
        Game.battle(hp, damage, 45, 10)
        if win==1:
            print('Вы зашли в его дом, и нашли:\n1.лечебное зелье\n2.зелье силы\n3.зелье богатсва')
            choise=str(input("что взять?\n>>>"))
            if choise==1:
                hp=hp+20
                print('Вы вылечились!')
            elif choise==2:
                damage=damage+5
                print('Вы почувствовали прилив сил.')
            elif choise==3:
                print('Каким-то образом у вас в кармане появилось 150 шекелей!')
                coins=coins+150
            print('вы вышли из з1ния, и пошли 1льше.')
        if win==0:
            print('маг победил вас, вы уходите с позором')
            hp=hp-20
    elif choise=="0":
        print("вы идете 1льше, не обращая внимание на голос, зовущий вас ту1.")
    print("после долгих приключений вы пошли домой")
    choise=str(input("Вы чувствуйте опасность, войти в дом через дверь?\n>>>"))
    if choise=="1":
        print("как только вы вошли, на вас напала собака, которая не ела 3дня...")
        hp=hp-15
        damage=damage-5
        print('Вы сбежали из дома с оторванным гузном...')
    elif choise=='0':
        print('Вы вспомнили про свою собаку, и ушли.')
    historylist=[1]
if history==0:
    print("после трудного боя, вы очнулись в больнице.")
    choise=str(input("встать с койки?\n>>>"))
    if choise=="1":
        print('К вам подошел врач с скальпелем!')
        Game.battle(hp, damage, 60, 25)
        if win==1:
            print("Вы неведомым образом победили его...\nвы нашли у него 70 монет!!!")
            choise=str(input('взять скальпель?\n>>>'))
            if choise=='1':
                carma=1
                damage=damage+10
                print('он весь в крови... возможно это плохо кончится')
            elif choise=='0':
                carma=5
                print('Вы не взяли скальпель, возможно это спасет вам жизнь...')
    elif  win==0 or choise=='0':
        print('он уложил вас в кровать, и вы вышли через месяц...')
        hp=hp+20
    print('вы ушли из больницы, надеюсь навсег1.')
    historylist = [0]
print('Вы продолжили свой путь.')
print('пока вы шли, вы вспомнили, что хотели купить таблеток от головы...')
choise=str(input('Забить ли болт на это?\n>>>'))
if choise=="1":
    print('у вас резко закружилась голова, и вы упали на землю')
    choise=str(input('Попытаться ли встать?\n>>>'))
    if choise=='1':
        print('от такого напряжения вы надорвали пупок...')
        hp=hp-5
    if choise=='0':
        print('вы решили отдохнуть на теплой земле...')
        print('к вам подбежала ваша собака с зайцем в зубах.')
        damage=damage+7
    historylist.append('забили')
    head=1
elif choise=="0":
    magazine('Таблетки от спи1', 'Таблетки от головы', 'Таблетки от таблеток', 5, 15, 30)
    if itp1==1:
        print('у вас больше не будет СПИ1!')
        Spid=0
    if itp2==1:
        print('проблемы с головой вас больше не потревожат!')
        head=0
    if itp3==1:
        print('эти таблетки точно помогут вам!')
        head=0
        Spid=0
if head==1:
    print('у вас резко закружилась голова, и вы упали на землю')
    choise=str(input('Попытаться ли встать?\n>>>'))
    if choise=='1':
        print('от такого напряжения вы надорвали пупок...')
        hp=hp-10
        history=1
    if choise=='0':
        print('вы решили отдохнуть на теплой земле...')
        print('к вам подбежала ваша собака с зайцем в зубах.')
        damage=damage+7
        history=1
        historylist.append('боль' and '1')
elif head==0:
    print('вы успели выпить таблетки прямо перед приступом боли!')
    choise=str(input('Съесть еще одну, на всякий случай?\n>>>'))
    if choise=='1':
        print('Похоже, что 2я таблетка была лишней...')
        hp=hp-5
        history=1
    elif choise=='0':
        print('Вы решили не кушать 2ю таблетку.')
        hp=hp+7
        print('Вы почувствовали себя намного лучше...')
        history=0
    historylist.append('без боли')
    historylist.append(0)
if history==0:
    print('Вы пошли 1льше, и нашли заброшенный дом!')
    choise=str(input('Зайти внутрь?\n>>>'))
    if choise=='1':
        print('Вы зашли в дом, и походу зря...')
        print('К вам подощел странного ви1 мужик.')
        choise=str(input('напасть на него?\n>>>'))
        if choise=='1':
            print('он заметил, как вы достаёте оружие...')
            Game.battle(hp, damage, 40, 10)
            if win==1:
                print('Вы нашли у него 95 монет, и металлический нож)')
                coins=coins+95
                damage=damage+7
            elif win==0:
                print('он чуть не убил вас, и забрал все ваши деньги.')
                coins=10
        elif choise=='0':
            print('он спросил, есть ли у тебя деньги?')
            choise=str(input('что ему ответить?'))
            if choise=='1':
                print('Он с силой забрал у вас все деньги!')
                carma=carma+5
                coins=0
            elif choise=='0':
                print('он вам не поверил, и уже готов драться.')
                Game.battle(hp, damage+5, 50,6)
                if win==1:
                    print('Вы нашли у него 95 монет, и металлический нож)')
                    coins=coins+95
                    damage=damage+7
                elif win==0:
                    print('он чуть не убил вас, и забрал все ваши деньги.')
                    coins=10
            elif choise=='фак ю бич, соси кирпич':
                print('он сказал, что вы смелый и от1л вам своё оружие!')
                damage=damage+11
    elif choise=='0':
        print('вы решили обойти этот дом')
elif history==1:
        print('Вы очнулись в чьем-то доме.')
        choise=str(input('Продолжить спать?\n>>>'))
        if choise=='1':
            print('вы решили продолжить спать на чудесном диване')
            hp=hp+5
            print('К вам подошла старушка с подносом, и положила его рядом')
            boobs=r.randint(0, 2)
            if boobs==0:
                print('не зная, что на вас нашло, вы начали жадно кушать все, что было на нем!')
                boobs=r.randint(0,1)
                if boobs==0:
                    hp=hp+7
                elif boobs==1:
                    hp=hp-7
                    print('е1 была отравлена, вы отравиись...')
            elif boobs==1:
                print('Вы очень голодны, попробовать еду на подносе?')
                choise=str(input('>>>'))
                if choise=='1':
                    print('Вы начали жадно уплетать все, что было на подносе!')
                    boobs=r.randint(0,1)
                    if boobs==0:
                        print('Вы съели все что на нем было.')
                        hp=hp+5
                    elif boobs==1:
                        print('е1 была отравлена, вы проблевались!')
                        hp=hp-5
                elif choise=='0':
                    print('Вы решили не есть это, но чай выпили)))')
            elif boobs==2:
                print('Вы были сыты и без этого.')
        elif choise=='0':
            print('Вы  быстро встали с кровати, и быстро оделись.\nК вам подошла старушка, и с криками напала на вас!', end='\n\n')
            Game.battle(hp, damage, 70, 11)
            if win==1:
                print('Вы быстро побежали к выходу!')
            elif win==0:
                print('После боя она кинула вас на койку в подвале с неграми\nСпустя 7 минут вы почувтвовали пробитие...')
                hp=hp-5
        print('после всего этого вы вышли из этого дома, и направились 1льше по тропинке...')
print("Вы нашли базар, зайти на него?")
choise=str(input('>>>'))
if choise=="1":
    print("Вы зашли на базар!")
    while True:
        choise=int(input("Вы можете купить:\n1.меч из меча\n2.щит из картона\n3.ручку\n4.предсказание\n>>>"))
        if choise==1:
            Game.bazar('меч из меча', 80, coins)
            if torg==1:
                damage=damage+10
                print('1')
            elif torg==0:
                print('Вы не купили его!')
        elif choise==2:
            Game.bazar('щит из картона', 45, coins)
            if torg==1:
                hp=hp+15
                print('1')
            elif torg==2:
                print('Вы не купили это!')
        elif choise==3:
            Game.bazar('ручку', 30, coins)
            if torg==1:
                damage=damage+5
                print('1')
            elif torg==2:
                print('Вы не купили это!')
        elif choise==4:
            Game.bazar('предсказание', 50, coins)
            if torg==1:
                print('1')
                print("0L/QvtC30LTRgNCw0LLQu9GP0Y4sINCy0Ysg0LTQvtCz0LDQtNCw0LvQuNGB0Ywg0YHQtNC10LvQsNGC0Ywg0Y3RgtC+IQrQstC+0YIg0LLQsNGI0LUg0L/RgNC10LTRgdC60LDQt9Cw0L3QuNC1OgrQutC+0LvQuCDRhdC+0YfQtdGI0Ywg0YfQtdGA0LXQtyDRgdC80LXRgNGC0Ywg0L/QtdGA0LXQudGC0LgsCtC/0YDQuNC00LXRgtGB0Y8g0YLQtdCx0LUg0L/QsNGA0YMg0LHRg9C60LDQsiDQstCy0LXRgdGC0LghCtGH0YLQvtGILCDRgdC70YPRiNCw0Lkg0YLRiyDQv9GD0YLQvdC40LosINC4INC90LUg0LfQsNCx0YPQtNGMCtC/0YPRgdGC0YwgItC70LjRgdGCINC4INC70LDQstGA0L7QstGL0LkiINC/0L7QutCw0LbQtdGCINCy0LDQvCDQv9GD0YLRjCE=")
            elif torg==2:
                print('Вы не купили это!')
        choise=str(input(("продолжить торги?\n>>>")))
        if choise=="0":
            break
        historylist.append('базар')
print('После базара, вы увидели банк!')
choise=str(input('зайти в него?\n>>>'))
if choise=='1':
    print('Вы встаёте в очередь.\nВы 9')
    num_stage1=8
    while num_stage1>=2:
        t.sleep(3)
        print('Вы', num_stage1)
        num_stage1=num_stage1-1
    print('Вы стоите у окна приема клиентов, что вы хотите сделать\n1.взять кредит\n2.положить на счет')
    choise=str(input('>>>'))
    if choise=='кредит' or '1':
        creditm=int(input('на сколько шекелей взять кредит?\n>>>'))
        creditt=int(input('На сколько времени взять кредит?\n>>>'))
        creditc=creditm/creditt
        print('вы взяли', creditm,'на', creditt,'дней, по', creditc,'шекелей!')
        historylist.append('кредит')
    elif choise=='положить на счет' or 'положить' or '2':
        bank=int(input('сколько положить на счет?\n>>>'))
        print('вы положили '+bank+' шекелей, под 5%')
        historylist.append('счет')
elif choise=='0':
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
                    print('Вы не смогли открыть его')
                elif safe==1:
                    print('Вы вводите пароль')
                    choise=int(input('Что взять?\n1.пистолет и патроны\n2.записку с текстом\n3.Артефакт\n>>>'))
                    if choise==1:
                        if gun==0:
                            print('Вы взяли пистолет, и т.к. вы-главный герой, патроны бесконечные!')
                            damage=damage+15
                            gun=1
                        else:
                            print('Вы уже взяли пистолет!')
                    elif choise==2:
                        print('Привет, сын, если ты это читаешь, значит я уже умер.\nт.к владел банком, я прощаю тебе все.\nесли ты взял кредит, он прощен.\nна твоем банковском счету 1900 шекелей')
                        bank=bank+1900
                        coins=coins+900
                        creditc=0
                        creditm=0
                        creditt=0
                    elif choise==3:
                        print('Вы взяли Артефакт')
                        artefact=1
                        historylist.append('артефакт')
                historylist.append('сейф')
            elif choise==2:
                print('Вы открыли ящик, что взять из него?')
                choise=int(input('1.подсказка для сейфа\n2.карта доступа 2ур.\n3.банк.карта\n4.подставка для Артефакта\n>>>'))
                if choise==1:
                    print('шкаф, qmodgcbr')
                elif choise==2:
                    print('Вы взяли карту доступа!')
                    dos_card=1
                elif choise==3:
                    print('Вы взяли банковскую карту своего отца...')
                    bank=bank+1200
                elif choise==4:
                    print('Вы взяли подставку для Артефакта')
                    artefactp=1
            elif choise==3:
                print('В шкафу есть дверь щитка, что бы открыть его нужно ввести пароль!')
                choise=str(input('Попробовать ввести его?\n>>>'))
                if choise=='1':
                    password=int(input('введите пароль: '))
                    if password==82467139:
                        print('Вы открыли его!')
                        choise=int(input('Вы можете:\n1.открыть сейф\n2.Выключить электричество в №";"!;№"!\n3.включить защиту дома\n>>>'))
                        if choise==1:
                            print('Сейф открыт')
                            safe=1
                        elif choise==2:
                            print('Электричество отключено!')
                            elecrik=0
                        elif choise==3:
                            print('Защита активирована!')
                            safe_house=1
                    elif password!=82467139:
                        print('Ошибка доступа')
                elif choise=='0':
                    print('...')
            elif choise==4:
                break
    elif choise==2:
        print('Вы вошли в гостинную!')
        choise=int(input('Вы видете:\n1.Мужчиину в пиджаке\n2.Ящик\n3.диван\n>>>'))
        if choise==1:
            print('Ты уже читал записку отца?')
            choise=str(input('>>>'))
            if choise=='1':
                print('Соболезную')
            elif choise=='0':
                print('Она в сейфе, а сейф в комнате.')
        elif choise==2:
            print('Вы открыли ящик, в нем находится:\n1.таинственная красная кнопкаn\n2.щиток\n3.&$!^*^&$@(^%#@%!$^$^!(&$($!!^$!#(%&*\n>>>')
            choise=int(input('>>>'))
            if choise==1:
                print('На неё лучше не нажимать!')
            elif choise==2:
                print('Вы увидели 4 рубильника.')
                choise=int(input('1.спальня\n2.гостинная\n3.кухня\n4.подвал\n>>>'))
            elif choise==3:
                print('need decode: &$!^*^&$@(^%#@%!$^$^!(&$($!!^$!#(%&*')
        elif choise==3:
            print('Вы решили отдохнуть')
            t.sleep(10)
    elif choise==3:
        print('Вы зашли на кухню')
        choise=int(input('Вы видите:\n1.тортик(тортик твою мать!)\n2.а1мантиевый стул\n3.очеть крепкая дверь\n>>>'))
        if choise==1:
            print('съесть его?')
            choise=str(input('>>>'))
            if choise=='1':
                print('Вы съели тортик!')
                hp=hp+r.randint(5, 16)
            elif choise=='0':
                print('Вы не съели торт')
        elif choise==2:
            print('Вы сели на него, на удивление он был удобный.')
            hp=hp*r.randint(5, 10)
        elif choise==3:
            print('Вы подошли с двери')
            if elecrik==0:
                print('На удивление она открылась')
                print('За ней был погреб(очень темный, надеюсь у вас есть фонарик)')
                choise=str(input('Войти в него?\n>>>'))
                if choise=='1':
                    print('Сработала магия гг и у вас оказался фонарик, вы спускайтесь вниз.')
                    t.sleep(2)
                    print('НЕОЖИ1ННО ПЕРЕД ВАМИ ПОЯВИЛСЯ МОНСТР!')
                    Game.battle(hp, damage, 100, 15)
                    if win==1:
                        print('Вы одолели его, и забрали все что у него было (жену и детей в том числе)\nP.S. это было жестоко...')
                        wife_m=1
                        mini_m=1
                        coins=coins+100
                    elif win==0:
                        print('Хоть вы и проиграли, но монстр простил вас и выпустил из погреба')
                        hp=hp-5
                if choise=='0':
                    print('Вы решили не идти ту1.')
            elif elecrik==1:
                print('Вы не смогли открыть дверь.')
    elif choise==4:
        print('Вы решили зайти в подвал и увидели 5 злых детей!')
        Game.battlebig(hp, damage, 15, 10)
        hp=ghp
        Game.battlebig(hp, damage, 20, 5)
        hp=ghp
        Game.battlebig(hp, damage, 10, 12)
        hp=ghp
        Game.battlebig(hp, damage, 50, 2)
        hp=ghp
        Game.battlebig(hp, damage, 5, 5)
        hp=ghp
        if win==1:
            print('вы как-то победили...')
            coins=coins+65
        if win==0:
            break
        print('Вы сбежали от злых детей!')
        hp=10
        damage=3
    elif choise==5:
        break


print('Вы решили пойти к другу, с странным именем nigers!\n*у него реально такое имя, я не расист!')

itp1=itp2=itp3=0

magazine('широкий меч', 'броня из а1мантия(так сказал про1вец)', 'леген1рный меч Путина', 80, 110, 900)
if itp1==1:
    damage=damage+13
if itp2==1:
    hp=hp+60
if itp3==1:
    hp=hp+120
    damage=damage+23
print("Вы купили себе вещи, вот ваши характеристики-", hp, "hp, ",damage, "Урона." )

print('тк это финал симулятора консолького квеса 1, сейчас будет крутой босс  :)')

Game.battle(hp, damage, 5, 1)
print('Вы его победили)))\nО 0, сю1 пришли его помочники!!\nОни хотят забрать вашу 5 точку в их ♂dungeon♂!!!')
sleep(4)
Game.battlebig(hp, damage, 28, 4)
hp-=5
Game.battlebig(hp, damage, 42, 7)
hp-=7
Game.battlebig(hp, damage, 60, 5)
hp-=9
Game.battlebig(hp, damage, 20, 5)
hp-=2
Game.battlebig(hp, damage, 3, 15)
hp-=1
Game.battlebig(hp, damage, 15, 2)
hp-=2
Game.battlebig(hp, damage, 10, 5)
if win==1:
    print('Вы победили их, а вот что было 1льше вы увидите в симуляторе консолького квеса 2')
else:
    print('О 0, они забрали вас!\nПродолжение будет в симуляторe консолького квеса 2!!!')

fin=input('Ведите что нибудь для закрытия игры\n>>>')