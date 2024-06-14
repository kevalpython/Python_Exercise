"""
word tree from each sentence
"""

SENTENCES = [
    "My name is Ram",
    "He is a good person",
    "You should be careful while coding",
    "He can do better",
    "The person is mysterious",
    "Jay Shree Ram",
    "It is my pen.",
]
SENTENCE_SPLIT = []
for i in SENTENCES:
    SENTENCE_SPLIT.append(i.split())
COUNT_WORD = {}
for i in SENTENCE_SPLIT:
    for word in i:
        if word in COUNT_WORD:
            COUNT_WORD[word] += 1
        else:
            COUNT_WORD[word] = 1
print(COUNT_WORD)
print(SENTENCE_SPLIT)
