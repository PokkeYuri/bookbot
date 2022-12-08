def main():
    filepath = "frankenstein.txt"
    text = get_file_contend(filepath)
    word_count = get_words_counts(text)
    words_dict = get_char_dict(text)
    print_char_dict_report(words_dict, word_count,filepath)

def get_file_contend(filepath):
    file_content = None
    try:  
        with open(filepath) as f:
            file_content =  f.read()
    except:
        raise Exception(f"file {filepath} could not read!")
    return file_content

def get_words_counts(text):
    return len(text.split())

def get_char_dict(text):
    result = {}
    for char in text.lower():
        if char.isalpha():
            if char not in result:
                result[char] = 0
            result[char] += 1
    return result

def print_char_dict_report(char_dict, word_count, filepath):
    char_list = []
    for key, value in char_dict.items():
        char_list.append([key, value])
    char_list.sort()

    print(f"--- Begin report of {filepath} ---")
    print(f"{word_count} words found in the document\n")
    for char_count in char_list:
        print(f"The '{char_count[0]}' character was found {char_count[1]} times")
    print("--- End report ---")

main()