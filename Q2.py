sentences = ["My name is Ram", "He is a good person", "You should be careful while coding", "He can do better", "The person is mysterious", "Jay Shree Ram", "It is my pen."]
sentence_split=[]
for i in sentences:
    sentence_split.append(i.split())
count_word={}
for i in sentence_split:
    for word in i:
        if word in count_word:
            count_word[word]+=1
        else:
            count_word[word]=1
print(count_word)

print(sentence_split)

