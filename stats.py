def get_words_num(text):
    return len(text.split())


def sort_on(items):
    return items["num"]


def sort_chars(chars_dict):
    sorted_chars = []
    for key in chars_dict:
        if key.isalpha():
            sorted_chars.append({"char": key, "num": chars_dict[key]})

    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars


def count_chars(text):
    chars_dict = {}

    for char in text:
        char = char.lower()
        if char not in chars_dict.keys():
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1

    return chars_dict


def output_chars(chars):
    for char in chars:
        print(f"{char['char']}: {char['num']}")
