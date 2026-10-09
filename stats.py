def get_book_text(file: str) -> str:
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def get_book_word_count(file: str) -> int:
    file_contents = get_book_text(file)
    words = file_contents.split()
    num_words = len(words)
    return num_words