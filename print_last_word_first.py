#sentence = 'binnen schijnt de zon'

# split by space
def last_word_first(sentence):
    split_sentence = sentence.split(" ")
    list_reverse = split_sentence[::-1]
    voeg_omgekeerde_gesplitst_samen = ' '.join(list_reverse)
    print(voeg_omgekeerde_gesplitst_samen)

sentence = input('enter word or sentence : ')
last_word_first(sentence)