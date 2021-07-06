def duplicate_count(text: str):
    """
    Counts the number of duplicate letters in a word
    """
    repeat_list = []
    fixed_text = text.upper()
    for char in fixed_text:
        counts = fixed_text.count(char)
        if counts > 1:
            repeat_list.append(char)
    return len(set(repeat_list))


print(duplicate_count("ABBA"))
