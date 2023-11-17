# Проект "Организатор личных финансов"

import json

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
    "date": None
}

file_path = 'financial_dataP2.json'

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

# додавання транзакції
def add_transaction():
    print("Введіть наступні дані")
    amount = float(input("Сумма: "))
    
    print("Доступні категорії: ", ", ".join(transaction_template["category"].keys()))
    category = input("Категорія: ")
    date = input("Дата: ")
    transaction = {'amount': amount, 'category': category, 'date': date}
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

# аналіз транзакцій 
def analyze_transaction():
    income = 0
    total_expense = 0
    expense_categories = {}

    for transaction in financial_data:
        amount = transaction['amount']
        category = transaction['category']

        if amount > 0:
            income += amount
        elif amount < 0:
            total_expense += amount
            expense_categories[category] = expense_categories.get(category, 0) + amount

    print(f"Загальний дохід: {income}")
    print(f"Загальні витрати: {total_expense}")

    if not expense_categories:
        print("Список даних порожній.")
    else:
        print("\nВитрати по категоріям:")
        for category, expense in expense_categories.items():
            print(f"{category}: {expense}")

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

# 
def reports_transaction():
    total_income = sum(transaction['amount'] for transaction in financial_data if transaction['amount'] > 0)
    total_expense = sum(transaction['amount'] for transaction in financial_data if transaction['amount'] < 0)
    
    print(f"Загальний дохід: {total_income}")
    print(f"Загальні витрати: {total_expense}")

load_data()

while True:
    print("""
1. Додати транзакцію
2. Переглянути транзакції
3. Видалити транзакцію
4. Загальний звіт
5. Аналіз транзакцій
6. Зберегти та вийти
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
        reports_transaction()
    elif choice == 5:
        analyze_transaction()
    elif choice == 6:
        save_data()
        print("Збережено! Программа завершена.")
        break
    else:
        print("Виникла помилка.")