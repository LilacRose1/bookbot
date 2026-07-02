def num_words(book):
    words_list = book.split()
    return len(words_list)

def num_characters(book):
    char_dict = {}
    words_list = book.split()
    for words in words_list:
        for char in words:
            if char.lower() in char_dict:
                char_dict[char.lower()] += 1
            else:
                char_dict[char.lower()] = 1
    return char_dict

def sort_on(tuple):
    return tuple[1]

def chars_dict_to_sorted_list(dict):
    new_list = []

    for key in dict:
        new_list.append((key, dict[key]))

    sorted_list = sorted(new_list, reverse= True, key= sort_on)
    return sorted_list
