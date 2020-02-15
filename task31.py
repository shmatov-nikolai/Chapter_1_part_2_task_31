'''
Напишите функцию которая подсчитает количество строк, слов и букв в текстовом
файле.
'''

import os


def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def get_words_dict(words):
    words_dict = dict()
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def get_letter_in_text(words):
    letter_string = ""
    letter_string = str(words)
    letter_string = letter_string.replace(" ", "")
    return letter_string


def main():
    filename = input("Введите путь к файлу: ")
    file_for_lines = open(filename) 
    lines = [x for x in file_for_lines.readlines() if x != "\n"]
    if not os.path.exists(filename):
        print("Указанный файл не существует")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        letter_string = get_letter_in_text(words)

        print("строк в тексте: " + str(len(lines)))
        print("Кол-во слов: %d" % len(words))
        print("Кол-во уникальных слов: %d" % len(words_dict))
        print(f'количество букв в тексте: {len(letter_string)}')   

if __name__ == "__main__":
    main()