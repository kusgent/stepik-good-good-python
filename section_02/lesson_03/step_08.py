# https://stepik.org/lesson/567022/step/8?unit=561296

from math import factorial as f

n, k = map(int, input().split())

print(int(f(n) / (f(k) * f(n - k))))
