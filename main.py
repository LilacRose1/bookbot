import sys
from stats import num_words, num_characters, chars_dict_to_sorted_list

def get_book_text(filepath):
    with open(filepath, encoding="utf-8-sig") as book:
        return book.read()

def print_report(filepath, num_words, tuple_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for tuple in tuple_list:
        if(tuple[0].isalpha() == True):
            print(f"{tuple[0]}: {tuple[1]}")
    print("============= END ===============")


def main():

    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    print_report(sys.argv[1], num_words(text),
                 chars_dict_to_sorted_list(num_characters(text)))
 
main()
