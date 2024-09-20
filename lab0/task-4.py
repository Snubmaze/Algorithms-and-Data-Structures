nums=open('input.txt','r').read()

space_ind=nums.index(" ")

a=int(nums[:space_ind])
b=int(nums[space_ind+1:])

if abs(a) >= 10**9 or abs(b) >= 10**9:
    print("wrong input : number out of range")
else:
    output=open("output.txt",'w').write(str(a+b**2))
