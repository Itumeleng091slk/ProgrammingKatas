
#Excercise: Hello/removed line that takes an input
 def Hello(person_name):
     greet = "Hello" + " " + person_name + "!"
     return greet

result = Hello ("Tshepo")
print(result)

#Exercise: check if a number is even/removed line to take an input
def even_or_odd(number):
    even_result = "{0} is even" .format(number)
    odd_result = "{0} is odd" .format(number)
    if (number % 2) == 0:
        return even_result  
    else:
        return odd_result        
look = even_or_odd(2) # Look function to check/look whether the given integer is even or odd
print(look)
      
# Exercise: Draw a square/removed a line to take an input
def square(number_rows):
    square_form = ''
    
    for row in range(number_rows):
        for coloumn in range(number_rows):
            print('#',  end="")
        print()
    return square_form
test1 = square(2)
test2 = square(4)
print(test1)
print(test2)

#Triangle (2)
# Exercise: Draw a right angle triangle/removed line that takes an input
def triangle(number_rows):
    triangle_size = ''
    for row_count in range(abs(number_rows) + 1):
        print("#" * row_count)
    return triangle_size
test1 = triangle(2)
print(test1)

# Exercise: Draw a right handed triangle
def triangle(number_rows):
    triangle_size = ''
    for row_count in range(abs(number_rows) + 1):
        print("#" * row_count)
    return triangle_size
test1 = triangle(4)
print(test1)
 
#Exercise: Draw an isosceles triangle
#Isosceles (2)
def isosceles(number_row):
    isosceles_row = ''
    number_row = 2*number_row - 2
    
    for count_row in range(0,number_row):
        for column in range (0, number_row):
            print(end=" ")
        number_row = number_row -1
        for column in range(0, count_row+1):    
            print("#", end=" ") 
        print("\r")
    return isosceles_row 

test1 = isosceles(2)

print(test1)

#Isosceles (4)
 def isosceles(number_row):
    isosceles_row = ''
    number_row = 2*number_row - 2
    
    for count_row in range(0,number_row):
        for column in range (0, number_row):
            print(end=" ")
        number_row = number_row -1
        for column in range(0, count_row+1):    
            print("#", end=" ") 
        print("\r")
    return isosceles_row 

test1 = isosceles(4)

print(test1)

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

#Exercise: combine two lists/arrays
def combine(list_1, list_2):
    len1 = len(list_1)
    len2 = len(list_2)
    join = []
    
    if len1 > len2:
        for list in range(len2):
            join.append(list_1[list])
            join.append(list_2[list])
        # Now add remaining elements from list1
        for remaining_index in range(list,len1):
            join.append(list_1[remaining_index])
    elif len1 < len2:
        list = 0
        for list in range(len1):
            join.append(list_1[list])
            join.append(list_2[list])
        for remaining_index in range(list,len2):
            join.append(list_2[remaining_index])
    else:
        if len1 == len2:
            for list in range(len1):
                join.append(list_1[list])
                join.append(list_2[list])
    return join
test1 = combine([1,2,3],[11,22,33])
print(test1)


#Exercise: Frame some text
def frame(words) : 
    size = len(max(words, key=len))
    print('*' * (size + 4))  
    for word in words:
          print('* {a:<{b}} *'.format(a=word, b=size))
    print('*' * (size + 4))
s=input("enter the words  : ")
frame(s.split(" "))





 
 

 



   




