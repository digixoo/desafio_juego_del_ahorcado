
def print_underline(word, array_letters):
    return ''.join(list(map(lambda x: x if x in array_letters else '_', word)))