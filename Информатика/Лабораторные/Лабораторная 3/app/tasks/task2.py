import re
from string import printable # Digits + letters + space + \t + \n + special simbols

def solve(string):
    """ 466730 % 6 = 2 =>
    Дан текст. Необходимо найти в нём каждый фрагмент, где сначала идёт слово «ВТ»,
    затем не более 4 слов, и после этого идёт слово «ИТМО».
    Для простоты будем считать словом любую последовательность букв, цифр и знаков
    «_» (то есть символов \\w).
    """
    remove_chars = ''.join(c for c in printable if not c.isalnum() and c not in (' ', '\n', '\t', '_')) # Создаем строку с символами, которые нужно удалить
    translation_table = str.maketrans('', '', remove_chars) # Создаем таблицу перевода для удаления специальных символов
    cleaned_string = re.sub(r'\s+', ' ', string.translate(translation_table)).strip() # Удаляем специальные символы и обрабатываем пробелы

    #pattern = r'\bВТ\b(?:\s+\w+){,4}\s+\bИТМО\b' # Шаблон для нахождения "ВТ (<= 4 слова) ИТМО"

    results = []
    
    # Теперь ищем все "ВТ" и "ИТМО" в строке
    vt_positions = [m.start() for m in re.finditer(r'\bВТ\b', cleaned_string)]
    itmo_positions = [m.start() for m in re.finditer(r'\bИТМО\b', cleaned_string)]

    for vt_pos in vt_positions:
        for itmo_pos in itmo_positions:
            if vt_pos < itmo_pos:  # "ВТ" должно быть перед "ИТМО"
                # Извлекаем текст между ними
                segment = cleaned_string[vt_pos:itmo_pos + len("ИТМО")]
                words_between = cleaned_string[vt_pos+3:itmo_pos].split() #+3, т.к. нужно следующее слово после ВТ, т.е. "В"+"Е"+" " == 3
                if len(words_between) <= 4:
                    results.append(segment)

    return results