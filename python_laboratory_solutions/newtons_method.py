x = int(input("Enter a number to calculate its square root: "))
iteration = int(input("How many iterations? "))
r = x
for i in range(iteration):
    r = (r+x/r)/2
    