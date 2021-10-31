# import urllib.request
# import certifi
# import ssl

# # pip3 install certifi
# # /Applications/Python\ 3.6/Install\ Certificates.command
# https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error

# url = 'https://www.gutenberg.org/files/730/730-0.txt'
# response = urllib.request.urlopen(url,context=ssl.create_default_context(cafile=certifi.where()))
# data = response.read()  # a `bytes` object
# text = data.decode('utf-8')
# print(text) # for testing



# import pickle

# Save data to a file (will be part of your data fetching script)

# with open('dickens_texts.pickle','w') as f:
#     pickle.dump(charles_dickens_texts,f)


# Load data from a file (will be part of your data processing script)
# with open('dickens_texts.pickle','r') as input_file:
#     reloaded_copy_of_texts = pickle.load(input_file)
# -----------------------
# I changed the code based on my in analyze_book, and the analyze_book solution, and the text I analyzed for this assignment is Oliver Twist by Charles Dickens
import random
import string
import sys
from unicodedata import category

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
        if line.startswith('*** END OF THE PROJECT'):
            break

        line = line.replace('-', ' ')

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THE PROJECT'):
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

    stopwords = process_file('text-mining/stopwords.txt', False)

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
    """
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return res


# def random_word(hist):
#     """Chooses a random word from a histogram.

#     The probability of each word is proportional to its frequency.
#     """
#     t = []
#     for word, freq in hist.items():
#         t.extend([word] * freq)

#     return random.choice(t)


def main():
    hist = process_file(f'text-mining/730-0.txt', skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist, excluding_stopwords=True)
    print('The most common words are:')
    for word,freq in t[0:20]:
            print(word, '\t', freq)

    words = process_file('data/words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff.keys():
            print(word, end=' ')

    # print("\n\nHere are some random words from the book")
    # for i in range(100):
    #     print(random_word(hist), end=' ')


if __name__ == '__main__':
    main()
