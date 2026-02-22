balance = 1000
attempts = 3
pin = 1612
while attempts > 0 and True:
    print("Введите пин")
    user_pin = int(input())
    if pin != user_pin:
        attempts -= 1
        print("Неверный пинкод, осталось попыток", attempts)
    else:
        while True:
            print("\n--- БАНКОВСКИЙ ТЕРМИНАЛ ---")
            print("1. Проверить баланс")
            print("2. Пополнить баланс")
            print("3. Снять деньги")
            print("4. Выход")

            user_input = input()
            if not user_input.isdigit():  # Проверка: введено ли число? [8, 9]
                print("Ошибка: введите цифру от 1 до 4.")
                continue

            choice = int(user_input)
            if choice == 1:
                print(balance)
            elif choice == 2:
                print("На сколько вы хотите пополнить свой баланс?")
                add_balance = int(input())
                balance += add_balance
            elif choice == 3:
                print("Сколько вы хотите снять со своего баланса?")
                out_balance = int(input())
                if balance < out_balance:
                    print("Ошибка, недостаточно средств")
                else:
                    balance -= out_balance
            elif choice == 4:
                print("До свидания!")
                break
            else:
                print("Ошибка, введите число из предложенных")
        break