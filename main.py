from stats import count_words, count_chars, sort_dict
import sys


def get_book_text(filepath: str) -> str:
    content = None

    with open(filepath) as f:
        content = f.read()

    return content


def print_report(filepath: str, total_words: int, sorted_list: list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    for i in range(0, len(sorted_list)):
        print(f"{sorted_list[i]['char']}: {sorted_list[i]['num']}")

    print("============= END ===============")


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(f"./{filepath}")
    num_words = count_words(text)
    num_chars = count_chars(text)
    sorted_list = sort_dict(num_chars)

    print_report(filepath, num_words, sorted_list)


if __name__ == "__main__":
    main()
