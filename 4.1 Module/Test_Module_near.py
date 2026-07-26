def my_func():
    return 'Hello, this is the test of connection - from the SAME folder!'

import pathlib
import sys
# 1. Повний шлях до файлу (наприклад: /home/user/project/script.py)
full_path = sys.argv[0]
# 2. Отримуємо тільки чисте ім'я файлу (script.py)
file_name = pathlib.Path(full_path).name

print(f"Ім'я файлу, що виконується: {file_name}")