# Finding the Percentage
# https://www.hackerrank.com/challenges/finding-the-percentage/problem
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for k,v in student_marks.items():
        if k == query_name:
            avg_score = sum(v)/len(v)
    
    print(f"{avg_score:.2f}")
