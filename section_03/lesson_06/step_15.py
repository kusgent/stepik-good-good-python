# https://stepik.org/lesson/567030/step/15?auth=login&unit=561304

cities1 = list(map(str, input().split()))

cities2 = ["Москва", "Тверь", "Вологда"]

cities3 = cities1 + cities2

print(*cities3)
