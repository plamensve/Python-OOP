input_string = input()
try:
    result_1, result_2 = input_string.split(',')
except:
    result_1, result_2 = input_string.split('.')

print(result_1)
print(result_2)

print(f"{result_1}{result_2}")
