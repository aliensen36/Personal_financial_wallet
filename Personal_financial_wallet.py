import os

# Класс записей в Финансовом кошельке
class Record:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.description = description

# Класс Финансовый кошелек
class FinancialWallet:
    def __init__(self, filename):
        self.filename = filename
        self.records = self.load_records_from_file()

    # Функция загрузки записей из файла
    def load_records_from_file(self):
        records = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if line:
                        record_data = self.parse_record(line)
                        records.append(Record(**record_data))
        return records

    def parse_record(self, line):
        data = {}
        parts = line.split(', ')
        for part in parts:
            key, value = part.split(': ')
            key = key.strip().lower()
            value = value.strip()
            if key == 'дата':
                key = 'date'
            elif key == 'категория':
                key = 'category'
            elif key == 'сумма':
                key = 'amount'
            elif key == 'описание':
                key = 'description'
            data[key] = value
        return data

    # Функция сохранения записей в файл
    def save_records_to_file(self):
        with open(self.filename, 'w') as file:
            for record in self.records:
                file.write(
                    f"Дата: {record.date}, Категория: {record.category}, Сумма: {record.amount}, Описание: {record.description}\n")
        print("Данные сохранены в файл.")

    # Показ текущего баланса
    def show_balance(self):
        total_income = sum(record.amount for record in self.records if record.category == 'Доход')
        total_expense = sum(record.amount for record in self.records if record.category == 'Расход')
        total_balance = total_income - total_expense
        print(f"Текущий баланс: {total_balance}")
        print(f"Доходы: {total_income}")
        print(f"Расходы: {total_expense}")

    # Функция добавления записей
    def add_record(self):
        print("Введите данные о новой записи:")
        date = input("Дата (гггг-мм-дд): ")
        category_code = input("Выберите категорию (1 - Доход, 2 - Расход): ")
        category = 'Доход' if category_code == '1' else 'Расход'
        amount = float(input("Сумма: "))
        description = input("Описание: ")
        new_record = Record(date, category, amount, description)
        self.records.append(new_record)
        print("Запись успешно добавлена!")

    # Функция редактирования записей
    def edit_record(self):
        print("Введите номер записи, которую хотите отредактировать:")
        for i, record in enumerate(self.records):
            print(f"{i + 1}. {record.date} - {record.category} - {record.amount} - {record.description}")
        try:
            index = int(input("Номер записи: ")) - 1
            if 0 <= index < len(self.records):
                print("Выберите поле для редактирования:")
                print("1. Дата")
                print("2. Категория")
                print("3. Сумма")
                print("4. Описание")
                choice = input("Введите номер поля: ")
                if choice == '1':
                    self.records[index].date = input("Введите новую дату (гггг-мм-дд): ")
                elif choice == '2':
                    category_code = input("Выберите новую категорию (1 - Доход, 2 - Расход): ")
                    self.records[index].category = 'Доход' if category_code == '1' else 'Расход'
                elif choice == '3':
                    self.records[index].amount = float(input("Введите новую сумму: "))
                elif choice == '4':
                    self.records[index].description = input("Введите новое описание: ")
                else:
                    print("Некорректный ввод.")
            else:
                print("Некорректный номер записи.")
        except ValueError:
            print("Некорректный ввод.")

    # Функция поиска записей
    def search_records(self):
        print("Выберите критерии для поиска:")
        print("1. По категории")
        print("2. По дате")
        print("3. По сумме")
        choice = input("Введите номер критерия: ")
        if choice == '1':
            category_code = input("Выберите категорию (1 - Доход, 2 - Расход): ")
            category = 'Доход' if category_code == '1' else 'Расход'
            found_records = [record for record in self.records if record.category == category]
        elif choice == '2':
            date = input("Введите дату (гггг-мм-дд): ")
            found_records = [record for record in self.records if record.date == date]
        elif choice == '3':
            amount = float(input("Введите сумму: "))
            found_records = [record for record in self.records if record.amount == amount]
        else:
            print("Некорректный ввод.")
            return

        if found_records:
            print("Найденные записи:")
            for record in found_records:
                print(
                    f"Дата: {record.date}, Категория: {record.category}, Сумма: {record.amount}, Описание: {record.description}")
        else:
            print("Записи не найдены.")

    # Функция показа записей из файла
    def show_file_content(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                print("Содержимое файла:")
                for line in file:
                    print(line.strip())
        else:
            print("Файл не найден.")

    # Основная функция программы
    def main(self):
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
                self.show_balance()
            elif choice == "2":
                self.add_record()
            elif choice == "3":
                self.edit_record()
            elif choice == "4":
                self.search_records()
            elif choice == "5":
                self.save_records_to_file()
            elif choice == "6":
                self.show_file_content()
            elif choice == "0":
                break
            else:
                print("Неверный ввод. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    wallet = FinancialWallet("financial_records.txt")
    wallet.main()