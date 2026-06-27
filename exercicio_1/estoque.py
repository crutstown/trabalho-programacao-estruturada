# Arquivo: estoque.py

def cadastrar_produtos():
    produtos = []

    while True:
        try:
            qtd = int(input("Quantos produtos deseja cadastrar? "))
            if qtd > 0:
                break
            print("Digite um número maior que zero.")
        except ValueError:
            print("Entrada inválida.")

    for i in range(qtd):
        print(f"\nProduto {i+1}")

        nome = input("Nome: ")

        while True:
            try:
                estoque = int(input("Quantidade inicial: "))
                if estoque >= 0:
                    break
                print("Quantidade inválida.")
            except ValueError:
                print("Digite um número inteiro.")

        for i in range(qtd):
            try:
                preco = float(input("Preço unitário: R$ "))
                if preco >= 0:
                    break
                print("Preço inválido.")
            except ValueError:
                print("Digite um valor válido.")

        produtos.append({
            "nome": nome,
            "estoque": estoque,
            "preco": preco
        })

    return produtos


def escolher_produto(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return None

    print("\nProdutos:")
    for i, produto in enumerate(produtos):
        print(f"{i + 1} - {produto['nome']}")

    while True:
        try:
            opcao = int(input("Escolha o número do produto: "))
            if 1 <= opcao <= len(produtos):
                return produtos[opcao - 1]
            print("Opção inválida.")
        except ValueError:
            print("Digite um número válido.")


def adicionar_estoque(produtos):
    produto = escolher_produto(produtos)
    if produto is None:
        return

    while True:
        try:
            qtd = int(input("Quantidade a adicionar: "))
            if qtd > 0:
                produto["estoque"] += qtd
                print("Estoque atualizado!")
                break
            print("Digite um valor maior que zero.")
        except ValueError:
            print("Entrada inválida.")


def retirar_estoque(produtos):
    produto = escolher_produto(produtos)
    if produto is None:
        return

    while True:
        try:
            qtd = int(input("Quantidade a retirar: "))
            if qtd <= 0:
                print("Digite um valor maior que zero.")
            elif qtd > produto["estoque"]:
                print("Estoque insuficiente.")
            else:
                produto["estoque"] -= qtd
                print("Retirada realizada!")
                break
        except ValueError:
            print("Entrada inválida.")


def consultar_produto(produtos):
    produto = escolher_produto(produtos)
    if produto is None:
        return

    print("\n--- Produto ---")
    print("Nome:", produto["nome"])
    print("Quantidade:", produto["estoque"])
    print(f"Preço unitário: R$ {produto['preco']:.2f}")
    print(f"Valor total: R$ {produto['estoque'] * produto['preco']:.2f}")


def listar_produtos(produtos):
    print("\n===== ESTOQUE =====")

    for produto in produtos:
        valor = produto["estoque"] * produto["preco"]

        print(f"\nNome: {produto['nome']}")
        print(f"Quantidade: {produto['estoque']}")
        print(f"Preço unitário: R$ {produto['preco']:.2f}")
        print(f"Valor total em estoque: R$ {valor:.2f}")


def menu():
    produtos = cadastrar_produtos()

    while True:
        print("\n========== MENU ==========")
        print("(a) Adicionar unidades ao estoque")
        print("(b) Retirar unidades do estoque")
        print("(c) Consultar um produto")
        print("(d) Listar todos os produtos")
        print("(e) Encerrar o programa")

        opcao = input("Escolha uma opção: ").strip().lower()

        if opcao == "a":
            adicionar_estoque(produtos)
        elif opcao == "b":
            retirar_estoque(produtos)
        elif opcao == "c":
            consultar_produto(produtos)
        elif opcao == "d":
            listar_produtos(produtos)
        elif opcao == "e":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()