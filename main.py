import requests
import time
import os

# Отримуємо токен із секретів
TOKEN = os.getenv('BOT_TOKEN')

GROUP_IDS = [
    '-1002326963395',  # Tuluzy
    '-1002501031375'   # Zhilyanskaya
]

TEXT = 'Вітаю, прошу надати інформацію стосовно замовлень!'
url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

for chat_id in GROUP_IDS:
    payload = {'chat_id': chat_id, 'text': TEXT}
    response = requests.post(url, data=payload)
    print(f'Відправлено до {chat_id}: {response.status_code} - {response.text}')
    time.sleep(1)
