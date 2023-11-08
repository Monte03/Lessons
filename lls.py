import string
import random

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    
    def change_password(self, new_password):
        if new_password != self.password:
            self.password = new_password
            print("Ваш пароль змінено")
        else:
            print("Новий пароль співпадає зі старим паролем")
  

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
        if self.user_remove in self.managed_users:
            self.managed_users.remove(user_remove)
            print("Користувача видалено")
        else:
            print("Користувача не було знайдено")
    
    def reset_users_password(self, user_reset, length=12, use_digits=True, use_spec_chars=True):
        new_password = self.gen_passwd(length, use_digits, use_spec_chars)
        user_reset.change_password(new_password)
        print("Пароль користувача {user_reset.username} було скинуто")
        
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
            random.choice(chars)
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
admin1.reset_user_password(user1)

# Вывод списка пользователей администратора
print(admin1.managed_users)