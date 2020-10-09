# Task : Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.
# The desired output is like :
#  fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

fibo = []
for i in range(-2, 8) :
    if i < 0 : fibo.append(1)
    else : fibo.append(fibo[i] + fibo[i+1])
print(fibo)