import threading
import os

def process_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()

        modified_content = content.replace('old_word', 'new_word')

        base_name = os.path.basename(file_name)

        new_file_name = f"modified_{base_name}"

        with open(new_file_name, 'w', encoding='utf-8') as new_file:
            new_file.write(modified_content)

        print(f"Файл {file_name} обработан b сохранен как {new_file_name}")
    except Exception as e:
        print(f"Ошибка при обработке файла {file_name}: {str(e)}")

file_list = ['file1.txt', 'file2.txt', 'file3.txt']

threads = []
for file_name in file_list:
    thread = threading.Thread(target=process_file, args=(file_name,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Все файлы обработаны.")
