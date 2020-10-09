sentence = input("Enter sentence please :")
# counts_letter_freq = {}
m = {}


# for i in sentence: 
#     if i in counts_letter_freq: 
#         counts_letter_freq[i] += 1
#     else: 
#         counts_letter_freq[i] = 1
# print(counts_letter_freq)
m = {m:m+1 for m in sentence if m in m}

print(m)
