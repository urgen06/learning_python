arr = []
n = int(input("Enter size of the array:"))
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))
def insertion(arr):
    for i in range(n):
        key=arr[i]
        j= i-1
        while j >=0 and arr[j] > key:
            arr[j+1]= arr[j]
            j=j-1

        arr[j+1]=key
insertion(arr)
print(f"Sorted array: {arr}")