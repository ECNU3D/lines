import reader as reader
from numpy import array
from pickle import dump
from keras.preprocessing.text import Tokenizer
from keras.utils import to_cateforical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding
from pickle import load
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from random import randint


def generate_seq(model, tokenizer, seq_length, seed_text, n_words):
    result = list()
    in_text = seed_text
    #generate a fixed number of words
    for _ in range(n_words):
        # encode the text as integer
        encoded = tokenizer.texts_to_sequences([in_text])[0]
        # truncate sequences to a fixed length
        encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
        # predict probabilities for each word
        yhat = model.predict_classes(encoded, verbose=0)
        # map predicted word index to word
        out_word = ''
        for word, index in tokenizer.word_index.items():
            if index == yhat:
                out_word = word
                break
        # append to input
        in_text += ' ' + out_word
        result.append(out_word)
    return ' '.join(result)


#load  cleaned text sequences
in_filename = 'republic_sequence.txt'
doc = reader.ordinary_process(in_filename)
lines = doc

seq_length = len(lines[0].split())-1

#load the model
model = load_model('model.h5')

#load the tokenizer
tokenizer = load(open('tokenizer.pkl', 'rb'))

#select a seed text
seed_text = lines[randint(0, len(lines))]
print(seed_text+'\n')

#generate new text
generated = generate_seq(model, tokenizer, seq_length, seed_text, 50)
print(generated)
