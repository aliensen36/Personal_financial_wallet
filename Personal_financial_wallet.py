import os

# Вывод текущего баланса
def show_balance(records):
    total_income = sum(record['amount'] for record in records if record['category'] == 'Доход')
    total_expense = sum(record['amount'] for record in records if record['category'] == 'Расход')
    total_balance = total_income - total_expense
    print(f"Текущий баланс: {total_balance}")
    print(f"Доходы: {total_income}")
    print(f"Расходы: {total_expense}")

# Добавление записи
def add_record(records):
    print("Введите данные о новой записи:")
    date = input("Дата (гггг-мм-дд): ")
    category_code = input("Выберите категорию (1 - Доход, 2 - Расход): ")
    category = 'Доход' if category_code == '1' else 'Расход'
    amount = float(input("Сумма: "))
    description = input("Описание: ")
    records.append({'date': date, 'category': category, 'amount': amount, 'description': description})
    print("Запись успешно добавлена!")

# Редактирование записи
def edit_record(records):
    print("Введите номер записи, которую хотите отредактировать:")
    for i, record in enumerate(records):
        print(f"{i + 1}. {record['date']} - {record['category']} - {record['amount']} - {record['description']}")
    try:
        index = int(input("Номер записи: ")) - 1
        if 0 <= index < len(records):
            print("Выберите поле для редактирования:")
            print("1. Дата")
            print("2. Категория")
            print("3. Сумма")
            print("4. Описание")
            choice = input("Введите номер поля: ")
            if choice == '1':
                records[index]['date'] = input("Введите новую дату (гггг-мм-дд): ")
            elif choice == '2':
                category_code = input("Выберите новую категорию (1 - Доход, 2 - Расход): ")
                records[index]['category'] = 'Доход' if category_code == '1' else 'Расход'
            elif choice == '3':
                records[index]['amount'] = float(input("Введите новую сумму: "))
            elif choice == '4':
                records[index]['description'] = input("Введите новое описание: ")
            else:
                print("Некорректный ввод.")
        else:
            print("Некорректный номер записи.")
    except ValueError:
        print("Некорректный ввод.")


# Поиск записи
def search_records(records):
    print("Выберите критерии для поиска:")
    print("1. По категории")
    print("2. По дате")
    print("3. По сумме")
    choice = input("Введите номер критерия: ")
    if choice == '1':
        category_code = input("Выберите категорию (1 - Доход, 2 - Расход): ")
        category = 'Доход' if category_code == '1' else 'Расход'
        found_records = [record for record in records if record['category'] == category]
    elif choice == '2':
        date = input("Введите дату (гггг-мм-дд): ")
        found_records = [record for record in records if record['date'] == date]
    elif choice == '3':
        amount = float(input("Введите сумму: "))
        found_records = [record for record in records if record['amount'] == amount]
    else:
        print("Некорректный ввод.")
        return

    if found_records:
        print("Найденные записи:")
        for record in found_records:
            print(
                f"Дата: {record['date']}, Категория: {record['category']}, Сумма: {record['amount']}, Описание: {record['description']}")
    else:
        print("Записи не найдены.")


# Сохранение записей в файл
def save_records_to_file(records, filename):
    with open(filename, 'w') as file:
        for record in records:
            file.write(f"Дата: {record['date']}, Категория: {record['category']}, Сумма: {record['amount']}, Описание: {record['description']}\n")
    print("Данные сохранены в файл.")

# Показ записей из файла
def show_file_content(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            print("Содержимое файла:")
            for line in file:
                print(line.strip())
    else:
        print("Файл не найден.")


# Загрузка записей из файла
def load_records_from_file(filename):
    records = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            record = {}
            for line in lines:
                line = line.strip()
                if line:
                    key, value = line.split(':', 1)  # Ограничение до одного разбиения
                    record[key.strip()] = value.strip()  # Убираем лишние пробелы
                else:
                    records.append(record)
                    record = {}
            if record:
                records.append(record)
    return records


# Имя файла для хранения данных
filename = "financial_records.txt"


def main():
    records = load_records_from_file(filename)
    while True:
        print("\nЛичный финансовый кошелек")
        print("1. Просмотр баланса")
        print("2. Добавить запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Сохранить записи в файл")
        print("6. Показать содержимое файла")
        print("0. Выйти из программы")
        choice = input("Выберите действие: ")

        if choice == "1":
            show_balance(records)
        elif choice == "2":
            add_record(records)
        elif choice == "3":
            edit_record(records)
        elif choice == "4":
            search_records(records)
        elif choice == "5":
            save_records_to_file(records, filename)
        elif choice == "6":
            show_file_content(filename)
        elif choice == "0":
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите действие из списка.")


if __name__ == "__main__":
    main()
