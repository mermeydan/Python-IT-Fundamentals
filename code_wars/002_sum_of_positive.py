# You get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# Note: if there is nothing to sum, the sum is default to 0.
# x=[1,-4,7,12]
# def positive_sum(array_1):
#     sum=0
#     for i in array_1:
#         if i>=0:
#             sum+=i
#         return sum
# print(positive_sum(x))

# #########################
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
# print(positive_sum(x))
################################
