
#voce foi contratado para criar um programa de calculo de media de notas escolares 
#este programa recebera duas notas e calculara a media 
#1.solicitar o input das notas numericas [ int ou float]
nota1 = int (input("Insira o primeiro numero da nota :"))
nota2 = int (input("Insira o segundo numero da nota :"))

#2.Realizar o calculo de media = (nota1 + nota2)/2
media = (nota1 + nota2)/2
print(media)

#3.Verificar se o aluno tiver nota >=5, então aprovado, senao reprovado, para isso vamos fazer uma comparação
if media >= 5:
    print("Aprovado")
else:
    print("Reprovado")
