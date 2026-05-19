# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue

#     print(current_number)

# def greet_user(userName):
#     print(f"Hello, {userName.title()}!")

# greet_user('john')

# def display_message():
#     print("This chapter introduce function.")

# display_message()

# def favorite_book(title):
#     print(f"One of my favorite books is {title.title()}.")

# favorite_book("alice in wonderland")

# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')


# def describe_pet(animal_type, pet_name):
#      print(f"\nI have a {animal_type}.")
#      print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', pet_name =  'harry')
# describe_pet('dog', 'willie')

# def describe_pet( pet_name, animal_type = 'dog'):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(pet_name = 'willie', animal_type = 'cat')
# describe_pet('willie')



# def make_shirt(t_shirt_size, t_shirt_word = "i love python"):
#     print(f"The size of t-shirt is {t_shirt_size.upper()}, and statement says {t_shirt_word.title()}.")

# make_shirt('xxl')
# make_shirt('xl')
# make_shirt('l', "i love c++")

# def describe_city(city_name, city_of_nation = 'china'):
#     print(f"{city_name.title()} is in {city_of_nation.title()}.")


# describe_city('guangzhou')
# describe_city('beijing')
# describe_city('frank')



# def get_formatted_name(first_name, last_name, middle_name = ' '):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

# def build_person(first_name, last_name, age = None):
#     person = {'first': first_name.title(), 'last': last_name.title()}
#     if age:
#         person['age'] = age

#     return person

# musician = build_person('jimi', 'hendrix', age = 27)
# print(musician)


# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name: ")
#     if f_name == 'q':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

# def greet_users(names):
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)

# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# def show_messages(document):
#     for show_message in messages:
#         print(show_message)

# messages = ['Hello world!', 'what is up', 'how are you']

# show_messages(messages)

# messages = ['Hello world!', 'what is up', 'how are you']
# sent_messages = []
# def send_messages(documents):
#     for document in documents:
#         print(document)

#     while documents:
#         sent_message = documents.pop()
#         sent_messages.append(sent_message)
    
#     print(documents)
#     print(sent_messages)

# send_messages(messages)

# def send_messages(documents):
#     for message in documents:
#         print(message)

#     while documents:
#         sent_message = documents.pop()
#         sent_messages.append(sent_message)
    
#     print(messages)
#     print(sent_messages)

# messages = ['Hello world!', 'what is up', 'how are you']
# sent_messages = []
# send_messages(messages)

# print("-------------------------------------------")

# def send_messages(documents):
#     for document in documents:
#         print(document)

#     while documents:
#         sent_message = documents.pop()
#         sent_messages.append(sent_message)
    
#     print(messages)
#     print(sent_messages)

# messages = ['Hello world!', 'what is up', 'how are you']
# sent_messages = []
# send_messages(messages[:])

# def make_pizza(*toppings):
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def make_pizza(size, *toppings):
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# def build_profile(first, last, **user_info):
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert', 'einstein', location ='princeton', field='physics')
# print(user_profile)

# def customer_sanwitch(*toppings):
#     print("\ncustomer_sanwitch is: ")
#     for topping in toppings:
#         print(f"{topping}")

# customer_sanwitch('tomoto', 'apple', 'banana')
# customer_sanwitch('cheery')

# def build_profile(first, last, **user_info):
#      user_info['first_name'] = first
#      user_info['last_name'] = last
#      return user_info

# user_profile = build_profile('chen', 'guoyi', location ='guangzhou', field='physics', height='175cm', weight='73kg')
# print(user_profile)


# def make_car(car_product, car_type, **car_info):
#     car_info['car_maker'] = car_product
#     car_info['car_type'] = car_type
#     return car_info

# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)

# def build_profile(name, age, **other):
#     other['person_name'] = name
#     other['person_age'] = age
#     return other

# user = build_profile('allen', 18, city='beijing', job='teacher')
# print(user)


# def student_info(stu_id, **score):
#     score['学号'] = stu_id
    
#     print(f"学号{stu_id} 数学{score['math']} 英语{score['english']} Python{score['python']}")

# student_info(7098, math=90, english=85, python=95)

# def info(name, gender='male', *hobbies, **other):
#     print(f"\nhere is {name}'s info: 性别{gender}, hobby is {hobbies}, 身高{other['height']} 体重{other['weight']}")
    
# info('chen', 'female', 'reading', 'running', 'swimming', height='176cm', weight='73kg')



# class Restaurant:


#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         print(f"The restaurant name is {self.restaurant_name}, and its cuisine type is {self.cuisine_type}.")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is opening.")


# restaurant = Restaurant('haidilao', 'huoguo')
# print(f"{restaurant.number_served} person had a huoguo.")

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# class Restaurant:


#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         print(f"The restaurant name is {self.restaurant_name}, and its cuisine type is {self.cuisine_type}.")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is opening.")

#     def set_number_served(self，number):
#         self.number_served = number


# restaurant = Restaurant('haidilao', 'huoguo')
# restaurant.number_served = 100
# print(restaurant.number_served)


# class Restaurant:


#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         print(f"The restaurant name is {self.restaurant_name}, and its cuisine type is {self.cuisine_type}.")

#     def open_restaurant(self):
#         print(f"{self.restaurant_name} is opening.")

#     def set_number_served(self):
#         print(f"{self.number_served} person had a huoguo.")

#     def increment_number_served(self, jishu):
#         self.number_served += jishu


# restaurant = Restaurant('haidilao', 'huoguo')
# restaurant.increment_number_served(200)
# restaurant.set_number_served()



# class User:
#     def __init__(self, first_name, last_name, height):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.height = height
#         self.login_attempts = 0

#     def describe_user(self):
#         print(f"user name is {self.first_name} {self.last_name}, and height is {self.height}.")

#     def greet_user(self):
#         print(f"Hello, {self.first_name} {self.last_name}, what is up!")

#     def increment_login_attempts(self, add_number = 1):
#         self.login_attempts += add_number

#     def reset_login_attempts(self):
#         self.login_attempts = 0


# user = User('chen', 'haitao', '175cm')
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# user.increment_login_attempts()
# print(f"递增了吗： {user.login_attempts}")

# user.reset_login_attempts()
# print(f"重置为0了吗： {user.login_attempts}")

