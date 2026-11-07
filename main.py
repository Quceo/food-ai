from json import loads #Импортируем функцию loads для превращения строки в JSON
from prompt import get_recipes #Берем функцию из prompt.py

products = input("Какие продукты у вас есть? \n") #Получение информации по продуктам
print("\nИщу рецепты...\n")

result = get_recipes(products) #Вызов функции из prompt.py

data = loads(result) #Превращаем текстовый ответ в JSON-файл

for dish in data["блюда"]:
    print("\n" + "=" * 40)
    print(dish["название"])
    print("=" * 40)

    print("\nИнгредиенты:")
    for ingredient in dish["ингредиенты"]:
        print(f"- {ingredient}")

    print("\nПриготовление:")
    for i, step in enumerate(dish["приготовление"], 1):
        print(f"{i}. {step}")

    print("\nНедостающие продукты:")
    if dish.get("недостающие_продукты"):
        for product in dish["недостающие_продукты"]:
            print(f"- {product}")
    else:
        print("Нет")
