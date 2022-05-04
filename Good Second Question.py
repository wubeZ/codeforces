def main():
    n, m = map(int, input().split())
    students = list(map(int, input().split()))
    students.sort()
    ans = []
    if len(students) % 2 == 0:
        mid = len(students)//2 - 1
    else:
        mid = len(students)//2
 
    for i in range(n):
        question = int(input())
        if students[mid] < question or students[0] >= question:
            ans.append('NO')
        elif question <= students[mid]:
            ans.append('YES')
 
    for i in ans:
        print(i)
 
 
main()
