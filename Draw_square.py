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
