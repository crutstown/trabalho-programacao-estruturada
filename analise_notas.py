# Arquivo: analise_notas.py

def ler_quantidade_alunos():
    while True:
        try:
            qtd = int(input("Solicite a quantidade de alunos da turma: "))
            if qtd > 0:
                return qtd
            print("A quantidade deve ser maior que zero.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: Digite um valor numérico válido.")

def definir_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif 5 <= media < 7:
        return "Recuperação"
    else:
        return "Reprovado"

def coletar_dados_turma(qtd_alunos):
    turma = []
    for i in range(qtd_alunos):
        print(f"\n--- Dados do Aluno {i+1} ---")
        nome = input("Nome do aluno: ").strip()
        
        n1 = ler_nota("Digite a primeira nota: ")
        n2 = ler_nota("Digite a segunda nota: ")
        n3 = ler_nota("Digite a terceira nota: ")
        
        media = (n1 + n2 + n3) / 3
        situacao = definir_situacao(media)
        
        turma.append({
            "nome": nome,
            "n1": n1,
            "n2": n2,
            "n3": n3,
            "media": media,
            "situacao": situacao
        })
    return turma

def exibir_relatorio(turma):
    print("\n" + "="*85)
    print(f"{'Nome do Aluno':<25} | {'Nota 1':<8} | {'Nota 2':<8} | {'Nota 3':<8} | {'Média':<8} | {'Situação':<12}")
    print("="*85)
    
    soma_medias = 0
    aluno_maior = turma[0]
    aluno_menor = turma[0]
    aprovados = 0
    recuperacao = 0
    reprovados = 0
    
    for aluno in turma:
        print(f"{aluno['nome']:<25} | {aluno['n1']:<8.1f} | {aluno['n2']:<8.1f} | {aluno['n3']:<8.1f} | {aluno['media']:<8.2f} | {aluno['situacao']:<12}")
        
        soma_medias += aluno['media']
        
        if aluno['media'] > aluno_maior['media']:
            aluno_maior = aluno
        if aluno['media'] < aluno_menor['media']:
            aluno_menor = aluno
            
        if aluno['situacao'] == "Aprovado":
            aprovados += 1
        elif aluno['situacao'] == "Recuperação":
            recuperacao += 1
        else:
            reprovados += 1
            
    media_geral = soma_medias / len(turma)
    
    print("="*85)
    print(f"\nMédia geral da turma: {media_geral:.2f}")
    print(f"Aluno com maior média: {aluno_maior['nome']} ({aluno_maior['media']:.2f})")
    print(f"Aluno com menor média: {aluno_menor['nome']} ({aluno_menor['media']:.2f})")
    print(f"Quantidade de aprovados: {aprovados}")
    print(f"Quantidade de alunos em recuperação: {recuperacao}")
    print(f"Quantidade de reprovados: {reprovados}")
    print("="*85)

def main():
    print("=== SISTEMA DE ANÁLISE DE NOTAS ===")
    qtd = ler_quantidade_alunos()
    turma = coletar_dados_turma(qtd)
    exibir_relatorio(turma)

if __name__ == "__main__":
    main()