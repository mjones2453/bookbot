def get_num_words(file_contents):
    count = 0
    for i in file_contents.split():
        count += 1
    return count

def get_num_char(file_contents):
    count = 0
    letter_dict = {}
    for i in file_contents:
        if i in letter_dict:
            letter_dict[i] += 1
        elif i not in letter_dict:
            letter_dict[i] = 1
    return letter_dict
        