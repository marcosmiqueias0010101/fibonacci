# Lista de preços em diferentes estabelecimentos
produtos = {
    "Produto A": {"estabelecimento_1": 20, "estabelecimento_2": 61, "estabelecimento_3": 37},
    "Produto B": {"estabelecimento_1": 17, "estabelecimento_2": 13, "estabelecimento_3": 15},
    "Produto C": {"estabelecimento_1": 37, "estabelecimento_2": 37, "estabelecimento_3": 35},
    "Produto D": {"estabelecimento_1": 33, "estabelecimento_2": 37, "estabelecimento_3": None},
}

# Função para verificar onde há economia e qual é o preço mais barato
def verificar_economias(produtos):
    for produto, precos in produtos.items():
        preco_minimo = min(precos.values())
        estabelecimentos_baratos = [estabelecimento for estabelecimento, preco in precos.items() if preco == preco_minimo]
        
        print(f"{produto}:")
        for estabelecimento, preco in precos.items():
            if preco == preco_minimo:
                print(f"  {estabelecimento}: R${preco:.2f} (Mais barato!)")
            else:
                print(f"  {estabelecimento}: R${preco:.2f}")

# Chama a função
verificar_economias(produtos) 