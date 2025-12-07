import matplotlib.pyplot as plt
from querys import dash_maior_qtd


def grafico_maiores_qtd():
    res = dash_maior_qtd()
    
    tipo = [item[0] for item in res]
    quantidade = [item[1] for item in res]
    
    cores = ['red', 'green', 'blue', 'orange', 'purple']
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(tipo, quantidade, color=cores) 
    
    ax.set_title('Quantidade em estoque', fontsize=16)
    ax.set_xlabel('Tipo produto', fontsize=12)
    ax.set_ylabel('Quantidade', fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    return fig