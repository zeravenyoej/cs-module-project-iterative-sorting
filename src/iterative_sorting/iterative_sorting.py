def insertion_sort(input_list):
    # mark first item as sorted (no code needed here, conceptual)
    for i in range(1, len(input_list)):                                            # for every item starting at the second element
        current_item = input_list[i]                                               # put current item in temp variable
        look_left_index = i - 1                                                    
        while look_left_index > 0 and current_item < input_list[look_left_index]:  # if we are not at the beginning and current item is less than sorted
            input_list[look_left_index + 1] = input_list[look_left_index]          # if sorted item is bigger, 
            look_left_index -= 1
        input_list[look_left_index] = current_item
    return input_list


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        current_index = i
        smallest_index = current_index
        while current_index < len(arr):
            if arr[current_index] > arr[smallest_index]: 
                current_index = current_index + 1
            else: 
                smallest_index = current_index
                current_index = current_index + 1
        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp
    return arr


def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range (0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swapped = True
    return arr



# def bubble_sort(arr):
#     for i in range(0, len(arr) - 1):
#         current_index = i 
#         right_index = current_index + 1
#         while right_index > len(arr):
#             if arr[current_index] < arr[right_index]:
#                 current_index = right_index
#                 right_index = right_index + 1
#             else:
#                 temp = arr[current_index]
#                 arr[current_index] = arr[right_index]
#                 arr[right_index] = temp
#                 current_index = right_index
#                 right_index = right_index + 1

#     return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
