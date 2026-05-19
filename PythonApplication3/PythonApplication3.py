from pathlib import Path
import json
from types import NoneType

# 练习10.11
# path = Path('favorite_number.json')
# favorite_number = input("Please enter your favorite number: ")
# content = json.dumps(favorite_number)
# path.write_text(content)
# print('-' * 50)

# favorite_number_show = path.read_text()
# number= json.loads(favorite_number_show)
# print(f"I know your favorite number! It's {number}.")

# 练习10.12
# path = Path('favoriteNumber.json')
# if path.exists():
#     favorite_number_show = path.read_text()
#     number= json.loads(favorite_number_show)
#     print(f"I know your favorite number! It's {number}.")

# else:
#     favorite_number = input("Please enter your favorite number: ")
#     content = json.dumps(favorite_number)
#     path.write_text(content)

# 练习10.13
# path = Path('remember_me.json')
# user_dict = {}
# user_dict['user_name'] = input("what is your name?  ")
# user_dict['gender'] = input("what is your gender? ")
# user_dict['height'] = input("what is your height? ")
# contents = json.dumps(user_dict)
# path.write_text(contents)

# user_info = path.read_text(encoding='utf-8')
# user_dict_show = json.loads(user_info)
# print(user_dict_show)

def get_stored_username(path):
    """如果存储了用户名，就获取它"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """提示用户输入用户名"""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    path = Path('username.json')
    username = get_stored_username(path)

    if username:
        print(f"Is your name {username}?")
        answer = input("Please enter yes or no: ")

        if answer.lower() == 'yes':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"We'll remember you now, {username}!")

    else:
         username = get_new_username(path)
         print(f"We'll remember you when you come back, {username}!")


greet_user()