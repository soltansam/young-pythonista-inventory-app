
from email.message import EmailMessage
from traceback import print_list
from data import *
from time  import sleep

shopping_list = []


def find_partial():
    wanted = input('enter a partial search: > ')
    result = list(filter(lambda x: wanted in x, warehouse1))
    print(result)

def search_warehouse1():
    s = input('Please enter an item:\n')
    if s in warehouse1:
        print(f'{s} is present in the list')
        print('and its index is: ', warehouse1.index(s))
        buying_decision = str.lower(input('Would you like to add to ur shopping list?: Y/n)'))
        if buying_decision == 'y':
            shopping_list.append(s)
        
            
    else:
        print(f'{s} is not present in the list')



# This method list the items in warehouse1
def list_the_items():
    # Show the menu and ask to pick a choice
    print('Here is the list of our available inventory: ')
    print('')
    print('************************************************')

    for a,b,c in zip(warehouse1[::3],warehouse1[1::3],warehouse1[2::3]):
        print ('{:<30}{:<30}{:<}'.format(a,b,c))
        sleep(0.1)

def view_shopping_list():
    if len(shopping_list) == 0:
            print('Nothing in your shopping list yet!')
    for i in shopping_list:
        print(i)
        