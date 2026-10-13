def binary_search(numbers, target):
    """
    Ищет необходимое число в введенном отсортированном списке.
    Возвращает индекс найденного элемента или None))
    """
    if not isinstance(numbers, list):
        raise TypeError("Первый аргумент должен быть списком.")

    if len(numbers) == 0:
        raise ValueError("Список не должен быть пустым.")

    if not all(type(x) in (int, float) for x in numbers):
        raise TypeError("Список должен содержать только числа.")

    if type(target) not in (int, float):
        raise TypeError("Искомое значение должно быть числом.")

    if any(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1)):
        raise ValueError("Список должен быть отсортирован по возрастанию.")

    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return None


# Пример 1. Поиск существующего элемента
def example_found():
    print("\nПример 1: поиск существующего элемента")
    print("Список: [1, 3, 5, 7, 9]")
    print("Искомое число: 5")
    print("Результат:", binary_search([1, 3, 5, 7, 9], 5))


# Пример 2. Поиск первого элемента
def example_first():
    print("\nПример 2: поиск первого элемента")
    print("Результат:", binary_search([2, 4, 6, 8], 2))


# Пример 3. Поиск отсутствующего элемента
def example_missing():
    print("\nПример 3: элемент отсутствует")
    print("Результат:", binary_search([1, 3, 5, 7], 4))


# Пример 4. Ошибка из-за несортированного списка
def example_unsorted():
    print("\nПример 4: несортированный список")
    try:
        binary_search([5, 2, 8, 1], 8)
    except (TypeError, ValueError) as error:
        print("Сообщение об ошибке:", error)


# Пример 5. Ошибка из-за неправильного типа данных
def example_wrong_type():
    print("\nПример 5: неправильный тип аргумента")
    try:
        binary_search("1, 2, 3", 2)
    except (TypeError, ValueError) as error:
        print("Сообщение об ошибке:", error)


def run_examples():
    """Запускает все демонстрационные примеры."""
    example_found()
    example_first()
    example_missing()
    example_unsorted()
    example_wrong_type()


def main():
    """Главное меню программы."""
    while True:
        print("\n=== БИНАРНЫЙ ПОИСК ===")
        print("1. Выполнить поиск")
        print("2. Показать примеры")
        print("0. Завершить программу")

        choice = input("Выберите действие: ")

        if choice == "1":
            try:
                text = input("Введите отсортированный список чисел через пробел: ")
                numbers = [float(x) for x in text.split()]

                if not numbers:
                    raise ValueError("Список не должен быть пустым.")

                target = float(input("Введите искомое число: "))

                result = binary_search(numbers, target)

                if result is None:
                    print("Элемент не найден. Результат: None")
                else:
                    print("Элемент найден. Индекс:", result)

            except ValueError as error:
                print("Ошибка:", error)
            except TypeError as error:
                print("Ошибка:", error)

        elif choice == "2":
            run_examples()

        elif choice == "0":
            print("Программа завершена.")
            break

        else:
            print("Ошибка: выберите 1, 2 или 0.")


if __name__ == "__main__":
    main()
