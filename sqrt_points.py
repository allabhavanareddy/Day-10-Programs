def sqrt_bs(n,epsilon=1e-6):
    if n<0:
        raise ValueError("cannot compte the square")
    if n<1:
        left,right=n,1
    else:
        left,right=0,n
    while abs(left-right)>epsilon:
        mid=(left+right)/2
        mid_square=mid*mid
        if mid_square<n:
            left=mid
        else:
            right=mid
    return (left+right)/2
n=int(input())
result=sqrt_bs(n)
print(f"The square root of {n} is approximately {result}")
        