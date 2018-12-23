import sys
import re
# Handling 'missing' with 'setdefault'

# bad approach:

WORD_RE = re.compile('\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # this is ugly; coded like this to make a point
            occurences = index.get(word, [])
            occurences.append(location)
            index[word] = occurences

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word]) 

print('\n', '-' * 20, '\n')

# using setdefault
index ={}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])
