import re

punc_to_look_for = ['!', '?', '.']

def find_all_punc(data):
    indexes = {}
    for punc in punc_to_look_for:
        indexes[punc] =  [match.start() for match in re.finditer('[' + punc + ']\s', data)]
    return indexes

def convert_i(data):
    return re.sub('\si([\s,\.])', ' I\g<1>', data)

def split_on_punc(data):
    pattern = re.compile('[%s]\s' % (''.join(punc_to_look_for)))
    return pattern.split(data)

def put_back_punc(new_sentences, punc_map):
    characters = list(new_sentences)
    for punc in punc_map:
        indexes = punc_map[punc]
        for i in indexes:
            characters[i] = punc
    return ''.join(characters)

def mark_sentence_case(data):
    punc_dict = find_all_punc(data)
    sentences = split_on_punc(data)
    sentences = [x.capitalize() for x in sentences]
    
    # we join with two spaces, because when we split, we took out the punc and the
    # spaces. to put the string back to the correct length, we do two spaces since one
    # will eventually end up being the punctuation mark
    new_sentences = '  '.join(sentences)
    new_sentences = put_back_punc(new_sentences, punc_dict)
    return new_sentences