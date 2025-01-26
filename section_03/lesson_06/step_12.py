# https://stepik.org/lesson/567030/step/12?auth=login&unit=561304

list_of_numbers = list(map(int, input().split()))

list_of_numbers = sorted(list_of_numbers, reverse=True)

print(*list_of_numbers)
