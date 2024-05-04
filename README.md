# Личный финансовый кошелек

Программа "Личный финансовый кошелек" представляет собой консольное приложение, разработанное для учета личных доходов и расходов. Она предоставляет пользователю возможность следующих действий:

1. **Просмотр баланса**: Показывает текущий баланс, а также раздельно доходы и расходы.

2. **Добавление записи**: Позволяет пользователю добавлять новые записи о доходах или расходах, включая дату, категорию (доход или расход), сумму и описание.

3. **Редактирование записи**: Позволяет пользователю изменять существующие записи о доходах и расходах, включая изменение даты, категории, суммы и описания.

4. **Поиск записей**: Позволяет пользователю находить записи по заданным критериям, таким как категория, дата или сумма.

5. **Сохранение записей в файл**: Сохраняет все текущие записи о доходах и расходах в текстовый файл для последующего доступа.

6. **Показ содержимого файла**: Отображает содержимое текстового файла с записями о доходах и расходах.

Приложение разработано с использованием языка программирования Python и не требует установки дополнительных библиотек. Оно обеспечивает удобный способ для пользователей вести учет своих финансов и легко настраивается под индивидуальные нужды благодаря простому интерфейсу и разнообразным функциям.


**Документация**

def show_balance(records):
    """
    Выводит текущий баланс, доходы и расходы на основе списка записей.

    Parameters:
    records (list): Список записей о доходах и расходах.

    Returns:
    None
    """
    total_income = sum(record['amount'] for record in records if record['category'] == 'Доход')
    total_expense = sum(record['amount'] for record in records if record['category'] == 'Расход')
    total_balance = total_income - total_expense
    print(f"Текущий баланс: {total_balance}")
    print(f"Доходы: {total_income}")
    print(f"Расходы: {total_expense}")

def add_record(records):
    """
    Добавляет новую запись о доходе или расходе в список записей.

    Parameters:
    records (list): Список записей о доходах и расходах.

    Returns:
    None
    """
    print("Введите данные о новой записи:")
    date = input("Дата (гггг-мм-дд): ")
    category_code = input("Выберите категорию (1 - Доход, 2 - Расход): ")
    category = 'Доход' if category_code == '1' else 'Расход'
    amount = float(input("Сумма: "))
    description = input("Описание: ")
    records.append({'date': date, 'category': category, 'amount': amount, 'description': description})
    print("Запись успешно добавлена!")

def edit_record(records):
    """
    Редактирует существующую запись о доходе или расходе в списке записей.

    Parameters:
    records (list): Список записей о доходах и расходах.

    Returns:
    None
    """
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

def search_records(records):
    """
    Ищет записи о доходах или расходах в списке записей по заданным критериям.

    Parameters:
    records (list): Список записей о доходах и расходах.

    Returns:
    None
    """
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
