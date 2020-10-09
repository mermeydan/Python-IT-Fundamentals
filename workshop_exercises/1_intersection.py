'''Verilen iki listenin kesişim elemanlarını set kullanmadan bulmaya çalışın?'''

list1 = [1, 2, 3, 4, 8, 9]
list2 = [2, 3, 6, 11]

kesisim = list(filter(lambda x : x in list2, list1))
print ("Kesişim elemanları: ", kesisim)

