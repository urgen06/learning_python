arr=[]
n = int(input("Enter size of the array:"))
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

def selection(arr):
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                temp = arr[j]
                arr[j]=arr[min]
                arr[min]=temp

selection(arr)
print(f"Sorted array: {arr}")