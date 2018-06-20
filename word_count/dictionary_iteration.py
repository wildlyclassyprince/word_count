# Our string
word = 'ANACONDA NAVIGATOR'

# Creating the tokenized list
tokenized = list()
for i in enumerate(word):
    tokenized.append(i)

# Creating the dictionary
results = dict()
for value, letter in tokenized:
    results[value] = letter

print(results)
