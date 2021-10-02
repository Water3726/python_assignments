#[Command]: HELLO
#> hello
#[Command]: hello
#> HELLO
#[Command]: clear-bot
#<창 청소>
#[Command]: goodbye
#<프로그램 종료

import os

print('넷중에 하나 입력')
print('1.hello')
print('2.HELLO')
print('3.clear-bot')
print('4.goodbye')
while True:
    select = str(input('[Command]:'))
    if select == 'hello':
        print('HELLO')
    elif select == 'HELLO':
        print('hello')
    elif select == 'clear-bot':
        os.system('cls')
    elif select == 'goodbye':
        break

