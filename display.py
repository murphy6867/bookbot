import collections

def display_result(path, num_words, dict_word):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    od = collections.OrderedDict(sorted(dict_word.items()))

    for key in od:
        print(f"{key}: {dict_word[key]}") 