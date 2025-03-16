def get_num_words(text):
    words_split = text.split()
    words_count = len(words_split)
    words_dict = {}

    for word in words_split:
        char_list = list(word.lower())
        for char in char_list:
            if char in words_dict:
                words_dict[char] = words_dict[char] + 1
            else:
                words_dict[char] = 1

    return [words_count, words_dict]