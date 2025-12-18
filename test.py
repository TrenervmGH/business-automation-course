print("Этот код я написал САМ")

name = input("Введите ваше имя: ")
print(f"Привет, {name}!")

with open('my_test.txt', 'w', encoding='cp1251') as f:
    f.write(f"Тест пользователя, {name}!")