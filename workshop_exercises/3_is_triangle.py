'''list1 = [[(3, 4, 5), (6, 8, 10), (3, 10, 6)]] verilen listenin elemanlarından üçgen oluşturulabilen elemanları bulun?'''

def is_triangle(a):
    if (a[0] + a[1] <= a[2]) or (a[0] + a[2] <= a[1]) or (a[1] + a[2] <= a[0]):
        return False
    else:
        return True
list1 = [(3, 4, 5), (6, 8, 10), (3, 10, 7)]
print(list(filter(is_triangle, list1)))