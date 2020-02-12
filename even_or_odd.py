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
