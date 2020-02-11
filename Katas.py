
#Excercise: Hello
def Hello():
      name = str(input("hello"))
      return name;
print("hello " + Hello())

#Exercise: check if a number is even
def even_or_odd(name="even or odd"):
    num = int(input("enter a number: "))
    if (num % 2) == 0:
        print( "{0} is even" .format(num))
    else:
        print("{0} is odd" .format(num))
even_or_odd("even or odd")
 
#Exercise: Draw a square
#Square(2)
 
# Exercise: Draw a square
def square(name ="side"):
    side = int(input("enter any number of the square : "))
    print("Square")
    for i in range(side):
        for i in range(side):
            print('#', end = ' ')
        print()
square(2)

#square(4)
# Exercise: Draw a square
def square(name ="side"):
    side = int(input("enter any number of the square : "))
    print("Square")
    for i in range(side):
        for i in range(side):
            print('#', end = ' ')
        print()
square(4)

#Triangle (2)
# Exercise: Draw a right handed triangle
def triangle(name = "x"):
    x = int(input("enter any number of a row: "))
    for i in range(x):
        for j in range(i + 1):
            print('#', end = ' ')
        print()
triangle(2)
 
#Triangle(4)
# Exercise: Draw a right handed triangle
def triangle(name = "x"):
    x = int(input("enter any number of a row: "))
    for i in range(x):
        for j in range(i + 1):
            print('#', end = ' ')
        print()
triangle(4)

#Exercise: Draw an isosceles triangle
#Isosceles (2)
def isosceles(num):
    num = int(input("enter the number of rows:"))
    num = 2*num - 2
    for i in range(0, num):
        for j in range (0, num):
            print(end=" ")
        num = num -1
        for j in range(0, i+1):    
            print("#", end=" ") 
        print("\r")
        
                
num = 2
isosceles(num)


#Isosceles (4)
# Exercise: Drawdef frame(words) :
    
    size = len(max(words, key=len))
    print('*' * (size + 4))  
    for word in words:
          print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))
s=input("enter the words  : ")
frame(s.split(" ")) an isosceles triangle
def isosceles(num):
    num = int(input("enter the number of rows:"))
    num = 2*num - 2
    for i in range(0, num):
        for j in range (0, num):
            print(end=" ")
        num = num -1
        for j in range(0, i+1):    
            print("#", end=" ") 
        print("\r")
        
                
num = 4
isosceles(num)


# Exercise: find the longest string
def longest(w):def frame(words) :
    
    size = len(max(words, key=len))
    print('*' * (size + 4))  
    for word in words:
          print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))
s=input("enter the words  : ")
frame(s.split(" "))
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


#Exercise: combine two lists/arrays
def combine():
      list1 = []
      list2 = []
    def frame(words) :
    
    size = len(max(words, key=len))
    print('*' * (size + 4))  
    for word in words:
          print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))
s=input("enter the words  : ")
frame(s.split(" "))
      list_1 = input("enter your first set of numbers: ") .split(" ")
      list1 = list_1

      list_2 = input("enter your second set of numbers: ").split(" ")
      list2 = list_2
  
      n = len(list1)
      store_list = []
      for i in range(n):
          store_list.append(list1[i])
          store_list.append(list2[i])
      print(store_list)
      
combine()

#Exercise: Frame some text
def frame(words) : 
    size = len(max(words, key=len))
    print('*' * (size + 4))  
    for word in words:
          print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))
s=input("enter the words  : ")
frame(s.split(" "))





 
 

 



   




