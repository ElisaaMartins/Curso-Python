# São imutáveis

halogenios = ('F', 'Cl', 'Br', 'I', 'At')

print(len(halogenios))

gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')

elementos = halogenios + gases_nobres

t1 = (5,2,6,8,4,5,6,4,4,0,12,22,3,4,5)

print(t1.count(3))
print(max(t1))

# Operações não disponíveis em tuplas: .sort(), .append(), reverse(), .pop()...
for elemento in elementos:
    print(f'Elemento químico: {elemento}')


grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(alcalinos)