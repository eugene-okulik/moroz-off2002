import os
import re
from datetime import datetime
import argparse
from colorama import init, Fore, Style


def parse_args():
    parser = argparse.ArgumentParser(description="Анализатор лог-файлов")
    parser.add_argument("path", help="Путь к файлу или папке с логами")
    parser.add_argument("--text", required=True, help="Искомый текст внутри ошибок")
    parser.add_argument("--first_only", action="store_true", help="Вывести только первое найденное совпадение")

    return parser.parse_args()


def process_file(file_path, log_data):
    """Обработка файла и сохранение его содержимого в структуре log_data"""
    filename = os.path.basename(file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Разделение файла на отдельные блоки логов
        blocks = re.split(r'(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}(?:\.\d+)?)\s+', content)[1:]

        # Формирование структуры log_data
        i = iter(blocks)
        for timestamp, block in zip(i, i):
            log_data.setdefault(timestamp.strip(), []).append((filename, block))


def read_files_or_single_file(path):
    """Чтение файла или всей папки"""
    log_data = {}

    if os.path.isfile(path):
        # Обрабатываем одиночный файл
        process_file(path, log_data)
    elif os.path.isdir(path):
        # Обрабатываем все файлы в каталоге
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                process_file(file_path, log_data)
    else:
        raise ValueError(f"Указанный путь '{path}' не является ни файлом, ни папкой!")

    return log_data


def search_text(log_data, text, first_only=False):
    """Поиск текста среди записей логов (регистронезависимо)"""
    results = []
    lower_case_text = text.lower()  # Приводим искомый текст к нижнему регистру заранее

    for timestamp, logs in sorted(log_data.items()):
        for filename, block in logs:
            # Приводим блок к нижнему регистру для сопоставления
            if lower_case_text in block.lower():
                words = block.replace("\n", " ").split()  # Преобразовываем в список слов
                index = next((i for i, w in enumerate(words) if lower_case_text in w.lower()), None)

                if index is not None:
                    # Определяем границы окна слов
                    start_word_idx = max(index - 5, 0)
                    end_word_idx = min(index + 6, len(words))  # Включаем само слово и ещё 5 после

                    # Создание сниппета из выбранного диапазона слов
                    snippet_words = words[start_word_idx:end_word_idx]
                    snippet = " ".join(snippet_words)

                    results.append({
                        'timestamp': timestamp,
                        'file_name': filename,
                        'snippet': snippet
                    })

                    if first_only:
                        return results

    return results


def print_results(results):
    """Раскрашивание результата"""
    init(autoreset=True)

    for result in results:
        print(f"{Fore.BLUE}{result['timestamp']} {Style.RESET_ALL}"
              f"{Fore.GREEN}{result['file_name']} {Style.RESET_ALL}- "
              f"{Fore.YELLOW}{result['snippet']}")


if __name__ == "__main__":
    args = parse_args()
    path = args.path
    target_text = args.text
    first_only = args.first_only

    try:
        log_data = read_files_or_single_file(path)
        results = search_text(log_data, target_text, first_only=first_only)

        if len(results) > 0:
            print_results(results)
        else:
            print(f"Текст '{target_text}' не найден ни в одном файле.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
