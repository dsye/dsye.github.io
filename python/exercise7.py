words = ['color','color','colour','amok','amok','amuck','adviser','advisor','adviser','pepper']

canonical_spellings = ['color','amuck','adviser','pepper']

#compare words in some way
mappings = {"colour":"color", "amok":"amuck", "advisor":"adviser"}
words2 = []

for word in words:
    if word in mappings:
        corrected_word = mappings[word]
        words2.append(corrected_word)
    else:
        words2.append(word)
print(words2)
