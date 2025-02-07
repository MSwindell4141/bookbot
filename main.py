# returns the total count of words in a given string
def word_count(text):
    return len(text.split())

# returns a dictionary containing each char in the text along with the number of times it occures.
def char_count(text):
    word_count_dict = {}
    for word in text:
        for char in word:
            char = char.lower()
            if char not in word_count_dict:
                word_count_dict[char] = 1
            else:
                word_count_dict[char] += 1
    return word_count_dict

# prints a report containing the total count of words and the number of times each letter occurs
def main():
    print("--- Begin report of books/frankenstein.txt ---")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(f"{word_count(file_contents)} words found in the document")
        unique_char_dict = char_count(file_contents)
        for char in unique_char_dict:
            if char.isalpha():
                print(f"The '{char}' character was found {unique_char_dict[char]} times")
    print("--- End report ---")

main()