#ceil(if number is not present in between the list,it will print greater than that" if 3 it print 4")
def bs_ceil(l,target):
    si=0
    li=len(l)-1
    while(si<=li):
        mid=((si+li)//2)
        if l[mid]==target:
            return l[mid]
        elif l[mid]<target:
            si=mid+1
        else:
            ceil=l[mid]
            li=mid-1
    return ceil
l=list(map(int,input().split()))
target=int(input())
print(bs_ceil(l,target))