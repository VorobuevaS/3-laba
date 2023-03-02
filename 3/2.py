n = input('Vvedite slovo')
d = 'ф'
x = 1
i = 0
while i < len(n):
    s = n[:(len(n)-1)]
    n = n[((len(n)+1)-len(n)):]
    i += 1
    if s == d:
       x = 1
if x == 0:
    print('Ого! Это редкое слово!')
else:
    print('Эх! Слово, конечно, не редкость!')



