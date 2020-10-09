my_rgb = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
def array_rgb(my_rgb):
    r_count = 0
    g_count = 0
    b_count = 0
    for i in range(len(my_rgb)):
        if my_rgb[i] == 'R':
            r = my_rgb.pop(i)
            my_rgb.insert(r_count, r)
            r_count += 1
        elif my_rgb[i] == 'G':
            g = my_rgb.pop(i)
            my_rgb.insert(r_count+g_count, g)
            g_count += 1
        else :
            my_rgb[i] == 'B'
            b = my_rgb.pop(i)
            my_rgb.insert(r_count+g_count+b_count, b)
            b_count += 1        
    return my_rgb

print(array_rgb(my_rgb))