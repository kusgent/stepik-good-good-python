# https://stepik.org/lesson/567030/step/9?auth=login&unit=561304

marks = list(map(int, input().split()))

print(round(sum(marks) / len(marks), 1))
