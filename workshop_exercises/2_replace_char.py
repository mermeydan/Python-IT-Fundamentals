''' Verilen kelimede w2 harfini w1 ile değiştiren fonksiyon yazın? (lambda ile yazmaya çalışın)'''

def replace_char(word, w1, w2):
    new_word = map(lambda x: x if x != w2 else w1, word)
    return "".join(new_word)

print(replace_char('clırusway', "a", "ı"))

