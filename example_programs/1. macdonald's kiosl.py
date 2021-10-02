import os

ham_list = ['Big Mac', 'Triple Cheese Burger']
ham_price = [4600, 5600]

dri_list = ['Coke', 'Sprite', 'Water']
dri_price = [1500, 1500, 1000]

def main():
    print('\t\tWelcome to Mcdonald\'s')
    print('\t\tPlease choose menus.\n')

    print('\t1. Hamburger')
    print('\t2. Drink')
    print('\t3. Exit')

    select = int(input('\t> '))
    os.system('cls')
    return select

def ham_scr():
    for i in range(len(ham_list)):
        print(f'{i+1}. {ham_list[i]}, {str(ham_price[i])}')
    
    select = int(input('> '))

    if select == 1:
        total_ham.append(ham_list[0])
        total_ham_price.append(ham_price[0])
    elif select ==  2:
        total_ham.append(ham_list[1])
        total_ham_price.append(ham_price[1])

    os.system('cls')
    return select

def dri_scr():
    for i in range(len(dri_list)):
        print(f'{i+1}. {dri_list[i]}, {str(dri_price[i])}')   

    select = int(input('> '))

    if select == 1:
        total_dri.append(dri_list[0])
        total_dri_price.append(dri_price[0])
    elif select ==  2:
        total_dri.append(dri_list[1])
        total_dri_price.append(dri_price[1])
    elif select == 3:
        total_dri.append(dri_list[2])
        total_dri_price.append(dri_price[2])

    os.system('cls')
    return select

if __name__ == '__main__':
    total_ham = []
    total_ham_price = []

    total_dri = []
    total_dri_price = []

    while True:
        a = main()
        if a == 1:
            ham_scr()
        elif a == 2:
            dri_scr()
        elif a == 3:
            print('선택하신 햄버거는 ',end='')
            for i in range(len(total_ham)):
                print(f' {total_ham[i]} ', end='')
            print('이며 음료는 ', end='')
            for i in range(len(total_dri)):
                print(f' {total_dri[i]}', end='')
            print(f'입니다. 총 결제 금액: {sum(total_ham_price)+sum(total_dri_price)}')
            break