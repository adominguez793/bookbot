def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print(" ")
    return make_formal(num_letters)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_letters(text):
    letter_counter = dict()
    lower = text.lower()
    for letter in lower:
        if letter in letter_counter:
            letter_counter[letter] += 1
        else:
            letter_counter[letter] = 1
    return letter_counter

def make_formal(num_letters):
    alphabet = []
    for letter in num_letters:
        if letter.isalpha() == True:
            alphabet.append(letter)
    for sort in alphabet:
        alphabet.sort(key=lambda sort: num_letters[sort])
    for formal in alphabet:
        print(f"The '{formal}' character was found {num_letters[formal]} times")
    print("--- End report ---")


main()
