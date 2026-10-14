from stats import get_num_words, character_count, chars_dict_to_sorted_list

def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = character_count(text)
    sorted_list = chars_dict_to_sorted_list(characters)
    print_report(book_path, num_words, sorted_list)

def print_report(book_path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for tuple in sorted_list:
        if tuple[0].isalpha():
            print(f"{tuple[0]}: {tuple[1]}")
    print("============= END ===============")

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()
    
main()
