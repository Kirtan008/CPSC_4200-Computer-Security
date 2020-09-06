from collections import Counter
from operator import itemgetter


"""
This function removes all non alphabetic
characters excluding space from a given string
"""
def remover(input_string):
    alphabets = list("qwertyuiopasdfghjklzxcvbnm ")
    for item in input_string:
        if item not in alphabets:
            input_string = input_string.replace(item, '')
    return input_string


"""
This function takes in a string and removes all
non alphabetic chars and splits the string into
list of words
"""
def getCleanWords(original_string):
    splitBySpace = original_string.split()
    cleanedWords = list()
    for aWord in splitBySpace:
        cleanedWord = remover(aWord)
        cleanedWords.append(cleanedWord)
    return cleanedWords


"""
This function takes in a dict and converts it into
a list in decreasing order of its values
"""
def get_sorted_alphaFreq_list(ngram_dict):
    sorted_alpha_dictionary = dict()
    for key, value in sorted(ngram_dict.items()):
        if key not in sorted_alpha_dictionary:
            sorted_alpha_dictionary[key] = value

    sorted_alphaFreq_list = sorted(sorted_alpha_dictionary.items(), key=itemgetter(1), reverse=True)
    return sorted_alphaFreq_list


"""
This function counts frequencies of monograms
from list of words
"""
def countFrequency(words):
    counterDictionary = dict()
    for word in words:
        for aCharacter in word:
            if aCharacter not in counterDictionary:
                counterDictionary[aCharacter] = 1
            else:
                counterDictionary[aCharacter] += 1

    sorted_alphaFreq_list = get_sorted_alphaFreq_list(counterDictionary)

    return sorted_alphaFreq_list


"""
This function counts frequencies of bigrams
and trigrams from list of words
"""
def get_ngram_list(words, n):
    ngram = dict()
    for word in words:
        n_word_dict = Counter(word[idx:idx + n] for idx in range(len(word) - (n - 1)))
        for n_char, frequency in n_word_dict.items():
            if n_char not in ngram:
                ngram[n_char] = frequency
            else:
                ngram[n_char] += frequency

    return get_sorted_alphaFreq_list(ngram)


"""
This function prints top 30 monograms, bigrams,
and trigrams in decending order from list of ngrams
"""
def print_ngram(ngram_list):
    if len(ngram_list) >= 30:
        for idx in range(30):
            print(ngram_list[idx][0], ngram_list[idx][1])
    else:
        for idx in range(len(ngram_list)):
            print(ngram_list[idx][0], ngram_list[idx][1])


"""
This function switches all cipher letters in list of
words to its allocated key from cipher_map
"""
def decode(word_lists):
    clean_word_str = ' '.join(word_lists)
    chiper_map = {'b': 'i', 'j': 't', 'm': 'a', 'n': 'd', 'p': 'h', 't': 'n', 'w': 'g', 'x': 'e', 'r': 's', 'l': 'm',
                  'a': 'c', 'y': 'w', 'c': 'o', 's': 'j', 'v': 'r', 'i': 'f', 'd': 'v', 'e': 'y', 'h': 'k', 'g': 'l',
                  'q': 'p'}
    decoded_string = ''.join(idx if idx not in chiper_map else chiper_map[idx] for idx in clean_word_str)
    return decoded_string


if __name__ == "__main__":

    with open('encrypted.txt', 'r') as file:
        input_string = file.read().replace('\n', '') #converts text from the file into a single string
    input_string = str.lower(input_string)
    
    clean_words = getCleanWords(input_string)

    for n in range(1, 4):
        if n == 1:
            print("\nMonograms: ")
        if n == 2:
            print("\nBigrams: ")
        if n == 3:
            print("\nTrigrams: ")
        ngram = get_ngram_list(clean_words, n)
        print_ngram(ngram)

print("\nDecoded message: \n" + decode(clean_words))
