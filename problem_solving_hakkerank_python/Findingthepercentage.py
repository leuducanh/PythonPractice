if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = str(input())
    scores = student_marks[query_name]

    print("{0:.2f}".format(round(sum(scores) / float(len(scores)), 2)))