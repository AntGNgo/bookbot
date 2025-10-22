from stats import count_words
from stats import count_chars
from stats import sort_chars
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(f_path):
    with open(f_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    book = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    text_count = count_words(book)
    print(f"Found {text_count} total words")
    print("--------- Character Count -------")
    sort_chars(book)


main()
