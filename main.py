# zavda1
# def filter_words(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as infile:
#         text = infile.read()
#
#     words = text.split()
#
#     long_words = [word for word in words if len(word) >= 7]
#
#     with open(output_file, 'w', encoding='utf-8') as outfile:
#         outfile.write("\n".join(long_words))
#
# input_file = 'input.txt'
# output_file = 'output.txt'
#
# filter_words(input_file, output_file)
#
# print(f"Всі слова довжиною 7 і більше літер були записані в '{output_file}'")
#
#  zavda2
# def copy_lines(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as infile:
#         lines = infile.readlines()
#
#     with open(output_file, 'w', encoding='utf-8') as outfile:
#         outfile.writelines(lines)
#
# input_file = 'input.txt'
# output_file = 'output.txt'
#
# copy_lines(input_file, output_file)
#
# print(f"Рядки з файлу '{input_file}' були переписані в '{output_file}'")

# zav3
# with open('input.txt', 'r', encoding='utf-8') as infile:
#     lines = infile.readlines()
#
# with open('output.txt', 'w', encoding='utf-8') as outfile:
#     for line in reversed(lines):
#         outfile.write(line)

# zav4
# with open('input.txt', 'r', encoding='utf-8') as infile:
#     lines = infile.readlines()
#
# star_line_added = False
#
# for i in range(len(lines)-1, -1, -1):
#     if ',' not in lines[i]:
#         lines.insert(i+1, '************\n')
#         star_line_added = True
#         break
#
# if not star_line_added:
#     lines.append('************\n')
#
# with open('output.txt', 'w', encoding='utf-8') as outfile:
#     outfile.writelines(lines)

# zav5
# char = input("Введіть символ, з якого повинні починатися слова: ")
#
# if len(char) != 1:
#     print("Будь ласка, введіть лише один символ.")
# else:
#     with open('input.txt', 'r', encoding='utf-8') as infile:
#         text = infile.read()
#
#     words = text.split()
#
#     count = sum(1 for word in words if word.lower().startswith(char.lower()))
#
#     print(f"Кількість слів, що починаються з '{char}': {count}")

# zav6
# with open('input.txt', 'r', encoding='utf-8') as infile:
#     lines = infile.readlines()
#
# with open('output.txt', 'w', encoding='utf-8') as outfile:
#     for line in lines:
#         modified_line = line.replace('*', 'TEMP').replace('&', '*').replace('TEMP', '&')
#         outfile.write(modified_line)

# zav7
# lines = ["Перший рядок", "Другий рядок", "Третій рядок", "Четвертий рядок"]
#
# with open('output.txt', 'w', encoding='utf-8') as outfile:
#     for line in lines:
#         outfile.write(line + '\n')

# zav8
# lines = ["Перший рядок", "Другий рядок", "Третій рядок", "Четвертий рядок"]
#
# with open('output.txt', 'w', encoding='utf-8') as outfile:
#     outfile.write("\n".join(lines))

# zav9
# with open('input.txt', 'r', encoding='utf-8') as infile:
#     text = infile.read()
#
# char_count = len(text)
#
# print(f"Кількість символів у файлі: {char_count}")

# zav10
# with open('input.txt', 'r', encoding='utf-8') as infile:
#     lines = infile.readlines()
#
# line_count = len(lines)
#
# print(f"Кількість рядків у файлі: {line_count}")

# zav1
# with open('file1.txt', 'r', encoding='utf-8') as file1:
#     lines1 = file1.readlines()
#
# with open('file2.txt', 'r', encoding='utf-8') as file2:
#     lines2 = file2.readlines()
#
# max_len = max(len(lines1), len(lines2))
#
# for i in range(max_len):
#     line1 = lines1[i] if i < len(lines1) else ''
#     line2 = lines2[i] if i < len(lines2) else ''
#
#     if line1 != line2:
#         print(f"Рядок {i + 1} не співпадає:")
#         print(f"Файл 1: {line1.strip()}")
#         print(f"Файл 2: {line2.strip()}")
#         print('-' * 40)

# zav2
# def is_vowel(c):
#     return c.lower() in 'аеєиіїоуюяАЕЄИІЇОУЮЯ'
#
# def is_consonant(c):
#     return c.lower() in 'бвгдеєжзиійклмнопрстуфхцчшщБВГДЕЄЖЗИІЙКЛМНОПРСТУФХЦЧШЩ'
#
# with open('input.txt', 'r', encoding='utf-8') as infile:
#     text = infile.read()
#
# num_chars = len(text)
# num_lines = text.count('\n') + 1
# num_vowels = sum(1 for c in text if is_vowel(c))
# num_consonants = sum(1 for c in text if is_consonant(c))
# num_digits = sum(1 for c in text if c.isdigit())
#
# with open('statistics.txt', 'w', encoding='utf-8') as outfile:
#     outfile.write(f"Кількість символів: {num_chars}\n")
#     outfile.write(f"Кількість рядків: {num_lines}\n")
#     outfile.write(f"Кількість голосних літер: {num_vowels}\n")
#     outfile.write(f"Кількість приголосних літер: {num_consonants}\n")
#     outfile.write(f"Кількість цифр: {num_digits}\n")
#
# print("Статистика записана в файл 'statistics.txt'.")

# zav3
# with open('input.txt', 'r', encoding='utf-8') as infile:
#     lines = infile.readlines()
#
# lines = lines[:-1]
#
# with open('output.txt', 'w', encoding='utf-8') as outfile:
#     outfile.writelines(lines)
#
# print("Останній рядок було видалено, і результат записано в 'output.txt'.")

# zav4
# with open('input.txt', 'r', encoding='utf-8') as infile:
#     lines = infile.readlines()
#
# max_length = max(len(line) for line in lines)
#
# print(f"Довжина найдовшого рядка: {max_length}")

# zav5
# word_to_count = input("Введіть слово для підрахунку: ").strip()
#
# with open('input.txt', 'r', encoding='utf-8') as infile:
#     text = infile.read()
#
# word_count = text.lower().split().count(word_to_count.lower())
#
# print(f"Кількість входжень слова '{word_to_count}': {word_count}")

# zav6
# word_to_find = input("Введіть слово, яке потрібно знайти: ").strip()
# word_to_replace = input("Введіть слово, на яке замінити: ").strip()
#
# with open('input.txt', 'r', encoding='utf-8') as infile:
#     text = infile.read()
#
# updated_text = text.replace(word_to_find, word_to_replace)
#
# with open('input.txt', 'w', encoding='utf-8') as outfile:
#     outfile.write(updated_text)
#
# print(f"Всі входження слова '{word_to_find}' було замінено на '{word_to_replace}'.")