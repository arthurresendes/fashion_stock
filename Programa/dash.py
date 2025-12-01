from querys import consulta_dahs
import matplotlib as plt



x_data = [1]
y_data = [res]
plt.figure(figsize=(8, 5))
plt.plot(x_data, y_data, marker='o', linestyle='--', color='blue', label=f'Total {TIPO} - {MARCA}')
plt.xlabel(f"Query Result (Total Count for {TIPO})")
plt.ylabel("Number of Items")
plt.title(f"Inventory Count for {TIPO} ({MARCA}, {COR}, {TAMANHO}, {GENERO})")
plt.legend()
plt.grid(True)
plt.show()