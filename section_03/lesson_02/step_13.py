# https://stepik.org/lesson/567026/step/13?unit=561300

s1, s2 = map(str, input().split())

print(s1[:len(s2)][1::2] == s2[1::2])
