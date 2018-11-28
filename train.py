# load and train
import reader as reader



from keras.layers import Embedding
from keras.layers import LSTM
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical
from keras.preprocessing.text import Tokenizer
from pickle import dump
from numpy import array
in_filename = 'lines.txt'
doc = reader.load_lines(in_filename)


lines = doc.split('\n')

print(lines[0])
#print(lines)

#integer encode sequences of words
tokenizer = Tokenizer(filters='')
tokenizer.fit_on_texts(lines)
sequences = tokenizer.texts_to_sequences(lines)

#print(sequences)

# vocabulary size
vocab_size = len(tokenizer.word_index) + 1

# separate into input and output
sequences = array(sequences)

# for i in range(len(sequences)):
# 	print(len(sequences[i]))


X, y = sequences[:, :-1], sequences[:, -1]

#print(X)

y = to_categorical(y, num_classes=vocab_size)
seq_length = X.shape[1]


#define model
model = Sequential()
model.add(Embedding(vocab_size, 50, input_length=seq_length))
model.add(LSTM(100, return_sequences=True))
model.add(LSTM(100))
model.add(Dense(100, activation='relu'))
model.add(Dense(vocab_size, activation='softmax'))
print(model.summary())


# compile model
model.compile(loss='categorical_crossentropy',
              optimizer='adam', metrics=['accuracy'])
# fit model
model.fit(X, y, batch_size=128, epochs=100)
#save the model to file
model.save('model.h5')
#save the tokenizer
dump(tokenizer, open('tokenizer.pkl', 'wb'))
