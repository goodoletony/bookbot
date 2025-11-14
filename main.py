import sys
from stats import get_book_text, get_word_count, get_char_count, sort_chars
def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    path = sys.argv[1]
    text = get_book_text(path)
    # print(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(text)} total words.")
    print("-------- Character Count --------")

    for item in sort_chars(get_char_count(text)):
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item["num"]}")


if __name__=="__main__":
    main()

