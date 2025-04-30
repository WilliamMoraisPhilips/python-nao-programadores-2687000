ano_nascimento = 1989
ano_formatura = 2010

# Considerando que as variáveis acima correspondem a 'Gerlaine', descubra a idade dela no ano da sua formatura
print(f"A idade de Gerlaine em sua formatura era {ano_formatura - ano_nascimento} anos de idade")

# Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print(ano_nascimento == ano_formatura)
print(ano_nascimento > ano_formatura)
print(ano_nascimento <= ano_formatura)

# Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
print(ano_nascimento != ano_formatura & ano_formatura > ano_nascimento)
print(ano_nascimento == ano_formatura | ano_formatura >= ano_nascimento)