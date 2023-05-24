def sum_even_num(arr):
    total = 0
    for num in arr:
        if num % 2 == 0:
            total += num
    return total

def count_array(arr):
    total = 0
    for num in arr:
        total +=1
    return total

arr = [4,8,3,14,23,24]

print(sum_even_num(arr))
print(count_array(arr))
print(arr[4])