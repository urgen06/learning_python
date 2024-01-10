a = []
n = int(input("Enter size of the array:"))
print("Enter the elements:")
for i in range(n):
    a.append(int(input()))

def partition(a,low,high):
    pivot=a[low]
    i=low+1
    j=high
    while i<j:
        while a[i]<= pivot:
            i+=1
        while a[j]>pivot:
            j-=1
        if i<j:
            temp = a[i]
            a[i]=a[j]
            a[j]=temp
   
    temp= a[low] 
    a[low]= a[j]
    a[j]=temp 

    return j
    
def quick(a,low,high):
    if low<high:
        partitionIndex= partition(a,low,high)
        quick(a,low,partitionIndex-1)
        quick(a,partitionIndex+1,high)

quick(a,0,n-1)
print(f"Sorted array: {a}")



        
