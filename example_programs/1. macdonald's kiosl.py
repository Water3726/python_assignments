import os

Hamburger = ['Big Mac', 'Triple Cheese Burger']
Drink = ['Coke', 'Sprite', 'water']
Hamburger_pri = [4600, 5600]
Drink_pri = [1500, 1500, 1000]
total_menu_Ham = []
total_pri_Ham = []
total_menu_dri = []
total_pri_dri = []


def main():
    print('Welcome to Mcdonald\'s')
    print('Please choose menus.')

    print('1. Hamburger')
    print('2. Drink')
    print('3. Exit')

    select = int(input('>'))
    os.system('cls')
    return select
    
    

      

def Ham():
    for i in range(len(Hamburger)):
        print(f'{str(i+1)}. {Hamburger[i]}, {str(Hamburger_pri[i])}')

    select = int(input('>')) 

    if select == 1:
        total_menu_Ham.append('Big Mac')
        total_pri_Ham.append(4600)
    elif select == 2:
        total_menu_Ham.append('Triple Cheese Burger')
        total_pri_Ham.append(5600)

    os.system('cls')
    return select


def Dri():
    for i in range(len(Drink)):
        print(f'{str(i+1)}. {Drink[i]}, {Drink_pri[i]}')

    select = int(input('>'))
    if select == 1:
        total_menu_dri.append('Coke')
        total_pri_dri.append(1500)
    elif select == 2:
        total_menu_dri.append('Sprite')
        total_pri_dri.append(1500)
    elif select == 3:
        total_menu_dri.append('Water')
        total_pri_dri.append(1000)

    os.system('cls')
    return select


main()