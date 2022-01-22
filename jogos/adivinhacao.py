print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 32
total_tentativas = 3
rodada = 1

# Sintaxe do loop usando comando while
# while(rodada <= total_tentativas):
#
# Sintaxe do loop usando comando for. O segundo argumento da função range é exclusivo. Isto é, o for será executado
# enquanto o valor de 'rodada' for menor que o valor da variável total_tentativas. Se não fosse somando 1 ao valor
# da variável total_tentativas a iteração ocorreria somente de 1 a 2.
#
for rodada in range(1, total_tentativas+1):
    # Usando String interpolation
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    # Por padrão quando se usa o input a variável que receberá o valor vindo do input será do tipo str
    chute_str = input("Digite o seu número: ")

    print("Você digitou o número ",chute_str)

    # Converte o valor de chute_str para uma variável do tipo int
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    # Blocos de comandos if / else devem ser iniciados com : (dois-pontos) como é o caso abaixo.
    if(numero_secreto == chute):
        # O Python exige uma identação de 4 espaços para que o comando seja considerado parte integrante de uma condição
        # if ou else. Tudo aquilo que tiver que ser executado dentro do bloco corresponde ao if ou ao else deve estar
        # devidamente identado. O primeiro comando que não estiver devidamente identado será considerado como fora
        # do bloco if / else.
        #
        print("Você acertou!")
    else:
        print("Você errou!")
        if(maior):
            print("O número que você digitou é maior que o número secreto.")
        elif(menor):
            print("O número que você digitou é menor que o número secreto.")
    # No caso de loop usando o comando for não se deve somar 1 ao valor da variável 'rodada'
    # rodada = rodada + 1

# Conforme mencionado acima, a linha abaixo será executada independentemente do resultado da condiçã if /else acima.
print("Fim do jogo")