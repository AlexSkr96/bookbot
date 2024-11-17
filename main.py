def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(f"{count_words(file_contents)} word found in document")
    for char, count in count_unique_chars(file_contents).items():
        print(f"The '{char}' charachter was found {count} times")
    print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def count_unique_chars(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char.isalpha():
            char_dict[char] = char_dict[char] + 1 if char in char_dict else 1
    char_dict = dict(sorted(char_dict.items(), key=lambda entry: entry[1], reverse=True))
    return char_dict


main()
