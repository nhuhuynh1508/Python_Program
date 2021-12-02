# count numbers

def reverse_array(array, length):
    result = []
    for i in range(length):
        result.append(array[length-1-i])

    return result


# data
data = [1, 2, 3, 4, 5, 4, 7, 2, 3]
length = 9

result = reverse_array(data, length)

# print array
print("Data array: ", data)
print("Reverse array: ", result)
