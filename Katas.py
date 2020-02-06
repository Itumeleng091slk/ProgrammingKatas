def longest(w):
    print("The longest word in the list is: ")
    words = list(w.split(" "))
    length= []
    for i in words:
        length.append(len(i))
    maximum = max(length)
    returnlist= []
    for j in words:
        if len(j) ==maximum:
           returnlist.append(j)
           list_word = j
           print(list_word)
longest(input("enter your words: "))
