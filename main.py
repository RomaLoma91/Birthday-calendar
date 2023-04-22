from datetime import datetime, timedelta

def get_birthdays_per_week():
    users = [
        {"name": "Anna", "birthday": datetime(1990, 5, 12)},
        {"name": "Sofiya", "birthday": datetime(1985, 3, 21)},
        {"name": "Roman", "birthday": datetime(1995, 7, 5)},
        {"name": "Ivan", "birthday": datetime(1988, 12, 15)}
    ]

    today = datetime.now().date()  # Поточна дата
    next_week = today + timedelta(weeks=1)  # Дата через тиждень

    # Словник для зберігання користувачів, яких потрібно привітати за днем народження
    birthdays = {}

    # Ітеруємось по списку користувачів
    for user in users:
        birthday = user["birthday"].date()  # Дата народження користувача
        # Якщо день народження припадає на вихідний день (суботу або неділю),
        # то переносимо його на понеділок
        if birthday.weekday() >= 5:
            birthday += timedelta(days=7 - birthday.weekday())
        if today <= birthday < next_week:  # Перевірка, чи припадає день народження на поточний тиждень
            # Додаємо користувача до словника birthdays за днем тижня
            day_of_week = birthday.strftime("%A")  # Отримуємо назву дня тижня
            if day_of_week not in birthdays:
                birthdays[day_of_week] = []
            birthdays[day_of_week].append(user["name"])

    # Виводимо список користувачів, яких потрібно привітати за днем народження
    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
        if day in birthdays:
            # Виводимо день тижня разом з ім'ями користувачів, розділеними комою та пробілом
            print(f"{day}: {', '.join(birthdays[day])}")
    

