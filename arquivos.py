
# PARTE 1 - CADASTRAR OS ALUNOS

while True:
    nome = input("Digite o nome do aluno: ")

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    arquivo = open("notas.txt", "a", encoding="utf-8")

    arquivo.write(f"{nome};{nota1};{nota2};{nota3}\n")

    arquivo.close()

    continuar = input("Deseja cadastrar outro aluno? (s/n): ")

    if continuar.lower() != "s":
        break


# PARTE 2 - CALCULAR AS MEDIAS E SEPARAR OS RESULTADOS

# Abrir os arquivos de resultado no modo "w"
# para substituir os resultados da execucao anterior.

aprovados = open("aprovados.txt", "w", encoding="utf-8")
exame = open("exame.txt", "w", encoding="utf-8")
reprovados = open("reprovados.txt", "w", encoding="utf-8")

with open("notas.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        dados = linha.strip().split(";")

        nome = dados[0]
        nota1 = float(dados[1])
        nota2 = float(dados[2])
        nota3 = float(dados[3])

        media = (nota1 + nota2 + nota3) / 3

        if media >= 7:
            situacao = "Aprovado"
            destino = aprovados

        elif media >= 5:
            situacao = "Exame"
            destino = exame

        else:
            situacao = "Reprovado"
            destino = reprovados

        destino.write(
            f"Nome: {nome}; "
            f"Notas: {nota1}, {nota2}, {nota3}; "
            f"Media: {media:.2f}; "
            f"Situacao: {situacao}\n"
        )

        print(nome, "- Media:", round(media, 2), "-", situacao)

aprovados.close()
exame.close()
reprovados.close()

print("Processamento concluido!")
