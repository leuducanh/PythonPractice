if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max = arr[0]
    max2= arr[0]-1
    for i in range(n):
        if arr[i] > max:
            max2 = max
            max = arr[i]
        elif arr[i] > max2 & arr[i] != max:
            max2 = arr[i]
    print(str(max2))