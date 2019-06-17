
f = open('text.txt', 'rt', encoding='utf-8')
text = f.read()
print(text)
f.seek(6, 0)
text = f.read()
print(text)
f.close()


with open('py_print.py', 'r', encoding='utf-8') as f3:
    for line in f3.readlines():
        print(line, end='')

print(f3.closed)
