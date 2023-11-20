#begin 1

# import math

# x = int(input("kiriting :"))
# x=1
# print(math.sqrt(x))

#begin 2

# import random as r # random modulini r deb chaqirayapmiz

# son = r.randint(0,100) # 0 va 100 oralig'ida tasodifiy son
# print(son)

# <<<
# set1 = {"apple",1,True,5.6,"apple"}
# set2 = {'a','b',1}

# S3 = set1.intersection(set2)

# print(S3)
# >>>

# #begin 3
# menu = [1,2,3,4,5,6,7,8,9,0]
# buyurtmalar = [1,2,3,4,5,6,7,8,9,0]

# for Son in buyurtmalar:
#     if Son in menu:
#         print(f"Butun {Son} bor")
#     else:
#         print(f"Kechirasiz, - son {Son} yo'q")

#begin 4

# a = 20
# b = 33

# if b > a:
#   print(a > 2)
# else:
#   print(b <= 3)

#begin 5

# a = 7
# b = 20

# if b > a:
#   print(a >= 0)
# else:
#   print(b < -2)

#begin 6

# a = 3
# b = 4
# c = 5

# if a <= b <= c:
#     print(a <= b)
# else:
#     print(a <= b <= c)

#begin 7

# a = 3
# b = 5
# c = 6

# if a >= b <= c:
#     print(a > b)
# else:
#     print(a > b < c)

#begin 8

# a = 3
# b = 5

# if a <= b :
#     print(a <= b)
# else:
#     print(a <= b)

#begin 9

# a = 2
# b = 5

# if a <= b :
#     print(a <= b)
# else:
#     print(a <= b)

#begin 10

# a = 3
# b = 6

# if a <= b :
#     print(a)
# else:
#     print(a <= b)

#begin 11

# a = 33
# b = 55

# if a <= b :
#     print(a)
# else:
#     print(b)

#begin 12

# a = 18
# b = 16
# c = 8

# print(bool(a))
# print(bool(b))
# print(bool(c))

#begin 13

# a = 18
# b = 15
# c = 8

# print(bool(a))
# print(bool([]))
# print(bool(c))

#begin 14

# a = -33
# b = 55
# c = -5

# if a <= b :
#     print(a,b)
# else:
#     print(c)

#begin 15

# a = 33
# b = 55
# c = -5

# if a <= b :
#     print(a,b)
# else:
#     print(c)

#begin 16

# a = 33
# b = 55

# if a <= b :
#     print(a)
# else:
#     print(b)

#begin 17

# a = 123

# if a == a :
#     print(a)

#begin 18

# num = 0

# while True:
#     num += 1
#     print(num)
    #cheksiz sanovchi sonlar
#
# num = 0
# ww = True
# while ww:
#     num = 1
#     if num == 10:
#         ww = False
#         print(num)

#

# n = 0 
# while n <= 98:
#     if n % 2 == 0:
#         n += 2
#         print(n)
#         faqat juft son chiqaradi

#

# a = input("uzb poyaxti nma :")
# b = "toshkent"
# if a == b:
#     print("togri")
# else:
#     print("notogri")

#

# ww = True
# text = 'uzbekiston poytaxti :'
# while ww:
#     a = input(text)
#     text = 'javob notori qayta kiriting :'
#     if a == 'toshkent' :
#         ww = False
#         print("javob togri")

# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
# print(ismlar)


# hello = []
# for i in range(1,10):
#     print("asalom alekum")

# def hello():
#     print("hello good")
    
# print(hello())

# def salom_ber():
#     print("hello")
    
# print(salom_ber())


# def salom_ber(ism, familya, yoshi):
#     print(f"assalom alekum {ism.title()} {familya.title()} {yoshi}")

# print(salom_ber(ism='ali', yoshi=19, familya='azizov'))
# # print(salom_ber("vali"))

# def kvadrat (x , y = 2):

#     print(x ** y)
    

# son = int(input('son kiriting :'))
# print(kvadrat(son))

#1yilini chiqarib beradi
# def yosh(ism, yosh):
#     year = 2023 - yosh
#     print(f"{ism}{year} siz shu yilda tug'ilgansiz")
# print(yosh('Sardor ',15))  


#2
# def yosh(ism, yosh):
#     print(f"{ism}{2023 - yosh} siz shu yilda tug'ilgansiz")
# print(yosh('Sardor ',15))  
# 
#  
# 3 none yo'q qilib beradi
# def yosh(ism, yosh):
#     return f"{ism}{2023 - yosh} siz shu yilda tug'ilgansiz"
# print(yosh('salohiddin ',15))   

# 
#4 soni kvadrati va kubi
# def kvad_kub(son):
#     kvadrati = son ** 2
#     kubi = son ** 3
#     print(f"{son} ning kvadrati {kvadrati} \n kubi {kubi}") 
# kvad_kub(9)    


# def katta(x, y, z):
#     if x > y and x > z:
#         print(f"{x} soni eng kata")
#     elif y > z:
#         print(f"{y} soni eng katta")
#     else:
#         print(f"{z} soni eng katta")
# katta(6, 8, 7)            


# def arifmetika(x, y, z, k):
#     summa = (x + y + z + k)/ 4
#     print(summa)
# arifmetika(2,2,2,2)


# def orta_geometrik(n):
#     multiplay = 1
#     for i in range(1, n+1):
#       son = int(input(f'{i}- sonni kiriting✌️ '))
#       multiplay *= son
#     print((multiplay) ** (1/n))
# orta_geometrik(4)


# nechta_son = int(input("butun son kiriting :"))
# def juftson(n):
#     list = []
#     index = 0
#     for i in range(1, n + 1):
#         son = int(input("{i}- son kiriting :"))
#     print(n)    


#soat yasash
# from turtledemo.clock import*
# while 1:
#     main()

#sonlar yig'indisi
# def yigindi(*sonlÅr):
#     y = 0
#     for i in sonlar:
#         y = y + i
#     return y


# print(yigindi(9,5,6,7,6))   


# def yigindi(x,*sonlar):
#     kvadrati = sonlar ** 3
    
#     return kvadrati , x


# print(yigindi(2,5,7,10))   

# sariq dev 1

# ism = 'james'
# familiya = 'bond'
# ism_sharif = f"{ism}  {familiya}"
# print(ism_sharif.upper())# harflarni kata harf bilan yozb berad
# print(ism_sharif.lower())# harflarni kichik harf bilan yozb berad
# print(ism_sharif.title())# 1chi harflarini katta qilib yozb berad
# print(ism_sharif.capitalize())# so'z boshdagi 1chi harflarni katta qilib yozb berad



# meva = "       olma       "
# print(meva)
# print("men" + meva.lstrip() + "yaxsh ko'raman")# bu chap tarafdi boshliqni olb tashlaydi
# print("men" + meva.rstrip() + "yaxsh ko'raman")# bu o'n tarafdi boshliqni olb tashladi
# print("men" + meva.strip() + "yaxsh ko'raman")# ikkala tarafdi boshliqni olb tashlaydi



# ism = input("ismingiz nima ? ")
# print("asalom alekum, " + ism) 



# ism = input("ismingiz nima ? \n>>>")
# print("asalom alekum, " + ism.title) 



# def katta(x, y, z):
#     if x > y and x > z:
#         print(f"{x} soni eng kata")
#     elif y > z:
#         print(f"{y} soni eng katta")
#     else:
#         print(f"{z} soni eng katta")
# katta(490,502,304) 



# radius = 20
# PI = 3.14
# diametr = 2*radius
# print("Aylananing uzunligi=", PI*diametr)


# ism = 'jobir'
# yosh = 23
# xabar = ism + ' ' + str(yosh) + ' yoshda'
# print(xabar)


# t_yil = int(input("tug'ilgan yilingizni kiriting: "))
# yosh = 2023 - t_yil
# print("siz", yosh, "yilda tug'ilgansiz")



# a = int("10") #butun son kiritish
# b = float("10") #butun son kiritish
# temp = str(36.6) #haqiqiy son kiritish


# mevalar = ['olma', 'anjr', 'shoftoli', 'nok']
# mevalar[0] = 'anor'#0 indexdi mevani o'zgartiradi
# mevalar.append("tarvuz")# bu yangi meva qo'shib beradi
# mevalar.append("o'rik")# bu yangi meva qo'shib beradi
# mevalar.insert(0, 'banan')#birinchi o'ringa banan qoshildi index 0 bo'lganligi uchun
# print(mevalar)


# cars = []
# cars.append("Laseti")#carsga list ichga element qo'shish
# cars.append("malibu")#carsga list ichga element qo'shish
# cars.append("jentra")#carsga list ichga element qo'shish

# del cars[1]#del index bo'yicha elementlarni o'chiradi
# cars.insert(0, 'Nexi 3')#insert index bo'yicha element qo'shadi
# cars.remove("jentra")#bu listni ichdi elementni nomi blan ochiradi
# print(cars)

# narhlar = [2000, 2933, 2343, 5000,]
# sonlar = ['bir', 'ikki', 3,4,5]
# print(narhlar[0] + narhlar[1])


# bozorlik = ['un','yog','piyoz','gosht','banan']
# maxsulot = bozorlik.pop(3)
# print("men" + maxsulot + "sotib oldim")
# print("olinmagan maxsulotlar", bozorlik)


# narhlar = [12000, 30400, 30300, 10000, 5000, 20000]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("eng arzon narh ",arzon, ". Eng qimmat ",qimmat)



# cars = ["Malibu", "TRaker", "kiya", "BMW"]
# cars.append("jentra")#listga malumot qo'shib beradi
# print(cars)



# toys = ('bus', 'teddy', 'car', 'bear', 'dino', 'snake')
# print(toys)#o'zgarmas ro'yxat


# mexmonlar = ['ali', 'Vali', 'hasan', 'husan', 'abror']
# print("salom", mexmonlar[0])
# print("salom", mexmonlar[1])




# mexmonlar = ['ali', 'Vali', 'hasan', 'husan', 'abror']
# for mehmon in mexmonlar:
#     print("salom", mehmon)
#     print("Xayr", mehmon)




# son = 1 # son ga 1 qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan...
#     print(son, end=' ') # son ni konsolga chiqaramiz,
#     son = son+1 # songa 1 qo'shamiz.



# sonlar = list(range(0,10)) # 0dan 9gacha chiqarib beradi beradi
# print(sonlar)



# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)




# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
# print(my_cars) 



# dostlar = []#bosh royxat
# print("5ta eng yaqin do'stingiz kim?")
# for n in range(5):
#     dostlar.append(input(f"{n+1} dostlaringizni ismini kiriting "))
# print(dostlar)    




# avtolar = ['audi', 'bmw','matiz', 'jenta','lobargini', 'tiko']
# for avto in avtolar:
#     if avto == 'mbw':
#         print(avto.upper())
#     else:
#         print(avto.title())    




# ism = input("ismingiz nima\n>>>")
# if ism.lower() != 'ali':
#     print(f"Uzr",{ism.title()}, "biz alini kutyapmiz.")
# else:
#     print("Salom Ali")



# javob = float(input("12x6 nechiga teng?>>>"))
# if javob!=72:
#     print("Javob xato!")



# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>=18:
#     print('Xush kelibsiz')
# else:
#     print("Kirish munkun emas!")



# login = input("Yangi login tanlang:")
# if len(login)<=5:
#     print("Login 5ta harfdan ko'proq bo'lishi shart")



# yil = int(input("tug'ilgan yilingiz kiriting :"))
# if 2023-yil<18:
#     print(f"Yoshingiz {2020-yil}da ekan.")
#     print("kirish munkin emas!")
# else:
#     print("Xush kelibsiz!")    



# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh>65: print("siz Covid-19 risk guruhda ekansiz")



# x,y = 25, 50 #x=25 va y=50
# print("x>y") if x>y else print("x<y")



# son = 50
# if son<0:
#     print("Manfiy son")
# else:
#     print("Musbat son")    



# yosh = int(input('yoshingiz nechida?  '))
# if yosh <=4:
#     print("Sizga kirish bepul.")
# elif yosh <=12:
#     print("sizga kirish 5000 sum")    
# elif yosh <=18:
#     print("sizga kirish 8000 sum")    
# else:
#     print("Sizga kirish 10000 sum")    



# yosh = int(input("Yoshingizni nechida?  "))
# if yosh<=4:
#     narh = 0
# elif yosh<=12:
#     narh = 5000
# elif yosh<=18:
#     narh = 8000
# else:
#     narh = 10000
# print(f"Sizga kirish {narh} sum")    



# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print("Bugun ish kuni.")



# kun = input("bugun nima kun?")
# harorat = float(input("Havo harorati qanday? "))

# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Chomilgan ketik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz!")    



# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# else:
#     price = 10000
    
# print(f"Sizga kirish {price} so'm")



# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4: # yosh bolalarga bepul
#     price = 0
# elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
#     price = 5000
# elif yosh<65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
#     price = 10000
# else: # qariyalarga esa 8000 so'm
#     price = 8000
# print(f"Sizga kirish {price} so'm")



# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')



# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#     print("Uyda dam olamiz!")



# narh = 15000 # mijoz 15000 so'mga taom oldi.
# choy = True # mijoz choy ham oldi
# salat = False # mijoz salat olmadi

# if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
#     narh = narh + 10000 # narhga 10000 so'm qo'shamiz
# elif choy or salat: # agar choy yoki salat olgan bo'lsa
#     narh = narh + 5000 # narhga 5000 so'm qo'shamiz

# print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz



# narh = 15000 # mijoz 15 so'mga ovqat oldi
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# #Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
# if choy:   # agar choy olsa
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:  # agar salat olsa
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:    # agar non olsa
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot: # agar kompot olsa
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti: # agar assorti olsa
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000
    
# print(f"Jami {narh} so'm")



# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# 'manti' in menu # menu da manti bormi?



# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#     print('Afsuski bizda bunday ovqat yo\'q')



# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() not in menu:
#     print('Afsuski bizda bunday ovqat yo\'q')
# else:
#     print('Buyurtma qabul qilindi.')


# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")



# print("O'ngacha sanaymiz")
# for n in range(10):
#     print(n+1)



# son = 50
# if son>=0:
#     print("Musbat son")
# else:
#     print("Manfiy son")



# son = input("Istalgan son kiriting: ")
# print(f"{son} ning kvadrati {son**2} ga teng")




# mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mevalar:
#     print(meva)



# son = int(input("Istalgan son kiriting: "))
# if son>=0:
#     print("Musbat son")
# else:
#     print("Manfiy son")



# mevalar = ['olma','anor','uzum']
# print(mevalar[2])



# radius = 5
# pi = 4.14
# aylana_yuzi = pi*radius**2
# print(aylana_yuzi)





# son = float(input("Istalgan son kiriting: "))
# ildiz = son**1/2
# print(f"{son} ning ildizi {ildiz} ga teng")



# mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mevalar:
#     print(meva)
#     print("Dastur tugadi")



# car_0 = {'model':'ferrari','rang':'qizil'}
# print(car_0['model'])



# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#  {talaba_0['t_yil']}-yilda tu'gilgan,\
#  {talaba_0['yosh']} yoshda")




# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(talaba_0)
# del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
# print(talaba_0)




# phone = telefonlar['ali']
# print(f"Alining telefoni {phone}")


# phone = telefonlar.get('hasan')
# print(phone)



# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }

# print(talaba_0.items())



# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")



# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")



# mahsulotlar = { # Do'kondagi mahsulotlar
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

# print(mahsulotlar.keys())



# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())



# telefonlar = input('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)




# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'    
#     }

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)



# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }

# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2015,
#         'narh':9000,
#         'km':89000,
#         'korobka':'mexanika'
#         }

# car2 = {
#         'model':'gentra',
#         'rang':'qizil',
#         'yil':2019,
#         'narh':15000,
#         'km':20000,
#         'korobka':'mexanika'
#         }



# malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
# for n in range(10):
#     new_car = { # har bir yangi mashina uchun lug'at yaratamiz
#         'model':'malibu',
#         'rang':None, # rangi noaniq
#         'yil':2020,
#         'narh':None, # narhi belgilanmagan
#         'km':0,
#         'korobka':'avto'
#         }
#     malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz



# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
#     for til in tillar:
#         print(f'{til.upper()} ', end='')




# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#            },
#     'vali':{'familiya':'aliyev',
#             'tyil':2001,
#             'malumot':"o'rta-maxsus",
#             'tillar':['html', 'css', 'js']},
#     'hasan':{'familiya':'husanov',
#              'tyil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']}
#     }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyil']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())



# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)



# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh) # yosh ni butun songa o'tkazamiz
# height = input("Bo'yingiz necha metr? ")
# height = float(height) # bo'yni o'nlik songa o'tkazamiz



# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())



# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")











