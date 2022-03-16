
#problems1
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
    if "Rust" in i:
        print('this languages is in list')

#problems2
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
l = []
for i in range(6):
    if i < 2:
        l.append(languages[i])
print(l)

#problems3
a = 7
for i in range(5):
    a = a*a
    print(a)

#problems4
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in range(6):
    print(i,languages[i])

#problems5
a = 0
for i in range(1,20):
    if i <= 10:
        a = i
    else:
        a -= 1
    print(a, end=',')

print()

#problem6
names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
for i in range(0,13,2):
    print(names[i])
print()
#problems7
names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
for i in range(1,13,2):
    print(names[i])

print()

#problems9
z = 0
a = []
b = []
for i in range(-100,100):
    if i % 13 == 0 and i % 2 == 0:
        a.append(i**2)
    z+=1
    if z % 7 == 0 and i % 2 != 0:
        print(i)
        b.append(i)
print(len(a))
print(len(b))

print()
#problem8
print("ВЫ МОЖЕТЕ ВЫЙТИ ПРОСТО ВВЕДИТЕ В ТЕРМИНАЛ '0' (это ноль) ")   
while True:
    a = int(input('Введите число: '))
    if a > 99 and a < 1000:
        print('Ваше число трёхзначное')
    if (a >= 0 and a % 2 == 0):
        print('Ваше число положительное и чётное')
    if a % 31 == 0:
        print('Ваше число делится на 31')
    if (a >= 100 and a % 17 == 0):
        print('Ваше число больше и делится на 17', a)
    elif (a >= 150 and a == 13**2):
        print('Ваше число больше 150 и равно к 13**2!', a)
    if a == 0:
        break
print("ВЫ МОЖЕТЕ ВЫЙТИ ПРОСТО ВВЕДИТЕ В ТЕРМИНАЛ '0' (это ноль) ")     
