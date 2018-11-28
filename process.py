import os
import numpy as np
import urllib
import chardet
import nltk


#this process of course is a decoding according to utf-8 rules, when it tries this, it
#encounters a byte sequence which is not allowed in utf-8-encoded strings
#(namely this 0xff at position 0)



source = "cornell_corpus/movie_lines.txt"
file = open(source,'rb')
line = file.readline()
lines = []
while line:
    lines.append(line)
    line = file.readline()
#print(lines[0])
temp = lines[0]
# print(temp[0])
temp = temp.decode('utf-8')
# print(temp)
# print(temp[0])


#detect the method of coding
encoding = []
for i in range(len(lines)):
    temp = lines[i]
    result = chardet.detect(temp)
    encoding.append(result['encoding'])

differ_encoding = []


for i in range(len(encoding)):
    if encoding[i] not in differ_encoding:
        differ_encoding.append(encoding[i])

#print(differ_encoding)


#delete some illegal codings
final_lines = []
for i in range(len(lines)):
    code = chardet.detect(lines[i])
    code = code['encoding']
    if code == None:
        continue
    if code == 'ISO-8859-1':
        continue
    if code == 'Windows-1252':
        continue
    if code == 'ISO-8859-9':
        continue
    if code == 'SHIFT_JIS':
        continue
    if code == 'Windows-1254':
        continue
    final_lines.append(lines[i])

#print(final_lines)


after_clean = []
for i in range(len(final_lines)):
    temp = final_lines[i]
    temp = temp.decode('utf-8')
    after_clean.append([])
    for j in range(len(temp)-1,0,-1):
        if temp[j-1]=='+':
            break
        after_clean[i].append(temp[j-1])
print(after_clean)


        
form_word = []
final_clean_lines = []



for i in range(len(after_clean)):
    #form_word.append([])
    temp = ''
    temp = temp.join(after_clean[i])
    temp = temp[::-1]
    #print(temp)
    final_clean_lines.append(temp)
    temp = temp.split(' ')
    form_word.append(temp)


#print(final_clean_lines)



# nltk use
another_edition = []
for i in range(len(final_clean_lines)):
    text = nltk.word_tokenize(final_clean_lines[i])
    another_edition.append(text)

#print(another_edition)


final_dataset = []
for i in range(len(another_edition)):
    for word in another_edition[i]:
        final_dataset.append(word)

print(final_dataset)
filename = "lines.txt"
temp = []

length = 50+1

set_test = set(final_dataset)
print("the length of the set")
print(len(set_test))

sequences = list()

for i in range(length,len(final_dataset)):
    seq =  final_dataset[i-length:i]
    line = ' '.join(seq)
    sequences.append(line)

print('Total Sequences: %d' % len(sequences))

out_filename = 'lines_after_process.txt'






#print(another_edition)
# from nltk.stem.porter import PorterStemmer
# porter_stemmer = PorterStemmer()
# print(porter_stemmer.stem('maximum'))

# #nltk lemmatization
# from nltk.stem import WordNetLemmatizer
# wordnet_lemmatizer = WordNetLemmatizer()
# print(wordnet_lemmatizer.lemmatize('crying'))




#print(form_word)


# for i in range(len(form_word)):
#     sign = []
#     for j in range(len(form_word[i])):
#         if form_word[i][j]=='':
#             sign.append(form_word[i][j])
#     for j in range(len(sign)):
#         temp = sign[j]
#         form_word[i].remove(temp)

# print(form_word)

# pun_word = []
# for i in range(len(form_word)):
#     pun_word.append([])
#     for j in range():
        