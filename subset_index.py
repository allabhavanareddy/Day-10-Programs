#program to print the index of subset equal to target sum


def sum(left,right,l):
    while left<right:
        if l[left]+l[right]==target:
           return left,right
        if l[left]+l[right]<target:
            return sum(left+1,right,l)
        else:
            return sum(left,right+1,l)
l=list(map(int,input().split()))
target=int(input())
res=sum(0,len(l)-1,l)
print(res)
print(f"[{res[0]},{res[1]}]") 

