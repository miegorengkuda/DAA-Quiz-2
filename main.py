import sys
import logging

def tokenize(text):
    tokens = []
    current = ''

    for ch in text.lower():
        if ch.isalnum() or ch == "'":
            current += ch
        else:
            if current:
                tokens.append(current)
                current = ''

    if current:
        tokens.append(current)

    return tokens

DEFAULT_STOPWORDS = [
    "the", "a", "an",
    "is", "are", "was", "were",
    "and", "or", "but",
    "in", "on", "at",
    "to", "of", "for"
]

def remove_stopword(tokens, stopwords=DEFAULT_STOPWORDS):
    return [t for t in tokens if t not in stopwords]

def lemmatize():
    pass

def lcs():
    pass

def main():
    if len(sys.argv == 2):
        path1 = sys.argv[1]
        path2 = sys.argv[2]

if __name__ == '__main__':
    main()
