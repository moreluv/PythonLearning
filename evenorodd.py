while True:
    print("Введите любое целок число, если хотите выйти напишите 0")
    num = int(input())
    if num % 2 == 0 and num != 0:
        print("Число четное")
    elif num == 0:
        break
    else:
        print("Число нечетное")
