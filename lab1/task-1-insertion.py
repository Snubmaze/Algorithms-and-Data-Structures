import time
def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
            else:
                break
    return arr

start=time.time()

with open('input.txt', 'r') as file:
    n=int(file.readline())
    arr=list(map(int,file.readline().split(' ')))


if not 1<=n<=10**3:
    print("n is out of range")
    exit()

for i in arr:
    if abs(i)>10**9:
        print(f"{i} is out of range")
        exit()
        
if n!= len(arr):
    print(f"array should contain {n} elements")
    exit()
    
else:
    print(insertion_sort(arr))
    finish=time.time()
    print(f"sort finished with {(finish-start)*1000} ms")
