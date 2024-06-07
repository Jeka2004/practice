def print_twinkle():
    print("Twinkle, twinkle, little star,")
    print("\tHow I wonder what you are!")
    print("\t\tUp above the world so high,")
    print("\t\tLike a diamond in the sky.")
    print("Twinkle, twinkle, little star,")
    print("\tHow I wonder what you are")

print_twinkle()

import math


def calculate_area_of_circle():
    radius = float(input("Введіть радіус кола: "))

    area = math.pi * (radius ** 2)

    print(f"Площа кола з радіусом {radius} дорівнює {area:.2f}")


calculate_area_of_circle()

color_list = ["Red", "Green", "White", "Black"]

first_color = color_list[0]
last_color = color_list[-1]

print("Перший колір у списку:", first_color)
print("Останній колір у списку:", last_color)


def calculate_expression(n):
    nn = int(str(n) * 2)
    nnn = int(str(n) * 3)

    result = n + nn + nnn

    return result


n = int(input("Введіть ціле число: "))

result = calculate_expression(n)

print(f"Результат обчислення n + nn + nnn для n = {n} дорівнює {result}")

def print_even_numbers(numbers):
    for number in numbers:
        if number == 237:
            break
        if number % 2 == 0:
            print(number)

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527]

print_even_numbers(numbers)

import re


def check_sequence(sequence):
    zero_sequences = re.findall(r'0+', sequence)
    one_sequences = re.findall(r'1+', sequence)

    if len(zero_sequences) != len(one_sequences):
        return False

    for zero_seq, one_seq in zip(zero_sequences, one_sequences):
        if len(zero_seq) != len(one_seq):
            return False

    return True


sequence1 = "01010101"
sequence2 = "00011100011"

print(check_sequence(sequence1))
print(check_sequence(sequence2))

def print_even_numbers(n, m):
    # Перебираємо числа від -n до n із кроком m
    for i in range(-n, n + 1, m):
        # Перевіряємо, чи є число парним
        if i % 2 == 0:
            print(i)

# Введення значень n і m
n = int(input("Введіть значення n: "))
m = int(input("Введіть значення m (порядковий номер студента у журналі): "))

# Викликаємо функцію для друку парних чисел
print_even_numbers(n, m)

import math

def calculate_combinations(m):
    if m > 25:
        return 0
    return math.factorial(25) // math.factorial(25 - m)

m = int(input("Введіть порядковий номер студента у журналі (m): "))

combinations = calculate_combinations(m)

print(f"Кількість можливих комбінацій для паролю довжиною {m} символів: {combinations}")

my_list = [1, 2, 3, 4, 5]

L = [3, 6, 7]
my_list.extend(L)
print("Після додавання елементів L:", my_list)

my_list.insert(1, 33333)
print("Після вставки 33333 на другий елемент:", my_list)

my_list.reverse()
print("У зворотному порядку:", my_list)

my_list.append(3)
print("Після додавання 3 в кінець списку:", my_list)

my_list.remove(3)
print("Після видалення першого 3:", my_list)

my_list.sort()
print("У порядку збільшення:", my_list)

my_list.clear()
print("Після очищення списку:", my_list)


def display_menu():
    print("\nМеню:")
    print("1. Показати карту читача")
    print("2. Взяти книгу")
    print("3. Повернути книгу")
    print("0. Вийти з програми")


def show_reader_card(reader):
    print("\nКарта читача:")
    print(f"ID: {reader['ID']}")
    print(f"Прізвище: {reader['Прізвище']}")
    print(f"Ім’я: {reader['Ім’я']}")
    print(f"Група: {reader['Група']}")
    print(f"Курс: {reader['Курс']}")
    print(f"Книги (борг): {', '.join(reader['Книги (борг)']) if reader['Книги (борг)'] else 'Немає'}")
    print(f"Статистика книг: {', '.join(reader['Статистика книг']) if reader['Статистика книг'] else 'Немає'}")


def take_book(reader):
    book_name = input("Введіть назву книги, яку хочете взяти: ")
    reader['Книги (борг)'].append(book_name)
    print(f"Книга '{book_name}' додана в борг.")


def return_book(reader):
    if not reader['Книги (борг)']:
        print("У вас немає книг у боргу.")
        return

    print("Ваші книги у боргу:")
    for book in reader['Книги (борг)']:
        print(book)

    book_name = input("Введіть назву книги, яку хочете повернути: ")
    if book_name in reader['Книги (борг)']:
        reader['Книги (борг)'].remove(book_name)
        reader['Статистика книг'].append(book_name)
        print(f"Книга '{book_name}' повернута та додана у статистику.")
    else:
        print(f"Книга '{book_name}' відсутня у вашому списку боргу.")


# Дані користувача
reader = {
    'ID': 1,
    'Прізвище': 'Скрипник',
    'Ім’я': 'Євгеній',
    'Група': 'ІПЗс-21-1',
    'Курс': 3,
    'Книги (борг)': [],
    'Статистика книг': []
}

while True:
    display_menu()
    choice = input("Введіть ваш вибір: ")

    if choice == '1':
        show_reader_card(reader)
    elif choice == '2':
        take_book(reader)
    elif choice == '3':
        return_book(reader)
    elif choice == '0':
        print("Вихід з програми...")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")