#def word_count():
    #book_path = "books/frankenstein.txt"
    #text = get_book_text(book_path)
    #words = text.split()
    #print(f"Found {len(words)} total words")

#def char_count():
    #book_path = "books/frankenstein.txt"
    #text = get_book_text(book_path)
    #chars = text.lower()
    #unique_char = {}
    #for char in chars:
        #if char not in unique_char:
            #unique_char[char] = 1
        #else: 
            #unique_char[char] += 1
    #return unique_char


#def get_book_text(path):
    #with open(path) as f:
        #return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list   
