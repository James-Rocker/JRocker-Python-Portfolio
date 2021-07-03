def anagrams(word, words):
    output_list = []

    def sort_word(word_to_sort):
        return "".join(sorted(word_to_sort))

    for unsorted_list_word in words:
        if sort_word(word) == sort_word(unsorted_list_word):
            output_list.append(unsorted_list_word)
    return output_list
