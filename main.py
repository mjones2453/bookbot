from stats import get_num_words, get_num_char

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents.lower()

# def sort_on(get_num_char):
#     return letter_dict["key"]

# def sort(sort_on):
#     for key in letter_dict:
#         letter_dict.sort(reverse=True, key=sort_on)
#     print (letter_dict)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    letter_dict = get_num_char(book_text)
    print("============ BOOKBOT ============")
    print("Analying book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print (f"{num_words} words found in the document")
    print("--------- Character Count ---------")
    print(f"{letter_dict}")

main()
