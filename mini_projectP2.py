# Проект "Организатор личных финансов"

import os
import json
from datetime import datetime

# зберігання даних та шаблон транзакцій
financial_data = []
transaction_template = {
    "amount": None,
    "category": {
        "Заробітня плата": None,
        "Комунальні послуги": None,
        "Транспорт": None,
        "Їжа": None,
        "Здоровʼя": None,
        "Розваги": None
    },
    "date": None,
    "month": None
}

available_categories = transaction_template["category"].keys()

file_name = 'mini_projectP2/financial_dataP2.json'
file_path = os.path.join(os.getcwd(), file_name)

# зберігання даних у файл json 
def save_data():
    with open(file_path, 'w') as json_file:
        json.dump(financial_data, json_file)

# завантаження даних з файлу json
def load_data():
    global financial_data
    try:
        with open(file_path, 'r') as json_file:
            financial_data = json.load(json_file)
    except FileNotFoundError:
        financial_data = []

# перевірка правильності дати
def check_date_format(date_string, format='%d.%m.%Y'):
    try:
        datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False

# додавання транзакції
def add_transaction():
    print("Введіть наступні дані")

    while True:
        try:
            amount = float(input("Сума:"))
            break
        except ValueError:
            print("Будь ласка, введіть число.")
            continue
    
    print("Доступні категорії: ", ", ".join(available_categories))
    
    while True:
        category = input("Категорія: ")
        if category in available_categories:
            break
        else:
            print("Некоректна категорія. Спробуйте ще раз.")
    
    while True:
        date = input("Дата (формат дд.мм.рррр): ")
        if check_date_format(date):
            break
        else:
            print("Некоректний формат дати. Спробуйте ще раз.")

    month = date[3:10]
    transaction = {'amount': amount, 'category': category, 'date': date, 'month': month}
    financial_data.append(transaction)
    print("Транзакція успішно додана!")

# перегляд транзакцій
def view_transaction():
    num=0
    if not financial_data:
        print("Список транзакцій порожній.")
    else:
        for transaction in financial_data:
            num+=1
            print(f"{num}. Сума: {transaction['amount']}, категорія: {transaction['category']}, дата: {transaction['date']}")

# перегляд витрат за певний місяць
def view_expenses_month():
    view_month = input("Який місяць ви хочете переглянути (формат мм.рррр): ")
    expenses_month = [i for i in financial_data if i['month'] == view_month]
    
    if not expenses_month:
        print(f"Не має витрат за місяць {view_month}.")
    else:
        print(f"Витрати за місяць {view_month}")
        for i, expenses in enumerate(expenses_month, 1):
            print(f"{i}. Сума: {expenses['amount']}, категорія: {expenses['category']}, дата: {expenses['date']}")

# витрати і заробіток в категоріях та загально
def expenses_income():
    income = 0
    total_expense = 0
    expense_categories = {}

    for transaction in financial_data:
        amount = transaction['amount']
        category = transaction['category']

        if amount > 0:
            income += amount
        
        if amount < 0:
            total_expense += amount
            expense_categories[category] = expense_categories.get(category, 0) + amount

    print(f"Загальний дохід: {income}")
    print(f"Загальні витрати: {total_expense}\n")
    
    if total_expense != 0:
        print("\nВитрати по категоріям:")
        for category, expense in expense_categories.items():
            print(f"{category}: {expense}")

# аналіз транзакцій
def analyze_transaction():
    while True:
        try:
            choice = int(input("""
1. Загальні фінанси
2. Витрати за місяць
3. Назад
Оберіть дію: """))
        except ValueError:
            print("Будь ласка, введіть число.")
            continue
        
        if choice == 1:
            expenses_income()
        elif choice == 2:
            view_expenses_month()
        elif choice == 3:
            return
        else:
            print("Виникла помилка.")

# видалення транзакцій
def remove_transaction():
    if not financial_data:
        print("Список транзакцій порожній.")
        return
    
    view_transaction()
    
    try:
        index = int(input("Оберіть номер транзакції: "))
        if 1 <= index <= len(financial_data):
            financial_data.pop(index-1)
            print("Транзакція була успішно видалена.")
        else:
            print("Невірно вказаний номер транзакції.")
    except ValueError:
        print("Було введене не число.")

load_data()

while True:
    print("""
1. Додати транзакцію
2. Переглянути транзакції
3. Видалити транзакцію
4. Аналіз транзакцій
5. Зберегти та вийти
""")
    
    try:
        choice = int(input("Оберіть функцію:"))
    except ValueError:
        print("Будь ласка, введіть число.")
        continue
    
    if choice == 1:
        add_transaction()
    elif choice == 2:
        view_transaction()
    elif choice == 3:
        remove_transaction()
    elif choice == 4:
        analyze_transaction()
    elif choice == 5:
        save_data()
        print("Збережено! Программа завершена.")
        break
    else:
        print("Виникла помилка.")