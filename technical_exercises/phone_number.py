def create_phone_number(n):
    first_three = '(' + str(''.join(map(str, n[0:3]))) + ')'
    mid_three = str(''.join(map(str, n[3:6])))
    last_four = str(''.join(map(str, n[6:10])))
    return f'{first_three} {mid_three}-{last_four}'


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
