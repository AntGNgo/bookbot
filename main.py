def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        word_count= len(file_content.split())
        chars = char_count(file_content)
        sorted_list = sort_list(chars)



        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        for i in range(0, len(sorted_list)):
            print(f"The '{sorted_list[i]['key']}' was found {sorted_list[i]['value']} times")
        print("--- End report ---")

def sort_list(dict):
    def sort_on(dict):
        return dict["value"]
    dict_list = []
    for key in dict:
        dict_list.append({"key": key, "value": dict[key]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def char_count(text):
    letters = {}
    for letter in text.lower():
        if not letter.isalpha():
            pass
        elif letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

main()