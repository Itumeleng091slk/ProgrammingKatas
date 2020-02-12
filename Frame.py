#Exercise: Frame some text
def frame(words) : 
    size = len(max(words, key=len))
    print('*' * (size + 4))  
    for word in words:
          print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))
s=input("enter the words  : ")
frame(s.split(" "))
