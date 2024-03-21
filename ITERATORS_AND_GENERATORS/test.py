from itertools import permutations

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

result = permutations(my_list)
counter = 0
for i in result:
    counter += 1
print(counter)