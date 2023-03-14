#yosh = int(input("yoshingiz nechida?"))
#if yosh <= 4:
#    narx = 0
#elif yosh <= 12 :
#    narx = 5000
#else:
#    narx = 10000
#
#print(f"sizga kirish {narx}so'm")

                              #14-dars
                          #LUG'AT(DICTIONARY)

#soz_turkum = {'apple':'olma', 'banana':'banan'}
#print(soz_turkum['apple'])
#print(soz_turkum['banana'])

#bozorolik = {'qovun':10000, 'uzum':6000, 'tarvuz':2500}
#print(bozorolik['qovun'])
#print(bozorolik['tarvuz'])
#print(bozorolik['uzum'])
#print(f"qovun narxi {bozorolik['qovun']} so'm")

#talaba = {'ism':'begzod xoshimov', 't_yil':2001, 'yosh':22}
#print(f"{talaba['ism'].title()}, {talaba['t_yil']} yilda tug'ilgan. U hozzir {talaba['yosh']} da")
#talaba['kurs'] = 3
#talaba['fakulteti'] = 'dasturiy injiniring'
#talaba['ism'] = 'asdbek'
#print(talaba)

#talaba = {}
#talaba['ism'] = 'begzod'
#talaba['yoshi'] = 22
#talaba['kursi'] = 3
#talaba['yonalishi'] = 'dasturiy injiniring'
#print(f"Talaba {talaba['ism'].title()}, yoshi {talaba['yoshi']} da. U {talaba['yonalishi']} yo'nalishi {talaba['kursi']} bosqich talabasi.")
#print(talaba)
#del talaba['yoshi']   #o'chirish
#print(talaba)

#telefonlar = {
#    'ali':'ipxone x',
#    'vali':'samsung',
#    'halil':'nokia',
#    'hasan':'sony',
#    'husan':'lg'
#}
#print(telefonlar)
              #boshqa o'zgaruvchiga qo'shish
#telefon = telefonlar.get("kamol", "bunday telefon mavjud emas!")
#print(telefon)

                      #15-DARS
                #LUG'AT BILAN ISHLASH
    # METOD items()
#telefonlar = {
#    'ali':'ipxone x',
#    'vali':'samsung',
#    'halil':'nokia',
#    'hasan':'sony',
#    'husan':'lg',
#    'sherbek':'sony',
#    'alisher':'samsung',
#    'begzod':'ipxone x',
#    'nodirbek':'redmi'
#} 
#print(telefonlar.items())
                #kalit va qiymatini alohida chiqarish
#for kalit,qiymat in telefonlar.items():
#    print(f"Kalit: {kalit}")
#    print(f"Qiymat: {qiymat}")

#for k, q in telefonlar.items():
#    print(f"{k.title()}ning telefoni {q}" )

         # METOD  keys() 
#mahsulotlar = {
#    'olma' : 10000,
#    'uzum' : 6000,
#    'nok' : 15000,
#    'banan' : 23000,
#    'mandarin':16000,
#    'kiwi':10000,
#    'shaftoli':8000,
#    'kakos':100000
#}
#print(mahsulotlar.keys())
#print("do'kondagi mahsulotlar")
#for maxsulot in mahsulotlar.keys():   #keys qo'ysa ham qo'ymasa ham bo'ladi.
#    print(maxsulot.title())

#bozorolik = ['olma', 'uzum', 'apelsin', 'ananas']
#for mahsulot in mahsulotlar:
#    if mahsulot in bozorolik:
#        print(f"{mahsulot.title()}, {mahsulotlar[mahsulot]} so'm")
#
#for buyum in bozorolik:
#    if buyum not in mahsulotlar:
#        print(f"Iltimos do'koningizga {buyum} ham olib keling!+")

                    # SORTED tartiblab beradi alifbo bo'yicha
#print("Do'kondagi mahsulotlar")
#for mahsot in sorted(mahsulotlar):
#    print(mahsot.title())

                #VALUES METODI faqat qiymatni chiqaramiz
#print(mahsulotlar.values())

#print("foydalanuvchilarga quyidagi narxlarni tavsiya qilamiz!")
#for mahsulot in mahsulotlar.values():
#    print(mahsulot)
#print(mahsulotlar)

                #SET FUNKSIYASI ikta birhillilarni bita qilib chiqarib beradi
#print("foydalanuvchlar quyidagi telefonlarni ishlatishadi!")
#for tel in set(telefonlar.values()):
#    print(tel)

                #set yaratish - setda bir nechta birxil ma'lumotlarning faqat bittasi chiqadi
#toys = {'car', 'ball', 'lamp', 'ball', 'bear', 'car'}
#print(toys)