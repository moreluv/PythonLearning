import random

player_score = 0
computer_score = 0
options = ['камень', 'ножницы', 'бумага']

print("Играем до 3-х побед!")

while player_score < 3 and computer_score < 3:
    user_choice = input("Ваш выбор (камень, ножницы, бумага): ").lower().strip()

    if user_choice not in options:
        print("Некорректный ввод, попробуй еще раз.")
        continue

    computer_choice = random.choice(options)
    print(f"Компьютер выбрал: {computer_choice}")

    # Твоя логика сравнения здесь...
    # Например:
    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
            (user_choice == 'ножницы' and computer_choice == 'бумага') or \
            (user_choice == 'бумага' and computer_choice == 'камень'):
        print("Вы выиграли раунд!")
        player_score += 1
    else:
        print("Компьютер выиграл раунд!")
        computer_score += 1

    print(f"Счет — Вы: {player_score}, Компьютер: {computer_score}\n")

print("Игра окончена!")
