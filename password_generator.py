import os
import random
import string

def delate_line():
    os.system('cls')

def wlcome_massege():
    print('Welcome to password generat progarm.')
    print('Thank you for choice us. ')
    print('Please to start program.')
    print('-'*30)


settings ={
    'lower':True,
    'upper':True,
    'number':True,
    'symbol':True,
    'space':True,
    'length':8
}


def yes_or_no(option, defalt):
    while True:
        user_input = input(f'Include {option}? (Default is {defalt} (y:yes, n:no,enter:default)) ')
        if user_input in ['y','n',''] :
            if user_input =='y' or user_input =='':
                return defalt
            return False
        print('Invalid input.Please try again')


def get_password_length(settings,min_pw_length =4,max_pw_length = 30):
    while True:
        user_password = input('Enter your password length: ')
        if user_password.isdigit():
            if min_pw_length < int(user_password) < max_pw_length:
                return int(user_password)
            print(f'Please enter number between {min_pw_length} and {max_pw_length}')
            print('Please try again.')
            print('-'*30)

        else:
            print('Please enter number.Please try again')
            print('-'*30)



def get_settings_from_user():
    for option,defalt in settings.items():
        if option!='length':
            user_choice =yes_or_no(option, defalt)
            settings[option] =user_choice

        else:
            user_password =get_password_length(settings)
            settings[option] =user_password

def get_upper_case():
    return (random.choice(string.ascii_uppercase))

def get_lower_case():
    return(random.choice(string.ascii_lowercase))

def password_genrator(settings):

    choices =list(filter(lambda x:settings[x] ==True,settings))
    chosen =random.choice(choices)
    if chosen == 'upper':
        return get_upper_case()

    if chosen =='lower':
        return get_lower_case()
    if chosen =='symbol':
        return (random.choice('@ #')) 

    if chosen =='space':
        return' '

    if chosen =='number':
        return(random.choice('0123456789'))

   



def run_password(settings):
    fainlly_password = ''
    for i in range(settings['length']):
        fainlly_password+=password_genrator(settings)
    print('-'*30)
    return(fainlly_password)



def run():
    delate_line()
    wlcome_massege()
    get_settings_from_user()
    print(f'Password Genrator:{run_password(settings)}')

run()