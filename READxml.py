import xml.etree.ElementTree as ET


def read_xml():
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    xml_descriptions = root.findall('channel/item/description')
    return xml_descriptions

def word_lenght():
    list_word_lenght = str()
    for description in read_xml():
        list_word_lenght += description.text
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