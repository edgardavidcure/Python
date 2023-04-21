my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]
even = []
not_even = []
outlier = []
for i in my_list:
    if i > 90:
        outlier.append(i)    
    elif i%2 == 0:
        even.append(i)
    else:
        not_even.append(i)
print('Even numbers', even)
print('Odd numbers', not_even)
print('outliers', outlier)
