def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        chars = count_chars(file_contents)
        print("--- Beign report of books/frankenstein.txt ---")
        print(f"{count_words(file_contents)} words found in the document\n")
    
        for i in chars:
            print(f"The '{i}' was found {chars[i]} times")
        print("--- End report ---")

def count_words(text):
    text_split = text.split() 
    return len(text_split)

def count_chars(text):
    text_lower = text.lower()    
    text_list = list(text_lower)

    char_dict = {}
    for char in text_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

main()