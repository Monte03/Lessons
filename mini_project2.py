# Проект "Организатор личных финансов"

financial_data = []

def add_transaction():
    print("Введіть наступні дані")
    amount = float(input("Сумма: "))
    category = input("Категорія: ")
    date = input("Дата: ")
    transaction = {'amount': amount, 'category': category, 'date': date}
    financial_data.append(transaction)
    print("Транзакція успішно додана!")

def view_transaction():
    num=0
    if not financial_data:
        print("Список транзакцій порожній.")
    else:
        for transaction in financial_data:
            num+=1
            print(f"{num}. Сума: {transaction['amount']}, категорія: {transaction['category']}, дата: {transaction['date']}")
        
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

def reports_transaction():
    total_income = sum(transaction['amount'] for transaction in financial_data if transaction['amount'] > 0)
    total_expense = sum(transaction['amount'] for transaction in financial_data if transaction['amount'] < 0)
    
    print("Звіт")
    print(f"Загальний дохід: {total_income}")
    print(f"Загальні витрати: {total_expense}")

while True:
    print("""
1. Додати транзакцію
2. Переглянути транзакції
3. Видалити транзакцію
4. Загальний звіт
5. Вийти
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
        print("Программа завершена.")
        break
    else:
        print("Виникла помилка.")