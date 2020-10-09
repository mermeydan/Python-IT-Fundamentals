'''Kullanıcıdan aldığınız cümlenin palindrom olup olmadığını kontrol eden fonksiyon yazın.
(Noktalama ve özel karakterleri dikkate almayın. Sadece alphanumeric karakterler i dikkate alın.)'''

def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)

# word = input("Please enter a word to check: ")
# word = ("Ey Edip Adana'da pide ye.")
word = ("Makam")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))