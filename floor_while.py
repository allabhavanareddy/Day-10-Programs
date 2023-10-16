# floor value (if 6 is not in the list then it will print less than that "5")
def bs_floor(l,target):
    si=0
    li=len(l)-1
    floor=-1
    while(si<=li):
        mid=((si+li)//2)
        if l[mid]==target:
            return l[mid]
        elif l[mid]<target:
            floor=l[mid]
            si=mid+1
        else:
            li=mid-1
    return floor
l=list(map(int,input().split()))
target=int(input())
print(bs_floor(l,target))

