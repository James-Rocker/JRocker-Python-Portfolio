def solution(number):
    blank_list = []
    for each in range(number):
        if each % 5 == 0 or each % 3 == 0:
            blank_list.append(each)
    return sum(blank_list)


print(solution(20))
