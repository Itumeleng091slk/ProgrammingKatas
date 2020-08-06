# Exercise: find the longest string
def longest_word(string=[]):
    longest_words = string
    length= []
    for word in longest_words:
        length.append(len(word))
    maximum = max(length)
    return_list = []
    for words in longest_words:
        if len(words) == maximum:
           return_list.append(words)
    print("\n".join(return_list))
    
if __name__ == "__main__":
    longest_word(["the", "quick", "brown", "fox", "ate", "my", "chickens"])
    longest_word(["once","upon","a","time"])
