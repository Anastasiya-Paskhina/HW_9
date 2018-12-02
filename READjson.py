import json


def read_j():
    with open('newsafr.json', encoding='utf-8') as f:
        file_j = json.load(f)
    return file_j


def word_lenght():
    list_word_lenght = str()
    for items in read_j()['rss']['channel']['items']:
        list_word_lenght += items['description']
    list_d = list_word_lenght.split()
    word_lenght = []
    for word in list_d:
        if len(word) > 6:
            word_lenght.append(word.lower())
    return word_lenght


def counter():
    word_counter = {}
    for word in word_lenght():
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    return word_counter


def top10():
    l = lambda counter: counter[1]
    list_top = sorted(counter().items(), key=l, reverse=True)
    count = 1
    top_10 = {}
    for word in list_top:
        top_10[count] = word
        count += 1
        if count == 11:
            break
    print(top_10)

if __name__ == '__main__':
    top10()