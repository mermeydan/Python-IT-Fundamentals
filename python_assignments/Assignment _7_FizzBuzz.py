# =====>> The first solution method
# def fizzbuzz(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return 'FizzBuzz'
#     elif n % 3 == 0:
#         return 'Fizz'
#     elif n % 5 == 0:
#         return 'Buzz'
#     else:
#         return str(n)
# print("\n".join(fizzbuzz(n) for n in range(1, 101)))

# =======>> The second solution method

print("\n".join(["Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i) for i in range(1,101)]))
