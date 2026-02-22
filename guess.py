import random
x = random.randint(1, 10)
print("Добро пожаловать в игру 'Угодайка', попробуй угодать число целое от 1 до 10 ")
y = int(input())
if y > 10:
    print("Введённое число больше 10")
elif y < 1:
    print("Введеное число меньше 1")
while y != x:
    if y > x:
        print("Не угадал, загаданное число меньше")
        y = int(input())
    elif y < x:
        print("Не угадал, загаданное число больше")
        y = int(input())

if y == x:
    print("Молодец! Ты угадал!")
