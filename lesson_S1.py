import string
import secrets

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return f"Користувач {self.username} {self.email}"
    
    def change_password(self, old_password, new_password):
        if old_password == self.password:
            if new_password != old_password:
                self.password = new_password
                print("Ваш пароль змінено")
            else:
                print("Новий пароль співпадає зі старим паролем")
        else:
            print("Старий пароль невірний")


class Admin(User):
    def __init__(self, username, password, email):
        super().__init__(username, password, email)
        self.managed_users = []
        
    def add_user(self, new_user):
        if new_user.username not in [self.username for user in self.managed_users]:
            self.managed_users.append(new_user)
            print("Користувача додано")
        else:
            print("Користувач вже зареєстрований")
    
    def remove_users(self, user_remove):
        if user_remove in self.managed_users:
            self.managed_users.remove(user_remove)
            print("Користувача видалено")
        else:
            print("Користувача не було знайдено")
    
    def reset_users_password(self, user_reset, length=12, use_digits=True, use_spec_chars=True):
        if user_reset in self.managed_users:
            new_password = self.gen_passwd(length, use_digits, use_spec_chars)
            user_reset.change_password(user_reset.password, new_password)
            print(f"Пароль користувача {user_reset.username} було скинуто")
    
    @staticmethod
    def gen_passwd(
        length=12,
        use_digits=True,
        use_spec_chars=True
    ):
        chars = string.ascii_letters
        if use_digits:
            chars+=string.digits
        if use_spec_chars:
            chars+=string.punctuation
        
        password = ''.join(
            secrets.choice(chars)
            for _ in range(length)
        )
        return password


# Создание пользователя и администратора
user1 = User('user1', 'password123', 'user1@example.com')
admin1 = Admin('admin1', 'adminpassword', 'admin1@example.com')

# Администратор добавляет пользователя
admin1.add_user(user1)

# Пользователь пытается сменить пароль на тот же самый
user1.change_password('password123', 'password123')  # Должно выдать ошибку

# Админ сбрасывает пароль пользователя
admin1.reset_users_password(user1)

# Вывод списка пользователей администратора
lists = admin1.managed_users
for user in lists:
    print(user)
