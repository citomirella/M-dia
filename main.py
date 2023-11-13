nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
print('Media: ', media)

if media >= 6:
  print('Aluno aprovado')
elif media <6:
  print('Aluno de recuperação')
  nota3 = float(input('Digite a nota da recuperação: '))

  exame = (media + nota3) / 2
  print("Media final =" , exame)

  if exame
