import os

def bulk_data():
    path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(path,'../data/data.txt')

    with open(path, 'r', encoding='utf-8') as file:
        words = [word.strip('\n') for word in file]

    return words
