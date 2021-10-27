
def is_valid(word, input):
    return True if input in word else False

def win(word, user_letters):
    new_word = ''.join(list(map(lambda x: x if x in user_letters else '', word)))   

    return True if new_word == word else False

def lose(lyfe):
    return True if lyfe <= 0 else False