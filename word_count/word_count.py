from __future__ import print_function, division

import re

# Remove any non-words and split lines into seperate words.
# Finally, convert all words to lowercase.
def splitter(line):
    line = re.sub(r'^\W+|\W+$', '', line)
    return map(str.lower, re.split(r'\W+', line))

file_name = input('Document Name: ')

def main():
    sums = dict()
    try:
        with open(file_name, 'r') as f:
            for line in f:
                for word in splitter(line):
                    word = word.lower()
                    sums[word] = sums.get(word, 0) + 1
    except IOError:
        print('Error performing file operation.')
    else:
        w = max(sums, key=lambda k: sums[k])
        print('Word: {0}\nCount: {1}'.format(w, sums[w]))

if __name__ == '__main__':
    main()
