def binary_search(A,V):
    result=[i for i in range(0,len(A)) if A[i]==V]
    counter=len(result)
    if counter:
        return f"element '{V}' appears {counter} time(s) in array\nindex(es) of element: {','.join(map(str,result))}"
    else:
        return f"element '{V}' not in array"


with open('input.txt','r') as file:
    V=int(file.readline())
    A=list(map(int,file.readline().split(' ')))


if not 0<=len(A)<=10**3:
    print("wrong len of array")
    exit()

elif not V<=10**3:
    print("V is out of range")
    exit()

for i in A:
    if i>=10**3:
        print(f"element {i} is ot of range")
        exit()

print(binary_search(A,V))

