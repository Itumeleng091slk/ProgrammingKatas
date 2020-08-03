#Exercise: check if a number is even/removed line to take an input
def even_or_odd(number):
    if(number % 2 == 0):
        return "even"
    else:
        return "odd" 

if __name__ == "__main__":
    result = even_or_odd(1) 
    print(result) 


