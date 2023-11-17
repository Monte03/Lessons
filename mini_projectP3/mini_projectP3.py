# Проект "Викторина Знаний"
import random
import time

def display_categories(questions):
    for category in questions.keys():
        print(category)

def choose_category(questions):
    display_categories(questions)
    category = input("Оберіть категорію: ")
    return category.capitalize()

def ask_question(category, questions, score):
    question = random.choice(questions[category])
    print(question['Запитання'])

    start_time = time.time()
    elapsed_time = 0

    while elapsed_time < 10:
        user_answer = input("Ваша відповідь: ")
        end_time = time.time()
        elapsed_time = end_time - start_time

        if user_answer:
            break

    if not user_answer or elapsed_time >= 10:
        print("Час вийшов! Ви програли.")
        return score

    if user_answer == question['Відповідь']:
        print("Правильно!")
        print(f"Витрачено часу: {elapsed_time:.2f} сек.")
        return score + 1
    else:
        print(f"Неправильно. Правильна відповідь: {question['Відповідь']}")
        return score

def play_quiz():
    score = 0
    questions = {
        'Історія': [
            {'Запитання': 'В якомум році відбулася Велика Жовтневська соціалістична революція?', 'Відповідь': '1917'},
        ],
        'Наука': [
            {'Запитання': 'Який хімічний елемент позначається символом "O"?', 'Відповідь': 'Кисень'},
        ],
        'Спорт': [
            {'Запитання': 'Яка команда перемогла в останньому Чемпіонаті світу з футболу?', 'Відповідь': 'Франція'},
        ],
    }

    print("Вітаю вас у грі 'Вікторина Знань'!")
    rounds = 3

    for _ in range(rounds):
        category = choose_category(questions)
        score = ask_question(category, questions, score)

    print(f"Гра скінчилася. Ваш рахунок: {score}")

if __name__ == "__main__":
    play_quiz()
