import os
import datetime

# Функция для вывода текущего баланса
def show_balance(records):
    total_income = sum(record['amount'] for record in records if record['category'] == 'Доход')
    total_expense = sum(record['amount'] for record in records if record['category'] == 'Расход')
    total_balance = total_income - total_expense
    print(f"Текущий баланс: {total_balance}")
    print(f"Доходы: {total_income}")
    print(f"Расходы: {total_expense}")

# Функция для добавления записи
def add_record(records):
    print("Введите данные о новой записи:")
    date = input("Дата (гггг-мм-дд): ")
    category = input("Категория (Доход/Расход): ")
    amount = float(input("Сумма: "))
    description = input("Описание: ")
    records.append({'date': date, 'category': category, 'amount': amount, 'description': description})
    print("Запись успешно добавлена!")

# Функция для сохранения записей в файл
def save_records_to_file(records, filename):
    with open(filename, 'w') as file:
        for record in records:
            file.write(f"Дата: {record['date']}\n")
            file.write(f"Категория: {record['category']}\n")
            file.write(f"Сумма: {record['amount']}\n")
            file.write(f"Описание: {record['description']}\n")
            file.write('\n')

# Функция для загрузки записей из файла
def load_records_from_file(filename):
    records = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            record = {}
            for line in lines:
                line = line.strip()
                if line:
                    key, value = line.split(': ')
                    record[key] = value
                else:
                    records.append(record)
                    record = {}
            if record:
                records.append(record)
    return records

# Основная функция для выполнения программы
def main():
    filename = 'finance_records.txt'
    records = load_records_from_file(filename)
    while True:
        print("\nВыберите действие:")
        print("1. Вывести текущий баланс")
        print("2. Добавить новую запись")
        print("3. Выйти из программы")
        choice = input("Введите номер действия: ")
        if choice == '1':
            show_balance(records)
        elif choice == '2':
            add_record(records)
        elif choice == '3':
            save_records_to_file(records, filename)
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
