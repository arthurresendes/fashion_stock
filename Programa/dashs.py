import matplotlib.pyplot as plt
from querys import contagem_tipos, menor_preco


def grafico_tipos_qtd():
    res = contagem_tipos()
    
    tipo = [item[0] for item in res]
    quantidade_tipo = [item[1] for item in res]
    
    cores = ['blue', 'orange', 'purple', 'red', 'green']
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(tipo, quantidade_tipo, color=cores) 
    
    ax.set_title('Contagem por tipo', fontsize=16)
    ax.set_xlabel('Tipo produto', fontsize=12)
    ax.set_ylabel('Quantidade', fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    return fig

def grafico_menor_preco():
    res = menor_preco()
    
    tipo = res[0]
    marca = res[1]
    cor = res[2]
    preco = res[3]
    
    frase = f"{tipo} da {marca} com coloração {cor}"

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(frase, preco, color='pink') 
    
    ax.set_title('Produto com menor preço', fontsize=16)
    ax.set_xlabel('Informações', fontsize=12)
    ax.set_ylabel('Preço', fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    return fig