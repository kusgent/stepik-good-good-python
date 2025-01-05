# https://stepik.org/lesson/567024/step/12?unit=561298

a, b, c = map(int, input().split())

print((a + b) > c and (a + c) > b and (b + c) > a)
