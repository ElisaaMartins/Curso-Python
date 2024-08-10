# programa que vai exibir uma lista de pedras preciosas exceto a que estiver especificada
pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamente', 'Turmalina')

for pedra in pedras:
    if pedra == 'Quartzo':
        continue # só finaliza a interação atual 
    print (pedra)
    
# break => finaliza o laço todo



