def main():
    n = input()
    setname = 0
    while n != 0:
        setname += 1
        print("Set #" + str(setname))
        arr = []
        for i in range(0,int(n)):
            arr.append(int(input()))
        sumup = sum(arr)
        totalChange = 0
        for i in range(0,int(n)):
            totalChange += abs(arr[i] - sumup)
        print("The minimum number of moves is " + str(totalChange) + ".")
main()