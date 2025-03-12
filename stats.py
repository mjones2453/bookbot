def get_num_words(file_contents):
    count = 0
    for i in file_contents.split():
        count += 1
    return count