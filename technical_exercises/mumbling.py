def accumulate(s):
    list_of_letters = list(s.replace(" ", ""))
    output_string = ""
    for count, letter in enumerate(list_of_letters):
        output_string += letter.upper()
        if count > 0:
            output_string += count * letter.lower()
        output_string += "-"
    return output_string[:-1]


if __name__ == "__main__":
    print(accumulate("abcd"))
