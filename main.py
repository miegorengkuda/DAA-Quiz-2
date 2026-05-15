import sys
import logging

def tokenize(text):
    tokens = []
    current = ''

    for ch in text.lower():
        if ch.isalnum():
            current += ch
        else:
            if current:
                tokens.append(current)
                current = ''

    if current:
        tokens.append(current)

    return tokens

DEFAULT_STOPWORDS = [
    'the', 'a', 'an',
    'is', 'are', 'was', 'were',
    'and', 'or', 'but',
    'in', 'on', 'at',
    'to', 'of', 'for'
]

def remove_stopword(tokens, stopwords=DEFAULT_STOPWORDS):
    return [t for t in tokens if t not in stopwords]

LEMMA_DICT = {
    'jumps': 'jump',
    'sang': 'sing'
}

def lemmatize(tokens, lemma_dict=LEMMA_DICT):
    return [lemma_dict.get(t, t) for t in tokens]

def preprocess(text):
    tokens = tokenize(text)
    tokens = remove_stopword(tokens)
    tokens = lemmatize(tokens)
    return tokens

# TODO: implement LCS
def lcs():
    pass

# TODO: make result evaluation function

# TODO: handle path semantic errors
# TODO: handle file not found
def main():
    if len(sys.argv == 2):
        path1 = sys.argv[1]
        path2 = sys.argv[2]
    else:
        path1 = input('text1 path:')
        path2 = input('text2 path:')
    f1 = open(path1)
    f2 = open(path2)
    text1 = f1.read()
    text2 = f2.read()
    f1.close()
    f2.close()

if __name__ == '__main__':
    main()
