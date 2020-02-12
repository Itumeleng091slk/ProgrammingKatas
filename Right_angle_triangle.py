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
