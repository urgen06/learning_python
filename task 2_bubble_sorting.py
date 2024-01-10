arr = []
n= int(input("Enter size of the array:"))
print("Enter the elements:")  
for i in range(n):
    arr.append(int(input()))
  
def bubble(arr):
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
               temp = arr[j]
               arr[j]= arr[j+1]
               arr[j+1]=temp
bubble(arr)            
print(f"Elements after sorting: {arr}")    