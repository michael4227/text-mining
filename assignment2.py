import random
import string
import sys
from unicodedata import category
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import nltk
# nltk.download('vader_lexicon')
from thefuzz import fuzz


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='utf8')

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = string.punctuation + string.whitespace
    for line in fp:
        if line.startswith('*** END OF'):
            break

        line = line.replace('-', ' ')

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1
    return hist

def bookname(filename):
    fp = open(filename, encoding='utf8')
    for line in fp:
        if line.startswith('Title: '):
            bookname = line[7:]
            return bookname

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF'):
            break


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def most_common(hist, excluding_stopwords=True):
    """Makes a list of word-freq pairs(tuples) in descending order of frequency.

    hist: map from word to frequency
    excluding_stopwords: a boolean value. If it is True, do not include any stopwords in the list.

    returns: list of (frequency, word) pairs
    """
    t = []

    stopwords = process_file('stopwords.txt', False)

    stopwords = list(stopwords.keys())
    # print(stopwords)

    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue

        t.append((freq, word))

    t.sort(reverse=True)
    return t

def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    a: the string used by the similarity function to compare the "most frequently used words" among the three books
    """
    t = most_common(hist)
    a = ''
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)
        a += word
    return a

# def similarity(hist, num=10):
#     """Prints the most commons words in a histgram and their frequencies.

#     hist: histogram (map from word to frequency)
#     num: number of words to print
#     """
#     t = most_common(hist)
#     a = ''
#     print('The most common words are:')
#     for word in t[:num]:
#         a += word
#         print(a)
#     return a

def main():
    similarity1 = []
    for i in range(3):
        hist = process_file(f'730-{i}.txt', skip_header=True)
        print('The book name:', bookname(f'730-{i}.txt'),'  Below are the analytical information')
        print('Total number of words:', total_words(hist))
        print('Number of different words:', different_words(hist), '\r')
        print_most_common(hist,num=10)
    #     similarity1.append(similarity(hist,num=10))
    # print(similarity)
    # book0 = similarity[0]
    # book1 = similarity[1]
    # book2 = similarity[2]
    # similarity_between_01 = fuzz.ratio(book0,book1)
    # similarity_between_12 = fuzz.ratio(book2,book1)
    # similarity_between_02 = fuzz.ratio(book2,book0)
    # print(f'The similarity between book 0 and 1 is {similarity_between_01},The similarity between book 1 and 2 is {similarity_between_12},The similarity between book 0 and 2 is {similarity_between_02}')

if __name__ == '__main__':
    main()
