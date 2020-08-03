# Exercise: Draw a right angle triangle/removed line that takes an input
def triangle(number_rows):
    for row_count in range(abs(number_rows) + 1):
        print("#" * row_count)

if __name__ == "__main__":
    triangle(2)
    triangle(4)
