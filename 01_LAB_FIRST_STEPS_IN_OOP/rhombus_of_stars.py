def print_stars_upper(num):
    for row in range(1, num + 1):
        print(f"{' ' * (num - row)}", '* ' * row)


def print_stars_bottom(num):
    for row in range(num - 1, 0, -1):
        print(f"{' ' * (num - row)}", '* ' * row)


number = int(input())
print_stars_upper(number)
print_stars_bottom(number)

