#Exercise: Frame some text
def Frame(words) : 
    s = "write code everyday"
    size = len(max(words, key=len))
    print('*' * (size + 4))  
    for word in words:
          print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))

print(Frame(s.spilt(" "))
