#Exercise: Draw an isosceles triangle
def isosceles(number_row):
    isosceles_row = 1
    for count_row in range(1,number_row + 1):
        print(f' ' * (number_row - count_row) + '#' * isosceles_row)
        isosceles_row += 2

if __name__ == "__main__":
    isosceles(2)
    isosceles(4)
