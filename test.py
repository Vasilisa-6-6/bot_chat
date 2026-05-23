f = open('text.txt', 'w', encoding='utf-8')
f.write('наггетсы,\nнаггетсы\nвсего за 69 руб\n9 штук\nнаггетсов\nтолько в burger king!!!!!')
f.close()

f = open('text.txt', 'r', encoding='utf-8')
s = f.read()
print(s)
f.close()

with open('text.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    print(s)