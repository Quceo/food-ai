from openai import OpenAI


def get_client(): # Функция, которая будет создавать общение пользователя и ИИ

   with open("api_key.txt", "r") as f: # Чтения файла api_key.text и передача его данных в переменную
    api_key = f.read().strip()

    return OpenAI( # Создаем клиента
        api_key=api_key, #api пользователя в другом файле для большей защищенности
        base_url='https://openrouter.ai/api/v1'
        #base_url='' - Использовать если используется неофициальный API...................
    )
