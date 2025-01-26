# https://stepik.org/lesson/567030/step/14?auth=login&unit=561304

cities1 = list(map(str, input().split()))

cities2 = ["Москва", "Тверь", "Вологда"]

cities3 = cities2 + cities1

print(*cities3)
