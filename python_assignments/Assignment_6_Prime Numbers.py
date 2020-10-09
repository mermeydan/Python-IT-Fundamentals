# Task : Print the prime numbers which are between 1 to entered limit number (n).
# You can use a nested for loop.
# Collect all these numbers into a list
# The desired output for n=100 :
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
# 61, 67, 71, 73, 79, 83, 89, 97]
prime_nums=[]
for i in range(1, 101): 
    if i > 1: 
        for n in range(2, i//2 + 2): 
            if i==2:
               prime_nums.append(i) 
            if (i % n) == 0: 
                break
            else: 
                if n == i//2 + 1: 
                    prime_nums.append(i)
print(prime_nums) 
