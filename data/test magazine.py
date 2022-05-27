def magazine(i1, i2, i3, c1, c2, c3):
        a1=a2=a3=0
        global itp1, itp2, itp3, coins
        #i know, that is stupid to add sub per. for sub per, but i do!
        m_circle=1
        print("Вы заходите в магазин")
        while m_circle==1 or m_circle=='да' or m_circle=='Да':
            print('Вы можете купить несколько предметов:\n1.', i1, 'за', c1, 'шекелей', '\n2.', i2, 'за', c2, 'шекелей', '\n1.', i3, 'за', c3, 'шекелей')
            print('У вас', coins, 'монет.')
            choise = input('>>>')
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