str=input("enter two nums devided by space: ")

space_ind=str.index(" ")

a=int(str[:space_ind])
b=int(str[space_ind+1:])

if abs(a) >= 10**9 or abs(b) >= 10**9:
    print("wrong input : number out of range")
else:
    print(a+b)
