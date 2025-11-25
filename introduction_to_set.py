def average(array):
    distinct_heights = set(array)
    total = sum(distinct_heights)
    avg = total/len(distinct_heights)
    return round (avg, 3)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)