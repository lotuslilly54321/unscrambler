#
# Objective: find the unscrambled word
#
# Inputs: dictionary of valid words (need to find)
# jumbled word
#
# Output: list of possible valid words
#
from itertools import permutations


def permutation(scramble, maxlen):
    if len(scramble) > maxlen:
        l = list(permutations(range(0, maxlen)))
    else:
        l = list(permutations(range(0, len(scramble))))
    return l


def translate(scramble, maxlen):
    answers = permutation(scramble, maxlen)
    results = []
    for i in answers:
        answer = ''
        for elem in i:
            answer = answer + scramble[elem]
        results.append(answer)
    return results


with open('words.txt') as dictionary:
    words = dictionary.readlines()
    for i in range(0, len(words)):
        words[i] = words[i].strip('\n')
        words[i] = words[i].lower()


def lenright(words, scramble):
    length = len(scramble)
    possibilities = []
    for i in words:
        if len(i) == length:
            possibilities.append(i)
        else:
            pass
    return possibilities


def word(scramble, maxlen):
    possible = translate(scramble, maxlen)
    possibilities = lenright(words, scramble)
    for s in possible:
        for c in possibilities:
            if c.startswith(s) == True and len(c) == len(scramble):
                print(c)


scrambled = 'tibenalding'
word(scrambled, len(scrambled))

