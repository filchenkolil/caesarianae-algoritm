lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
algorithm_types = ['шифрование', 'дешифрование']
languages = ['русский', 'английский']


def is_algorithm_types_validation(text):
    if text in algorithm_types:
        return True
    else:
        return False


def is_languages_validation(text):
    if text in languages:
        return True
    else:
        return False


def is_digit_validation(text):
    if text.isdigit():
        return True
    else:
        return False


def read_algorithm_types():
    while True:
        user_input = input().lower()
        if is_algorithm_types_validation(user_input):
            return user_input
        else:
            print('Некорректный ввод. Попробуй еще раз')


def read_language():
    while True:
        language_type_user_input = input().lower()
        if is_languages_validation(language_type_user_input):
            return language_type_user_input
        else:
            print('Некорректный ввод. Попробуй еще раз')


def read_shift_step():
    while True:
        number = input()
        if is_digit_validation(number):
            return int(number)
        else:
            print('Некорректный ввод. Введите числовое значение.')


def get_alphabet(language):
    if language == 'русский':
        return lower_rus_alphabet
    else:
        return lower_eng_alphabet


def find_index(alphabet, text):
    text = text.lower()
    return alphabet.find(text)


def calculate_new_index(index, step, type):
    if language == 'русский':
        if type == 'шифрование':
            return (index + step) % 32
        else:
            return (index - step) % 32
    else:
        if type == 'шифрование':
            return (index + step) % 26
        else:
            return (index - step) % 26


def get_letter_by_index(alphabet, index, is_upper):
    if is_upper:
        return ''.join(alphabet[index]).upper()
    else:
        return ''.join(alphabet[index])


def caesar(text, step, type):
    output = ''

    for i in range(len(text)):
        letter = text[i]

        if letter.isalpha():
            current_alphabet = get_alphabet(language)
            index = find_index(current_alphabet, letter)
            new_index = calculate_new_index(index, step, type)
            output += get_letter_by_index(current_alphabet, new_index, letter.isupper())
        else:
            output += letter

    print(output)


print('Выберите направление: шифрование или дешифрование')
algorithm_choice = read_algorithm_types()
print('Выберите язык текста: русский или английский')
language = read_language()
user_data = input('Введите текст:\n')
print('Введите шаг сдвига:')
shift_step = read_shift_step()
caesar(user_data, shift_step, algorithm_choice)