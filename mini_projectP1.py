# Проект "Генератор случайных историй"
import random

# Категорії: місця, персонажі, дії, події, висновок.
places = ["парку", "ресторані", "бібліотеці", "школі", "магазині", "готелі"]
persons = ["Джон", "Мері", "професор Сміт", "королева", "поліцейський", "митець"]
actions = ["вбиває", "цілує", "шукає", "думає", "подорожує", "зустрічається"]
events = ["весілля", "бойової подія", "фільму", "відкриття", "фестивалю", "свята"]
conclusions = ["одружуються", "знаходять скарб", "закохуються", "вирішують загадку", "встановлюють мир", "відмовляються один від одного"]

# Шаблон історії 
history_template = "У {place} {persons} {actions} під час {events}. На кінець історії вони {conclusions}."

while True:
    exit_input = input("Щоб вийти введіть exit, або натисніть Enter для генерації історії: ")
    if exit_input.lower() == 'exit':
        break
    
    # Випадкові слова з категорій
    rnd_place = random.choice(places)
    rnd_persons = random.choice(persons)
    rnd_actions = random.choice(actions)
    rnd_events = random.choice(events)
    rnd_conclusions = random.choice(conclusions)

    # Створення історії
    history = history_template.format(place=rnd_place, persons=rnd_persons, actions=rnd_actions, events=rnd_events, conclusions=rnd_conclusions)

    print(history)