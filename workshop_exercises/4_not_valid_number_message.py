'''cKullanıcıdan girdi alan ve girilen değer sayı değilse "sayı" is not valid number mesajı veren bir fonksiyon yazın'''
def get_integer(prompt):
    while True:
        tempt = input(prompt)
        if tempt.isnumeric():
            return tempt
        print("{0} is not a valid number".format(tempt))
get_integer("Please enter a number: ")
