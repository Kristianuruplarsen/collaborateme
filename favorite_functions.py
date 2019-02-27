from math import sqrt, ceil

# (Kristian) My favorite function: 
# The sieve of eratosthenes
def sieve_of_eratosthenes(n: int) -> set:
    """ Find all prime numbers less than n.
    """
    numberline = set(range(2, n))

    for p in range(2, ceil(sqrt(n)) ):
        for num in range(2*p, n, p):
            numberline.discard(num)
            
    return numberline



from nltk import ngrams

# (Nicklas) My favorite function: 
# nltk ngrams <3
def nick_grams(text,n):
    tokenize = nltk.word_tokenize(text)
    return list(ngrams(tokenize, n))
