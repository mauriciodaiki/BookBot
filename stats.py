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

def sort_on(char: tuple[str, int]) -> int:
    return char[1]

def chars_dict_to_sorted_list(characters: dict[str, int]) -> list[tuple[str, int]]:
    chars_list = []
    for character in characters:
        chars_list.append((character, characters[character]))
    sorted_chars_list = sorted(chars_list, reverse=True, key=sort_on)
    return sorted_chars_list
        
