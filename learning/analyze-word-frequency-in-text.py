sentence = "one fish two fish red fish blue fish"

histogram = {}

#create array of all words
sentence = sentence.split()

#loop through sentence
for word in sentence:
    if word in histogram:
        histogram[word] += 1
    else:
        histogram[word] = 1

print(histogram)
