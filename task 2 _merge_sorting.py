a = []
n = int(input("Enter size of the array:"))

print("Enter the elements:")
for i in range(n):
    a.append(int(input()))

def merge(a, low, mid, high):
    i = low
    j = mid + 1
    k = low
    b = [0] * len(a)

    while i <= mid and j <= high:
        if a[i] < a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
        k += 1

    while i <= mid:
        b[k] = a[i]
        i += 1
        k += 1

    while j <= high:
        b[k] = a[j]
        j += 1
        k += 1

    for i in range(low, high + 1):
        a[i] = b[i]

def merge_sort(a, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(a, low, mid)
        merge_sort(a, mid + 1, high)
        merge(a, low, mid, high)

low = 0
high = n - 1
merge_sort(a, low, high)
print(f"Sorted array: {a}")
