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
