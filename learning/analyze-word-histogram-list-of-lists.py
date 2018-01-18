#histogram = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]

sentence = 'mamma mashed my mashed potatoes'

#list of lists
def list_list(sentence):
    arr_sentence = sentence.split()
    histogram = []

    for word in arr_sentence:
        if len(histogram) == 0:
            histogram.append([word, 1])
        else:
            isFound = False
            for i in range(0,len(histogram) - 1):
                histo_entry = histogram[i]
                if histo_entry[0] == word:
                    histo_entry[1] += 1
                    isFound = True
            if isFound == False:
                histogram.append([word, 1])
    return histogram

print(list_list(sentence))
