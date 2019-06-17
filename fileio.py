
f = open('text.txt', 'w', encoding='utf-8')
writesize = f.write('안녕하세요\n파이썬입니다.!@#$%')
f.close()

f = open('text2.txt', 'wb')
writesize = f.write(bytes('파이썬~', encoding='utf-8'))
f.close()

f = open('text2.txt', 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()

f = open('미친개알고리즘.PNG', 'rb')
data = f.read()
f.close()

f = open('testpng.png', 'wb')
writesize = f.write(data)
f.close()
