n1 = float(input('Digite a nota da primeira prova: '))
n2 = float(input('Digite a nota da segunda prova: '))
n3 = float(input('Digite a nota de trabalho: '))
n4 = float(input('Digite a nota de tarefa: '))
n5 = float(input('Digite a nota atitudinal: '))
m = (n1+n2+n3+n4+n5)/5
print('Sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Ai sim, tu passou!')
else:
    print('Vish, tu não passou!')