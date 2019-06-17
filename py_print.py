import sys


print(1)

x = 0.2
s = "hello"
print(x)
print(s)
print(x, s)

print('Hello World', file=sys.stdout)

f = open('hello.txt', 'w')
print('Hello World', file=f)
f.close()