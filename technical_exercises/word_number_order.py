import re


def order(sentence):
    if len(sentence) > 0:
        number_list = re.findall(r'\d+', sentence)
        word_list = sentence.split()
        ordered_string = ' '.join([number_list for _, number_list in sorted(zip(number_list, word_list))])
        return ordered_string
    else:
        return sentence


print(order("is2 Thi1s T4est 3a"))
