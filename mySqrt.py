def mySqrt(x):
    if x == 1 or x == 0:
        return x

    start = 1
    end = x//2

    while start <= end:
        print(start, end)
        mid = (start+end)//2
        print(mid)
        mid_start = mid * mid
        print(mid_start)
        mid_end = (mid + 1) * (mid + 1)
        print(mid_end)
        print('__________')
        if x == mid_start:
            return mid
        elif x == mid_end:
            return mid+1
        elif x > mid_start and x < mid_end:
            return mid
        elif x < mid_start:
            end = mid - 1
        elif x > mid_end:
            start = mid + 1


print(mySqrt(121))
print(mySqrt(8))