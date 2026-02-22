balance = 1000

while True:
    print("\n--- БАНКОВСКИЙ ТЕРМИНАЛ ---")
    print("1. Проверить баланс")
    print("2. Пополнить баланс")
    print("3. Снять деньги")
    print("4. Выход")

    choice = int(input())
    if choice == 1:
        print(balance)
        continue
    if choice == 2:
        print("На сколько вы хотите пополнить свой баланс?")
        add_balance = int(input())
        balance += add_balance
        continue
    if choice == 3:
        print("Сколько вы хотите снять со своего баланса?")
        out_balance = int(input())
        if balance < out_balance:
            print("Ошибка, недостаточно средств")
        else:
            balance -= out_balance
            continue
    if choice == 4:
        print("До свидания!")
        break
