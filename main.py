from stats import get_num_words, character_count

def main() -> None:
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = character_count(text)
    print(f"Found {num_words} total words")
    print(characters)

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()
    
main()
