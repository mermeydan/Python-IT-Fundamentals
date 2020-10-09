# first solution
# def gene(x, y):  # defined by positional args
#     print(x, "belongs to Generation X")
#     print(y, "belongs to Generation Y")
 
# dict_gene = {'y' : "Marry", 'x' : "Fred"}
# gene(**dict_gene)  # we call the function by a single argument(variable)

# second_solution
def gene(x='Solomon', y='David'):  # defined by kwargs (default values assigned to x and y)
    print(x, "belongs to Generation X")
    print(y, "belongs to Generation Y")
 
dict_gene = {'y' : "Marry", 'x' : "Fred"}
gene(**dict_gene) 
