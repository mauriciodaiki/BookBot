def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)

def character_count(text: str) -> dict[str, int]:
    lowercase_text = text.lower()
    characters = {}
    for char in lowercase_text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters