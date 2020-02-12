
#Excercise: Hello/removed line that takes an input
 def Hello(person_name):
     greet = "Hello" + " " + person_name + "!"
     return greet

result = Hello ("Tshepo")
print(result)

#Exercise: check if a number is even/removed line to take an input
def even_or_odd(number):#
    if (number % 2) == 0:
        print( "{0} is even" .format(number))
    else:
        print("{0} is odd" .format(number))
even_or_odd(2)
 
# Exercise: Draw a square/removed a line to take an input
def square(side):
    for row in range(side):
        print('#'* side)
square(2)

#square(4)
# Exercise: Draw a square/ removed a line to take an input
def square(number_rows):
    for row in range(number_rows):
        print('#'* number_rows)
square(4)

#Triangle (2)
# Exercise: Draw a right handed triangle/removed line that takes an input
def triangle(number_rows):
    for row_count in range(abs(number_rows) + 1):
        print("#" * row_count)
triangle(2)

# Exercise: Draw a right handed triangle
ddef triangle(num_rows):
    for row_count in range(abs(num_rows) + 1):
        print("#" * row_count)
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
        
          ef triangle(name = "x"):
38
    x = int(input("enter any number of a row: "))
39
    for i in range(x):
40
        for j in range(i + 1):
41
            print('#', end = ' ')
42
        print()
43
triangle(4)      
num = 2
isosceles(num)


#Isosceles (4)
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


#Exercise: combine two lists/arrays
def combine():
      list1 = []
      list2 = []
    
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





 
 

 



   




