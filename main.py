import sys

from stats import get_num_words
from display import display_result
from get_book import get_book_text

def main(path):
    result = get_book_text(path)
    num_words, result_words = get_num_words(result)
    display_result(path, num_words, result_words)


if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1]:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    try:
        main(book_path)
    except KeyError as e:
        print(e)
    