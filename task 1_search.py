# Linear search for unsorted list
# a = int(input("Enter any number you want to search:"))
# mylist = [1,23,56,73,100,121]
# for x in mylist:
#     if a == x:
#         print("Yes, the number you searched is in my list.")
#         break
# else:
#     print("Number you searched is not found.")



#binary search for sorted list
def binary_search(arr,target):
    low =0
    high = len(arr) 
    while low <= high:
        mid = (low + high) // 2 
        mid_value = arr[mid]
        if mid_value == target:
            return mid
        if mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
mylist = [1,12,34,57,89,99,110,290,512]
target_element = int(input("Enter a number you want to search:"))
result = binary_search(sorted(mylist),target_element)
if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found.")
        