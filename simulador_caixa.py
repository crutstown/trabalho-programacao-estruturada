# Arquivo: simulador_caixa.py

def ler_inteiro_positivo(mensagem, minimo=1):
    while True:
        try:
            valor = int(input(mensagem))
            if valor >= minimo:
                return valor
            print(f"Erro: O valor deve ser maior ou igual a {minimo}.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

def calcular_tempo_atendimento(itens):
    return 2 + 0.5 * itens

def encontrar_caixa_menor_tempo(tempos_caixas):
    menor_tempo = tempos_caixas[0]
    indice_menor = 0
    
    for i in range(1, len(tempos_caixas)):
        if tempos_caixas[i] < menor_tempo:
            menor_tempo = tempos_caixas[i]
            indice_menor = i
            
    return indice_menor

def alocar_cliente(caixas, tempos_caixas, codigo_cliente, tempo_atendimento):
    indice_caixa = encontrar_caixa_menor_tempo(tempos_caixas)
    caixas[indice_caixa].append(codigo_cliente)
    tempos_caixas[indice_caixa] += tempo_atendimento

def calcular_estatisticas(tempos_clientes, tempos_caixas):
    tempo_medio_cliente = sum(tempos_clientes) / len(tempos_clientes) if tempos_clientes else 0
    
    maior_tempo = max(tempos_caixas)
    menor_tempo = min(tempos_caixas)
    
    caixa_maior = tempos_caixas.index(maior_tempo) + 1
    caixa_menor = tempos_caixas.index(menor_tempo) + 1
    
    tempo_total_sistema = maior_tempo
    
    return tempo_medio_cliente, caixa_maior, caixa_menor, tempo_total_sistema

def exibir_resultado(caixas, tempos_caixas, tempos_clientes):
    print("\n" + "="*50)
    print("               RESULTADO DA SIMULAÇÃO               ")
    print("="*50)
    
    for i in range(len(caixas)):
        clientes_str = ", ".join(caixas[i]) if caixas[i] else "Nenhum cliente"
        print(f"Caixa {i + 1}:")
        print(f"  Clientes atendidos: {clientes_str}")
        print(f"  Tempo total: {tempos_caixas[i]:.1f} minutos\n")
        
    tempo_medio, caixa_maior, caixa_menor, tempo_total = calcular_estatisticas(tempos_clientes, tempos_caixas)
    
    print("-" * 50)
    print(f"Tempo médio de atendimento por cliente: {tempo_medio:.2f} minutos")
    print(f"Caixa com maior tempo acumulado: Caixa {caixa_maior}")
    print(f"Caixa com menor tempo acumulado: Caixa {caixa_menor}")
    print(f"Tempo total necessário para encerrar os atendimentos: {tempo_total:.1f} minutos")
    print("="*50)

def main():
    print("=== SIMULADOR DE CAIXA DE SUPERMERCADO ===")
    
    qtd_caixas = ler_inteiro_positivo("Quantidade de caixas: ")
    qtd_clientes = ler_inteiro_positivo("Quantidade de clientes: ")
    
    caixas = [[] for _ in range(qtd_caixas)]
    tempos_caixas = [0.0] * qtd_caixas
    tempos_clientes = []
    
    for i in range(qtd_clientes):
        print(f"\nCliente {i + 1}:")
        codigo = input("Código: ").strip()
        itens = ler_inteiro_positivo("Quantidade de itens: ", minimo=0)
        
        tempo = calcular_tempo_atendimento(itens)
        tempos_clientes.append(tempo)
        
        alocar_cliente(caixas, tempos_caixas, codigo, tempo)
        
    exibir_resultado(caixas, tempos_caixas, tempos_clientes)

if __name__ == "__main__":
    main()