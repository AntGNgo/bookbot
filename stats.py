def count_words(text):
    text_split = text.split()
    return len(text_split)

def count_chars(text):
    chars = {}
    for c in text:
        c_lower = c.lower()
        if c_lower in chars:
            chars[c_lower] += 1
        else:
            chars[c_lower] = 1
    return chars

def sort_chars(text):
    chars = []
    count = count_chars(text)
    for i in count:
        if i.isalpha():
            chars.append({"char": i, "num": count[i]})
    
    def sort_on(items):
        return items["num"]
    
    chars.sort(reverse=True, key=sort_on)

    for i in range(len(chars)):
        print(f"{chars[i]["char"]}: {chars[i]["num"]}")