def string_vowel(string): 
    vowels = ('a', 'e', 'i', 'o', 'u')  
    for x in string.lower(): 
        if x in vowels: 
            string = string.replace(x, "") 
    print(string) 
   
string = input("Enter ein Satze :")
string_vowel(string)
