if __name__ == '__main__':
    min = 1000
    min2 = min
    arrmin = []
    arrmin2 = []
    for _ in range(int(input())):
        name = str(input())
        score = float(input())
        if (score < min):
            min2 = min
            min = score
            del arrmin2[:]
            arrmin2.extend(arrmin)
            del arrmin[:]
            arrmin.append(name)
        elif score > min and score < min2:
            min2 = score
            del arrmin2[:]
            arrmin2.append(name)
        elif score == min:
            arrmin.append(name)
        elif score == min2:
            arrmin2.append(name)
    arrmin2.sort()
    for pos in range(len(arrmin2)):
        print(arrmin2[pos])
