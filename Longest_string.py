# Exercise: find the longest string
def longest(w):
    longest_word = ''
    words = list(w.split(" "))
    length= []
    for word in words:
        length.append(len(word))
    maximum = max(length)
    returnlist= []
    for long in words:
        if len(long) ==maximum:
           returnlist.append(long)
           list_word = long
           print(list_word)
    return longest_word
test = longest("the qucik brwon fox ate  chickens")
print(test)
