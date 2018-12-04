def insert(lstori, lst):
    lstori.insert(lst[0], lst[1])
    return lstori


def remove(lstori, lst):
    lstori.remove(lst[0])
    return lstori


def append(lstori, lst):
    lstori.append(lst[0])
    return lstori


if __name__ == '__main__':
    N = int(input())
    command = {
        "insert": lambda lstori, lst: lstori.insert(lst[0], lst[1]),
        "print": lambda lstori, lst: print(lstori),
        "remove": lambda lstori, lst: remove(lstori, lst),
        "append": lambda lstori, lst: append(lstori, lst),
        "sort": lambda lstori, lst: lstori.sort(),
        "pop": lambda lstori, lst: lstori.pop(0),
        "reverse": lambda lstori, lst: lstori.reverse()
    }
    lstori = []
    i = 0
    while i < N:
        lst = list(input().split())
        lstcomand = list(map(int, lst[1:]))
        command[lst[0]](lstori, lstcomand)
        i += 1



