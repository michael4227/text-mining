import urllib.request

url = 'https://www.gutenberg.org/files/730/730-0.txt'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
print(text) # for testing

# import pickle

# Save data to a file (will be part of your data fetching script)

# with open('dickens_texts.pickle','w') as f:
#     pickle.dump(charles_dickens_texts,f)


# Load data from a file (will be part of your data processing script)
# with open('dickens_texts.pickle','r') as input_file:
#     reloaded_copy_of_texts = pickle.load(input_file)

# with open('730-0.txt', 'w') as fout:
#     line1 = "How many roads must a man walk down\n"
#     fout.write(line1)

#     line2 = "Before you call him a man?\n"
#     fout.write(line2)
# fout.close()
