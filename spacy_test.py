# import spacy
# from spacy_readability import Readability

# nlp = spacy.load('en')
# read = Readability(nlp)
# nlp.add_pipe(read,last=True)

# doc = nlp("I am some really difficult text to read because I use obnoxiously large words.")

# print(doc._.flesch_kincaid_grade_level)
# print(doc._.flesch_kincadi_reading_ease)
# print(doc._.dale_chall)
# print(doc._.smog)
# print(doc._.coleman_liau_index)
# print(doc._.automated_readability_index)