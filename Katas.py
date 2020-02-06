
#Excercise: Hello
def Hello():
      name = str(input())
      return name;
print("hello " + Hello())

Exercise: check if a number is even
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
print('*', end = ' ')
print()
square(2)

#square(4)
# Exercise: Draw a square
def square(name ="side"):
side = int(input("enter any number of the square : "))
print("Square")
for i in range(side):
for i in range(side):
print('*', end = ' ')
print()
square(4)


#Triangle (2)
# Exercise: Draw a right handed triangle
def triangle(name = "x"):
x = int(input("enter any number of a row: "))
for i in range(x):
for j in range(i + 1):
print('*', end = ' ')
print()
triangle(2)
 
#Triangle(4)
# Exercise: Draw a right handed triangle
def triangle(name = "x"):
x = int(input("enter any number of a row: "))
for i in range(x):
for j in range(i + 1):
print('*', end = ' ')
print()
triangle(4)

#Exercise: Draw an isosceles triangle
#Isosceles (2)
def isosceles(n):
n = 2*n - 2
for i in range(0, n):
for j in range (0, n):
print(end=" ")
n = n - 1
for j in range (0, i+1):
print("*", end=" ") 
print("\r")
n = 2
isosceles(n)

#Isosceles (4)
# Exercise: Draw an isosceles triangle
def isosceles(n):
n = 2*n - 2
for i in range(0, n):
for j in range (0, n):
print(end=" ")
n = n - 1
for j in range (0, i+1):
print("*", end=" ") 
print("\r")
n = 4
isosceles(n)


# Exercise: find the longest string
from itertools import count
def longest_word(lst, n):
cnt = count()
return sorted (lst, key = lambda w : (len(w), next(cnt)),reverse = True) [:n]
lst = ("Samantha" , "itumeleng")
n = 1
print(longest_word(lst, n))


# continuation
from itertools import count
def longest_word(lst, n):
cnt = count()
return sorted (lst, key = lambda w : (len(w), next(cnt)),reverse = True) [:n]
lst = ("Samantha" , "itumeleng","sally","carrie","margarita")
n = 3 = input("words")
print(longest_word(lst, n))

#Exercise: combine two lists/arrays
def main():
list_1 = [2,4,6,8]
list_2 = [1,3,5,7]
list_3 = list_1 +list_2
print (list_3)
main()

#Exercise: Frame some text
<<<<<<< HEAD
s=input("enter the words  : ")
def frame(words) :
    size = len(max(words, key=len))
    print('*' * (size + 4))  
    for word in words:
          print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))
frame(s.split(" "))
=======




 
 

 



   

>>>>>>> c09187b5aeabf027572cf873e823dff15a9372a4
