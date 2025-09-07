import sys
from stats import get_words_num, count_chars, sort_chars, output_chars


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    path = sys.argv[1]
    full_text = get_book_text(path)
    chars = count_chars(full_text)
    sorted_chars = sort_chars(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {get_words_num(full_text)} total words")
    print("----------- Character Count ----------")
    output_chars(sorted_chars)
    print("============ END ================")


if __name__ == "__main__":
    main()

