import subprocess


def execute_command(command, text_to_find):
    try:
        # Выполняем команду и захватываем вывод
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Проверяем, содержит ли вывод нужный текст
        if result.returncode == 0 and text_to_find in result.stdout:
            return True
        else:
            return False
    except Exception as e:
        print("Произошла ошибка:", e)
        return False


# Пример использования
command = "ls -l"
text_to_find = "example_file.txt"
if execute_command(command, text_to_find):
    print("Текст найден в выводе команды.")
else:
    print("Текст не найден в выводе команды или произошла ошибка при выполнении команды.")
