# Write bubble sort function

# [1,2,3,4,5] -> bubble_sort -> [5,4,3,2,1]

def bubble_sort(items: list, optimize = False) -> list:
    items_count = 0
    for _ in items[1:]:
        i = 0
        is_sorted = False
        while i < len(items) - 1:
            num_1 = items[i]
            num_2 = items[i + 1]

            if num_1 < num_2:
                items[i] = num_2
                items[i + 1] = num_1
                is_sorted = True

            i+=1
            items_count += 1

        if not is_sorted and optimize:
            break

    print(f'Items count: {items_count}')
    return items

numbers = [2, 3, 5, 10, 2, 1, 14, 15, 12, 4, 20, 8]
numbers_o = [2, 3, 5, 10, 2, 1, 14, 15, 12, 4, 20, 8]

numbers_2 = [47, 92, 33, 74, 86, 51, 62, 90, 19, 58, 20, 64, 55, 91, 89, 66, 60, 23, 80, 7]
numbers_2_o = [47, 92, 33, 74, 86, 51, 62, 90, 19, 58, 20, 64, 55, 91, 89, 66, 60, 23, 80, 7]

numbers_3 = [39, 70, 75, 56, 98, 67, 20, 23, 47, 54, 89, 60, 42, 58, 83, 22, 77, 73, 85, 45]
numbers_3_o = [39, 70, 75, 56, 98, 67, 20, 23, 47, 54, 89, 60, 42, 58, 83, 22, 77, 73, 85, 45]

print(bubble_sort(numbers))
print(bubble_sort(numbers_o, optimize=True))

print(bubble_sort(numbers_2))
print(bubble_sort(numbers_2_o, optimize=True))

print(bubble_sort(numbers_3))
print(bubble_sort(numbers_3_o, optimize=True))



