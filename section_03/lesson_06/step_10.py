# https://stepik.org/lesson/567030/step/10?auth=login&unit=561304

title = input()
author = input()
number_of_pages = int(input())
price = float(input())

book = [title, author, number_of_pages, price]

del book[2]
book[1] = "Пушкин"
book[2] *= 2

print(book)
