def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_characters(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for x,y in char_count.items():
        letter = x
        count = y
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    lowered_string = text.lower()
    character_count = {}

    for i in lowered_string:
        if i.isalpha():
            if i in sorted(character_count):
                character_count[i] += 1
            else:
                character_count[i] = 1  
    sorted_count = dict(sorted(character_count.items()))    
    return sorted_count


main()