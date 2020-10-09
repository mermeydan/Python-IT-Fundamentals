'''Soru 4 de yazdığınız fonksiyonu is_int.py uzantılı olarak kaydedin ve daha önceden yaptığınız amstrong sayısını 
bulma ödevinde kullanmak üzere import edip kullanın.'''

from is_int import get_integer

while True:
    number = get_integer("Please enter a number to check if it's an Armstrong Number : ")

    len_num = len(number)

    list_num = list(number)

    armstrong = 0

    for i in list_num:
        armstrong += int(i) ** len_num
        
    if int(number)==armstrong:
        print("{} is an Armstrong number".format(int(number)))
        break
    else: 
        print("{} is not an Armstrong number".format(int(number)))

