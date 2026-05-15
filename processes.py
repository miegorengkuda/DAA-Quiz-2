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
    'the', 'a', 'an',
    'is', 'are', 'was', 'were',
    'and', 'or', 'but',
    'in', 'on', 'at',
    'to', 'of', 'for'
]

def remove_stopword(tokens, stopwords=DEFAULT_STOPWORDS):
    return [t for t in tokens if t not in stopwords]

LEMMA_DICT = {
    'lenses': 'lens',
    'sailors': 'sailor',
    'efficiently': 'efficient',
    'stood': 'stand',
    'weighed': 'weigh',
    'weirder': 'weird',
    'colonial': 'colony',
    'colonies': 'colony',
    'stubbornness': 'stubborn'
}

def lemmatize(tokens, lemma_dict=LEMMA_DICT):
    return [lemma_dict.get(t, t) for t in tokens]

def preprocess(text):
    tokens = tokenize(text)
    tokens = remove_stopword(tokens)
    tokens = lemmatize(tokens)
    return tokens

def lcs_length(tokens1, tokens2):
    m = len(tokens1)
    n = len(tokens2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if tokens1[i - 1] == tokens2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def similarity_score(tokens1, tokens2):
    lcs = lcs_length(tokens1, tokens2)
    return (2 * lcs) / (len(tokens1) + len(tokens2))
