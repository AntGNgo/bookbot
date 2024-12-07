def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
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

main()