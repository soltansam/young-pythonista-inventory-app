
from cgi import print_directory
import imp
from time import sleep
from data import warehouse1, warehouse2
from functions_library import *
shopping_list

# Get the user name
print('                                 ***Welcome to the global inventory system***')
sleep(1.0)
print('')

user_name = input('Please enter your name to continue: ')

# Greet the user
sleep(1.0)
print('Greetings to you,', user_name)
print('')
print('Here is a brief manual:')
sleep(1.0)
print('To list the items, press 1')
sleep(1.0)
print('To search an item, press 2')
sleep(1.0)
print('To partial search an item, press 3')
sleep(1.0)
print('To View the shopping_list, press 4')
sleep(1.0)
print('To checkout & quit the Application, press 5')
sleep(1.0)


while True:
    print('************************************')
    user_entry = input('''What do you want to do? 
    1:list items, 
    2:Search, 
    3:Partial search, 
    4:View shopping_list, 
    5:Quit & checkout > ''')
    
    if user_entry == '1':
        list_the_items()
    elif user_entry == '2':
        search_warehouse1()
    elif user_entry == '3':
        find_partial()
    elif user_entry == '4':
        view_shopping_list()
    elif user_entry == '5':
        print('*************************************')
        print('here is your list: ')
        view_shopping_list()
        print('***************   See you next time at global inventory. Goodbye!         ********')
        break