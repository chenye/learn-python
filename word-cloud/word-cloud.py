
def count_words(paragraph):
    d = dict()
    for word in paragraph.split():
        d[word] = d.get(word, 0) + 1
    return d

paragraph = "abc is the name of a song that starts with abc"
print count_words(paragraph)

