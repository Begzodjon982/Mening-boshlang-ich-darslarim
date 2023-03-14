                #NESTING - lug'at icida royhat yoki royhat icida lug'at yoki lug'at ichida lug'atlarni
#Bir biriga bog'lanib tarmoqlanib ketishi
#car0 = {
#    'model':'lacetti',
#    'rangi':'oq',
#    'yil':2015,
#    'narxi':13000,
#    'km':50000,
#    'karobka':'avtomat'
#}
#
#car1 = {
#    'model':'nexia 3',
#    'rangi':'oq',
#    'yil':2019,
#    'narxi':9000,
#    'km':20000,
#    'karobka':'mexanika'
#}
#
#car2 = {
#    'model':'cobalt',
#    'rangi':'mokirasfalt',
#    'yil':2022,
#    'narxi':12000,
#    'km':7000,
#    'karobka':'mexanika'
#}
#car = car2
#print(f"{car['model'].title()} "
#      f"{car['rangi']} rangli "
#      f"{car['yil']}-yil ishlab chiqarilgan "
#      f"narxi {car['narxi']}$ "
#      f"{car['km']}km yurgan.")

# Oson usuli
#cars = [car0, car1, car2]
#for car in cars:
#    print(f"{car['model'].title()} "
#        f"{car['rangi']} rangli "
#        f"{car['yil']}-yil ishlab chiqarilgan "
#        f"narxi {car['narxi']}$ "
#        f"{car['km']}km yurgan.")

#print(cars)
                #inddeksi boyicha chaqirish
#print(cars[0]['model'])

#print(f"{cars[0]['rangi'].title()} "
#    f"{cars[0]['model']}")

#malibus = []
#for n in range(10):
#    new_car = {
#        'madel':'malibu',
#        'rangi':None,
#        'yil':2020,
#        'narxi':None,
#        'km':0,
#        'karobka':'avtomat'
#    }
#    malibus.append(new_car)
#print(malibus)
#for malibu in malibus[:3]:
#    malibu['rangi']='qizil'
#
#for malibu in malibus:
#    print(malibu)
#
#for malibu in malibus[3:6]:
#    malibu['rangi']='qora'
#
#
#for malibu in malibus[6:]:
#    malibu['rangi']='kok'
#    malibu['karobka']='mexanika'#
#
#for malibu in malibus:
#    if malibu['karobka']=='avtomat':
#        malibu['narxi']=40000
#    else:
#        malibu['narxi']=35000
#    print(malibu)


#dasturchilar = {
#    'ali' : ['python', 'c++'],
#    'vali' : ['html', 'css', 'js'],
#    'hasan' : ['php', 'sql'],
#    'husan' : ['python', 'php'],
#    'maryam' : ['c++', 'c#']
#}
#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi asturlash tillarini biladi:")
#    for til in tillar:
#       print(til.upper())

#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi asturlash tillarini biladi:")
#    for til in tillar:
#       print(f"{til.upper()}", end=(' '))
#
#hamkasblar = {
#    'ali':{'familya':'valiyev',
#            'tyil':1996,
#            'malumot':'oliy',
#
#            'tillar':['paython','c++']
#            },
#    'vali':{'familya':'aliyev',
#            'tyil':1990,
#            'malumot':'oliy',
#            'tillar':['js','java','c#']
#            },
#    'hasan':{'familya':'sobirov',
#             'tyil':1993,
#             'malumot':'o`rta',
#             'tillar':['MYSQL','php']
#            }
#}
#
#for ism, info in hamkasblar.items():
#    print(f"\n{ism.title()}{info['familya'].title()}"
#          f"{info['tyil']}-yilda tug'ilgan."
#          f"Ma'lumoti:{info['malumot']}.\n"
#          "quyidagi dasturlash tillarini biladi:")
#    for til in info['tillar']:
#                print(til.upper())


                        #17-DARS INPUT() VA WHILE 
#input()
#ism = input("salom ismingizni kiriting:")
#savol = f"Salom ,{ism.title()} yoshingiz nechida?"
#yosh = input(savol)
#yosh = int(yosh)
#boyi = input('boyingiz nechi metr?')
#boyi = float(boyi)
#print(f"Salom {ism.title()} sizni yoshingiz {yosh} da ekan, bo'yingiz esa {boyi} m sm da ekan.")
#
#while
#son = 1 
#while son <= 5:
#        print(son, end=" ")
#        son = son + 1
#        #son += 1            #ikkalasini vazifasi bir xil tepadagi son bilan
#print("dastur tugadi")
#
                #while and input
#
#print('kiritilgan sonni kvadratini chiqaruvchi dastur:')
#savol = "Istalgan son kiriting:"
#savol = "(dastur toxtashi uchun 'exit' deb yozing!)"
#qiymat = ''
#while qiymat != "exit":
#        qiymat = input(savol)
#        if qiymat != "exit":
#                print(float(qiymat)**2)
#print('dastur tugadi:')

                #ishora

#print('kiritilgan sonni kvadratini chiqaruvchi dastur:')
#savol = "Istalgan son kiriting:"
#savol = "(dastur toxtashi uchun 'exit' deb yozing!)"
#ishora = True
#while ishora:
#        qiymat = input(savol)
#        if qiymat == 'exit':
#                ishora = False
#        else:
#             print(float(qiymat)**2)
#print('dastur tugadi:')
#
                #break while
#
#print('kiritilgan sonni kvadratini chiqaruvchi dastur:')
#savol = "Istalgan son kiriting:"
#savol += "(dastur toxtashi uchun 'exit' deb yozing!)"
#while True:     #abadiy tsikl
#        qiymat = input(savol)
#        if qiymat == 'exit':
#                break       #tsiklni to'xtatish
#        else:
#                print(float(qiymat)**2)
#print("dastur tugadi:")                
#
                #for uchun break
#
#sonlar = list(range(1,11))
#for son in sonlar:
#        if son == 9:
#                break
#        else:
#                print(f"{son} ning kvadrati {son**2} ga teng!")
#
                #CONTINUE
#
#sonlar = list(range(1,11))
#for son in sonlar:
#        if son == 5:
#                continue
#        print(f"{son} ning kvadrati {son**2} ga teng!")
#
                #COUNTINUE WHILE
#
#son = 0
#while son < 10:
#        son += 1
#        if son%2 != 0:     #agar son ikkiga bo'linsa 2% != 0 da faqat ikkiga bo'linadigon sonltoq sonlar chiqadi, agar tengmi == desak toq sonlarni chiqarib beradi.
#                continue
#        else:
#                print(son) 
#
#abadiy tsikillar
#
#son = 0
#while son < 10 :           #buni tog'irlash uchun while dan so'ng son += 1 qilishimiz kerak.
#        if son%2 != 0:
#                continue
#        else:
#                print(son)
#
#     To'xtovsiz davom etadi
#son = 1
#while son>0:         #tsiklni to'g'irlash uchun son oldiga <10 qilish kerak.
#        son += 1
#        if son%2 != 0:
#                continue
#        else:
#                print(son)
#
                        #18-DARS WHILE VA ROYHATLAR       
#
#print("yaqin do'stlaringizni ismini kiriting:")
#ismlar = []
#n=1    #ismlarni sanash uchun o'zgaruvchi
#while True:
#        savol = f"{n}-do'stingiz ismini kiriting:"
#        ism = input(savol)
#        ismlar.append(ism)
#        takrorlash = input("yana ism qo'shasizmi? (ha/yo'q)")
#        n+=1
#        if takrorlash != "ha":
#                break
#
#print("do'stlaringiz ro'yhati:")
#for ism in ismlar:
#        print(ism.title())
#print(ismlar)
#
#
#print("do'stingizni ismi va yoshini kiriting:")
#dostlar = {}
#ishora = True
#while ishora:
#        ism = input("Do'stingiz ismini kiriting:")
#        yosh = input(f"{ism.title()}ning yoshi nechida?")
#        dostlar[ism] = int(yosh)
#
#        javob = input("yana ma'lumot qo'shasizmi? (ha/yo'q)")
#        if javob == "yo'q":
#                ishora = False
#
#for ism, yosh in dostlar.items():        
#       print(f"{ism.title()}{yosh}da")
#print(dostlar)

#shart bajarilishi davomida ro'yhat ichidagi barcha elementlar birin ketin o'chib ketadi
#cars = ['lasetti', 'nexia', 'cobalt', 'nexia', 'matiz', 'nexia']
#while 'nexia' in cars:         #whiledan oldin car deb o'zgaruvchi kiritish va unga ro'yhat ichidagi elementni berish kerak
#        cars.remove('nexia')
#print(cars)
#
#talabalar = ['hasan', 'husan', 'olim', 'botir']
#baholangan_talabalar = {}
#while talabalar:
#        talaba = talabalar.pop()
#        baho = input(f"{talaba.title()}ning bahosini qoying:")
#        print(f"{talaba.title()}  bahlandi.")
#        baholangan_talabalar[talaba] = int(baho)
#print(baholangan_talabalar)

            #19-DARS FUNCTIONS (FUNKSIYALAR)
#def salom_ber():
#    """Salom beruvchi dastur"""    #SHU JOYI DOCSTRING DEYILADI BOSHQA DASTURCHILAR UCHUN FUNKSIYAGA TUSHUNARLI MA'LUMOT BERISH
#    print("Assalomu aleykum")
#salom_ber()
#
#def salom_ber(ism):      #qavs ichiga dasturchi tomonidan ma'lumot joylansa parametr foydalanuvchi tomonidan esa argument deyiladi!
#    """Foydalanuvchi ismini qabul qilib,
#    unga salom beruvchi dastur"""
#    print(f"Assalomu aleykum, hurmatli {ism.title()}!")

#salom_ber('hasan')
#salom_ber('olim')
#print(print.__doc__)      #funksiyani koment qismini korish uchun

#def toliq_fio(ism,familya):
#    """foydalanuvchi ismini va familyasini 
#    jamlab chiqaruvchi funksiya"""
#    print(f"Foydalanuvchi ismi:{ism.title()}\n"
#          f"Foydalanuvchi familyasi:{familya.title()}")
#toliq_fio('begzod', 'xoshimov')

#ismlar = []
#for ism in ismlar:
#    ism = input("ism kiriting:")
#    ism.append(ismlar)
#    print(ism)

#def yosh_hissobla(ism, t_yil):
#    """foydalanuvchi tug'ilgan yilini chiqarib beruvchi funksiya"""
#    print(f"Salom {ism.title()}. Siz {2023-t_yil}da ekansiz!")
#yosh_hissobla('begzod', 2001)

                #20-DARS FUNKSIYADAN QIYMAT QAYTARISH

#def toliq_ism_yasa(ism,familya):
#    """ism va familya qaytaruvchi dastur"""
#    toliq_ism = f"{ism.title()} {familya.title()}"
#    print(toliq_ism)
#
#toliq_ism_yasa('begzod', 'xoshiov')    

#def toliq_ism_yasa(ism,familya):
#    """ism va familya qaytaruvchi dastur"""
#    toliq_ism = f"{ism.title()} {familya.title()}"
#    return toliq_ism     #LOCAL VARIABLE (MAHALLIY O'ZGARUVCHI)
#talaba = toliq_ism_yasa('begzod', 'xoshiov')  
#print(talaba)
#talaba1 = toliq_ism_yasa('olim', 'akromov')
#talaba2 = toliq_ism_yasa('ali', 'valiyev')
#print(f"Darsga kelmagan talabalar {talaba1.title()} va {talaba2.title()}")
#print(f"Talaba {talaba1.title()} darsga kechikib keldi!")

#def toliq_ism_yasa (ism, familya, otasining_ismi = ''):
#    """toliq ism familya qaytaruvchi funktsiya"""
#    if otasining_ismi:
#        toliq_ism = f"{ism} {otasining_ismi} {familya}"
#    else:
#        toliq_ism = f"{ism} {familya}"
#    return toliq_ism.title()
#
#talaba1 = toliq_ism_yasa('begzod', 'xoshimov')
#talaba2 = toliq_ism_yasa('alisher', 'yuldashev', 'xasanovich')
#print(f"Darsga kelmagan talabalar {talaba1} va {talaba2}")

#def avto_info(kompaniya, model, rangi, karobka, yili, narxi=None):
#    avto = {'kompaniya': kompaniya,
#            'model': model,
#            'rang': rangi,
#            'karobka': karobka,
#            'yil': yili,
#            'narx': narxi}
#    return avto
#avto1 = avto_info('GM', 'damas', 'oq', 'mexanika', 2019)
#avto2 = avto_info('GM', 'gentra', 'oq', 'avtomat', 2021, 13000)
#avtolar = [avto1 , avto2]
#print('online bozordagi avto mashinalar:')
#for avto in avtolar:
#    if avto['narx']:
#        narx = avto['narx']
#    else:
#        narx = "noma'lum"
#    print(f"{avto['rang']} {avto['model']}. Narxi: {narx}")

#def oraliq(min,max):
#    sonlar = []
#    while min<max:
#        sonlar.append(min)
#        min += 1
#    return sonlar
#print(oraliq(0, 10))
#print(oraliq(20, 31))

#def oraliq(min,max,qadam):
#    sonlar = []
#    while min<max:
#        sonlar.append(min)
#        min += 1
#    return sonlar
#print(oraliq(0, 11))

def raqamlar(min,max,qadam):
    sonlar = []
    if qadam:
        min += qadam == max
        sonlar.append(min)
    else:
        min<max
        sonlar.append(min)
        min+=1
        return sonlar
son = raqamlar(1, 12, 2)
print(son)
    
