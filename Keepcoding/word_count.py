from word_count_texts import stopWords, text

text = text.replace('’',"'").replace('”',"").replace('“',"").replace('?',"").replace('.',"").replace(',',"").replace('‘',"").replace('(',"").replace(')',"").replace('[',"").replace(']',"").replace('!',"").replace('\n'," ").replace('—'," ")

stop_words_li = stopWords.split("\n")
text_li = text.split(" ")

text_li = list(filter(lambda x: (x != ''), text_li))
text_li = list(map(lambda x: x.lower(), text_li))

no_stopwords = []
for word in text_li:
    if word not in stop_words_li:
        no_stopwords.append(word)

word_ocurrences = {}
for word in no_stopwords:
    if word not in word_ocurrences.keys():
        word_ocurrences[word] = 1
    else:
        word_ocurrences[word] += 1 

for word in dict(sorted(word_ocurrences.items(), key=lambda item: item[1])):
    print(f"Word: {word} --- Occurrences: {str(word_ocurrences[word])}")