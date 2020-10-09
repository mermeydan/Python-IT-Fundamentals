
def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return temp

        print("{0} is not a valid number".format(temp))
