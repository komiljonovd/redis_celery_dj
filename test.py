import requests
import time

# Замени на URL твоего локального API
URL = "http://localhost:8000/api/v1/news-list/" 

print("Начинаем DDOS-атаку на локальный API...")

while True:

    for i in range(1, 35):
        response = requests.get(URL)
        
        if response.status_code == 200:
            print(f"[{i}] ✅ Успешно: 200 OK")
            print(response.text)
        elif response.status_code == 429:
            print(f"[{i}] 🛑 ЗАБЛОКИРОВАНО Rate Limit! Статус: 429")
            print("Ответ сервера:", response.json())
            time.sleep(60)
            break
        else:
            print(f"[{i}] ⚠️ Неожиданный статус: {response.status_code}")
            
