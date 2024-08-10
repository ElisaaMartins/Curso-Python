#programa de disparo de alarme

porta = 'f'
janela = 'f'

alarme = (porta == 'a') or (janela == 'a')
msg = 'Alarme disparado? ' + str(alarme)

print(msg)
