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
