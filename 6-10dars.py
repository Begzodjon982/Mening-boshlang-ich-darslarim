# SONLAR    #6-dars

#a = 20     #int - butun son
#b = 5.5    #float - o'nlik son
#print(type(a))

#aholi_soni = 36_234_123
#print("o'zbekiston aholi soni =", aholi_soni, " ga teng")

#a = 20
#b = 5.5
#c = a * b
#x, y, z = 10, 1.1, -12
#print(c)
#d = 100/2
#print(d)
#d = 100//2
#print(d)

# KATTA HARFLAR BILAN YOZILGAN O'ZGARUVCHILAR O'ZGARMAS YANI KONSTANTA.

#radius = 20
#PI = 3.14159  #PI constanta o'zgarmas
#diametr = 2*radius
#print("aylana uzunligi =", PI * diametr)

#ism = "jobir"
#yosh = 30
#xabar = ism + " " + str(yosh) + " yoshda"
#print(xabar)

#t_yil = int(input("tug'ilgam yilingizni kiriting:"))
#yosh = 2023 - t_yil
#print("siz ", yosh , "yoshda ekansiz")

#kvadrat = 45
#PI = 3.14
#yuza = kvadrat**2
#yuza1 = kvadrat**3
#print(yuza1)

#yosh = int(input("yoshingiz nechida:"))
#yosh1 = 2023 - yosh
#print("siz ", yosh1 ,"yilda tug'ilgansiz!")

#a = int(input("1-son kiriting:"))
#b = int(input("2-son kiriting:"))
#print(a + b)
#print(a - b)
#print(a * b)
#print(a / b)

#LIST - ([]) ro'yhat  # 7-dars
#mevalar = ["olma", "anjir", "shaftoli", "o'rik"]  # matnli ro'yhat
#narxalar = [100, 2000, 30000, 3.23332, -22332]   #sonli ro'yhat
#sonlar = ["bir", "ikki", "uch", 4, 5, 6]    #aralash ro'yhat 
#ismlar = []   # bo'sh ro'yhat 
#print(mevalar)
# indekslar bo'yicha chaqirish mumkin indeksi 0 dan boshlanadi  -1 dan oxirdan birinchi element chiqaradi.
#mevalar[0] = "anor"
#mevalar[-1] = "uzum"
#print(mevalar)
#print(mevalar[0].title())
#print(mevalar[0].upper())
#print(mevalar[0].lower())
#print(mevalar[0].capitalize())
#mevalar.append("tarvuz"),("o'rik")
#print(mevalar)
#mevalar.insert(2, "ananas")
#print(mevalar)

#cars = ["bmw", "tayota", "audi", "gm", "ferari"]
#cars.append("malibu")
#cars.append("lacetti")
#print(cars)
#del cars[0]   #indeksi bo'yicha o'chirish 
#print(cars)
#cars.remove("bmw")   #remove indeks bo'yicha mas nomi bo'yicha o'chiraveradi lekin ro'yhatdan birinchi kelganini.
#print(cars)
#car = cars.pop(2)   #pop - bu ro'yhat ichidagi elementni indeksi bo'yicha chiqarib beradi agar indeks berilmasa royhat oxiridagi elementni chiqaradi yani oxirgi qo'shilgan elementni
#print(car)

# 8 - DARS 

#cars = ["bmw", "mersades", "kia", "audi", "lada", "Damas", "cobalt", "shevrolet"]
#print(cars)
#cars.sort()   # SORT ro'yhatlani alifbo tartibida va birinhi kotta harflardan boshlab tartiblab beradi
#print(cars)                        #raqamlarni ham
#cars.sort(reverse=True)
#print(cars)
#print(sorted(cars))   # SORTED bu faqat consolga tartiblagan holda chiqarib beradi asl ro'yhat o'garmaydi
#print(sorted(cars, reverse=True))             #raqamlarni ham
#cars.reverse()   #ro'yhatni teskarisiga tartiblab beradi
#print(cars)
#print(len(cars))   #LEN  ro'yhat uzunligini aniqlab beradi

#sonlar = [12, 44, 24, 98, 74, -43, -22, 9.4, 29, 30, 7.6]
#print(sorted(sonlar))

#sonlar = list(range(0, 10))
#print(sonlar)
#toq_sonlar = list(range(1,20,2))
#print(toq_sonlar)
#juft_sonlar = list(range(0,20,2))
#print(juft_sonlar)
#print(max(toq_sonlar))

#narxlar = [12000, 20000, 14000, 43000, 25000, 40000]
#print(narxlar)
#arzon = min(narxlar)
#qimmat = max(narxlar)
#jami = sum(narxlar)
#print("eng arzoni", arzon , "eng qimmati", qimmat, "jami", jami,  )

#cars = ["bmw", "mersades", "kia", "audi", "lada", "Damas", "cobalt", "shevrolet"]
#print(cars[0:3])
#my_cars = cars[ : ]   #ro'yhatni nushalash
#print(cars)
#my_cars.remove('bmw')
#print(my_cars)

# TUPLE o'zgarmas ro'yhat 

#toys = ('bear', 'bus', 'car', 'dino', 'snake', 'lizard')
#print(type(toys))
#toys = list(toys)
#toys.append('teddy')
#print(toys)
#toys = tuple(toys)
#print(toys)
#sonlar = list(range(120, 1202, 2))
#print(sonlar)
#print(sum(sonlar))
#a = max(sonlar)
#b = min(sonlar)
#print(a - b)
#print(len(sonlar))
#sonlar = list(range(120, 1202, 2))
#son = sonlar[0:20]
#son1 = sonlar[510:530]
#son2 = sonlar[-1180:-1]
#print(son)
#print(son1)
#print(son2)

#taomlar = ['osh', 'tuxum', 'shashlik', 'qozonkabob', 'bistrogen']
#nonushta = taomlar[:]
#print(taomlar)
#print(nonushta)
#nonushta.remove('osh')
#nonushta.remove('shashlik')
#nonushta.remove('qozonkabob')
#print(nonushta)
#nonushta.append('sariyog')
#nonushta.append('kolbasa')
#print(nonushta)
#print(taomlar)
#nonushta = tuple(nonushta)
#print(nonushta)

#9-DARS   FOR SIKILLI

#mehmonlar = ['ali', 'vali', 'hasan', 'husan', 'olim']
#for mehmon in mehmonlar:
#    print("salom", mehmon)    
#for mehmon in mehmonlar:
#    print(f"hurmatli {mehmon} sizni dushanba kuni nohorgi oshga taklif qilamiz!")
#    print("hurmat bilan palonchiyevlar oilasi\n")

#sonlar = list(range(11))
#for son in sonlar:
#    print(f"{son} ning kvadrati {son**2} ga teng!")

#sonlar_kvadrati = []
#for son in sonlar:
#    sonlar_kvadrati.append(son**2)
#print(sonlar)
#print(sonlar_kvadrati)

#dostlar = []
#print("5 ta eng yaqin dostingizni kiriting!")
#for n in range(5):
#    dostlar.append(input((f"{n+1} dostingizni ismini kiriting:")))
#print(dostlar)

#ismlar = ['anvar', 'begzod', 'alisher', 'valisher', 'nodirbek']
#for ism in ismlar:
#    print("salom ", ism, "dostim")
#print(f"kod 5 marta takrorlandi: ")

#sonlar = list(range(10, 100, 3))
#print(sonlar)
#for son in sonlar:
#    print(f"{son**3}")

#kino = []
#for n in range(5):
#    kino.append(input((f"{n+1} sevimli kino nomini kiriting:")))
#print(kino)

#odamlar = []
#for n in range(10):
#    odamlar.append(input((f"bugun kimlar bilan suhbatlashdingiz:")))
#print(odamlar)

# 10 - DARS   TARMOQLANISH "IF", "ELSE"

#avtolar = ['bmw', 'cobalt', 'damas', 'audi', 'lacetti']
#for avto in avtolar:
#    if avto == "bmw":
#        print(avto.upper())
#    else:
#        print(avto.title())

#ism = input("ism kiriting:")
#if ism.lower() != 'ali':
#    print(f"uzur {ism.title()} biz alini kutyapmiz:")
#else:
#    print("salom ali")
    
#javob = float(input("12x6 nechiga teng:"))
#if javob != 72:
#    print("javob hato")
#else:
#    print("javob to'g'ri")

#yosh = int(input("yoshingizni kiriting:"))
#if yosh >= 18 :
#    print("sizga kirish mumkin marhamat")
#else:
#    print("kirish mumkin emas:")

#login = input("login kiriting:")
#if len(login) <= 8 :
#    print("login 8 harfdan yoki ishoradan iborat bo'lishi kerak:")
#else:
#    print("login qabul qilindi!")
#print(login)

#yosh = int(input("tug'ilgan yilingizni kiriting:"))
#if 2023-yosh < 18:
#    print(f"yoshingiz {2023-yosh} da ekan")
#    print("kirish mmkin emas")
#else:
#    print("xush kelibsiz!")

#yosh = int(input("yoshingiz nechida:"))
#if yosh>65: print("siz covid-19 ning risk guruhida ekansiz!")
#else:
#    print("siz hech qaysi guruhga kirmaysiz")

#x,y = 25, 50
#print("x>y") if x>y else print("x<y")

#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
#    if car != "gm":
#        print(car.title())
#    else:
#        print(car.upper())

#login = input("ismingizni kiriting:")
#if login.lower() == "admin":
#    print("hush kelibsiz admin foydalanuvchilar ro'yhatini ko'rasizmi!")
#else:
#    print(f"hush kelibsiz {login}")

#x = int(input("son kiriting:"))
#y = int(input("son kiriting:"))
#if x==y :
#    print("sonlar teng:")
#else:
#    print("teng emas:")

#son = int(input("son kiriting:"))
#if son < 0 :
#    print("manfiy son")
#else:
#    print("musbat son")





















