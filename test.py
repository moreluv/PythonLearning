inventory = ["Меч", "Щит", "Зелье", "Шлем", "Нагрудник", "Лук", "Стрелы"]
print(inventory)
print(len(inventory))
inventory.append("Монеты")
print(inventory)
item = inventory.pop(3)
print(item)
del inventory[1]
print(inventory)
print(sorted(inventory))

