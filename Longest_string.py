# Exercise: find the longest string
def longest(width):
    longest_word = ''
    words = list(width.split(" "))
    length= []
    for word in words:
        length.append(len(word))
    maximum = max(length)
    return_list= []
    for long in words:
        if len(long) ==maximum:
           return_list.append(long)
           list_word = long
    return longest_word

print(list_word)
test = longest("the quick brown fox ate  chickens")
print(test)
