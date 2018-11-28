import string
import nltk
import chardet
import os
import numpy as np
import urllib


#load doc into memory
def load_lines(filename):
    file = open(filename,'r')
    text = file.read()
    file.close()
    return text


#cook the doc and apart the lines
def apart_lines(doc):
    doc = doc.replace('\n',' ')
    tokens = nltk.word_tokenize(doc)
    return tokens


def ordinary_process(filename):
    source = filename
    file = open(source, 'rb')
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
        for j in range(len(temp)-1, 0, -1):
            if temp[j-1] == '+':
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
    
    return final_dataset


def save_doc(lines,filename):
    data  = '\n'.join(lines)
    file = open(filename,'w')
    file.write(data)
    file.close()