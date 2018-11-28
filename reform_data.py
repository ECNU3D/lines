import reader as reader

in_filename = 'cornell_corpus/movie_lines.txt'
tokens = reader.ordinary_process(in_filename)
print(tokens[:200])
print('Total Tokens: %d'%len(tokens))
print('Unique Tokens: %d'%len(set(tokens)))

length = 50+1
sequences = list()
for i in range(length,len(tokens)):
    seq = tokens[i-length:i]
    line = ' '.join(seq)
    sequences.append(line)
    if len(sequences)>=100000:
    	break
print("Total sequence:%d" % len(sequences))

out_filename = 'lines.txt'
reader.save_doc(sequences,out_filename)





