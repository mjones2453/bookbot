from stats import get_num_words, get_num_char
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents.lower()

def sort_on(item):
    return item["count"]

def sort(letter_dict):
    # Convert the dictionary to a list of dictionaries
    letter_list = [{"char": char, "count": count} for char, count in letter_dict.items()]
    letter_list.sort(reverse=True, key=sort_on) # Sort in descending order
    return letter_list

def main():
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    letter_dict = get_num_char(book_text)
    sorted_letters = sort(letter_dict)
    print("============ BOOKBOT ============")
    print(f"Analying book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print (f" Found {num_words} total words")
    print("--------- Character Count ---------")
    for entry in sorted_letters:
        print(f"{entry["char"]}: {entry["count"]}")
    print("============= END ===============")

main()
