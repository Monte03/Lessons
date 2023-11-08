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
        
    def add_users(self, new_user):
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
    
    def reset_users_password(self, user_reset):
        new_password = ''.join