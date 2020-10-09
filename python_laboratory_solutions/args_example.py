# arguments first
# def brothers(bro1, bro2, bro3):
#     print('Here are the names of brothers :')
#     print(bro1, bro2, bro3, sep='\n')
# family = ['tom', 'sue', 'tim']
# brothers(*family)

# arguments second solution.
def brothers(*args):
    print('Here are the names of brothers :')
    for i in args:
        print(i)
family = ['tom', 'sue', 'tim']
brothers(family, *family)
