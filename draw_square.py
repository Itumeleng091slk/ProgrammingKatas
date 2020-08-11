# Exercise: Draw a square/removed a line to take an input
def square(number_rows):
    for row in range(number_rows):
        for coloumn in range(number_rows):
            print('#',  end='')
        print()


if __name__ == "__main__":
    square(2)
    square(4)
  

