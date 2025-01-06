# BI-Analytics
Case de Business Analytics ( Basico )
_____________________________________________
import pandas as pd
import matplotlib.pyplot as plt


meses = list(range(1, 13))  
clientes_iniciais = 100
cac_por_cliente = 150 
ticket_primeira_compra = 100  
ticket_recompra = 200  
lucro_primeira_compra = ticket_primeira_compra * 0.3 
lucro_recompra = ticket_recompra * 0.3  
probabilidades = [0.2] + [0.125] * 9 + [0.05] * 2  


clientes_restantes = clientes_iniciais
custo_total = clientes_iniciais * cac_por_cliente
lucro_acumulado = lucro_primeira_compra * clientes_iniciais
custo_acumulado = custo_total - lucro_acumulado


data = {
    "Mês": [0] + meses,
    "Clientes Restantes": [clientes_iniciais],
    "Clientes Recomprando": [0],
    "Lucro Mensal (R$)": [lucro_primeira_compra * clientes_iniciais],
    "Lucro Acumulado (R$)": [lucro_acumulado],
    "Custo Acumulado (R$)": [custo_acumulado],
}


for i, mes in enumerate(meses):
    prob = probabilidades[i] 
    clientes_recomprando = int(clientes_restantes * prob)
    lucro_mensal = clientes_recomprando * lucro_recompra
    lucro_acumulado += lucro_mensal
    custo_acumulado = max(0, custo_acumulado - lucro_mensal)

    data["Clientes Restantes"].append(clientes_restantes)
    data["Clientes Recomprando"].append(clientes_recomprando)
    data["Lucro Mensal (R$)"].append(lucro_mensal)
    data["Lucro Acumulado (R$)"].append(lucro_acumulado)
    data["Custo Acumulado (R$)"].append(custo_acumulado)

    clientes_restantes -= clientes_recomprando

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))
# Grafico 1 - custo vs lucro
plt.subplot(2, 1, 1)
plt.plot(df["Mês"], df["Custo Acumulado (R$)"], label="Custo Acumulado (R$)", color="darkcyan", marker="o")
plt.plot(df["Mês"], df["Lucro Acumulado (R$)"], label="Lucro Acumulado (R$)", color="darkblue", marker="o")
plt.title("Custo vs Lucro Acumulado")
plt.xlabel("Mês")
plt.ylabel("Valor (R$)")
plt.legend()
plt.grid()

# Grafico 2 - clientes na recompra
plt.subplot(2, 1, 2)
plt.bar(df["Mês"], df["Clientes Recomprando"], color="darkblue", alpha=0.7)
plt.title("Clientes Recomprando por Mês")
plt.xlabel("Mês")
plt.ylabel("Quantidade de Clientes")
plt.grid(axis="y")


plt.tight_layout()
plt.show()![download](https://github.com/user-attachments/assets/97d0df78-c0c8-41c5-b72d-4e0e5ccb7470)


