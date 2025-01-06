import pandas as pd
import matplotlib.pyplot as plt

# Dados iniciais
meses = list(range(1, 13))  # Meses de 1 a 12
clientes_iniciais = 100
cac_por_cliente = 150  # Custo de aquisição por cliente
ticket_primeira_compra = 100  # Ticket médio da primeira compra
ticket_recompra = 200  # Ticket médio de recompras
lucro_primeira_compra = ticket_primeira_compra * 0.3  # Margem de lucro (30%)
lucro_recompra = ticket_recompra * 0.3  # Lucro por recompra
probabilidades = [0.2] + [0.125] * 9 + [0.05] * 2  # Probabilidades de recompra por mês

# Inicializando variáveis
clientes_restantes = clientes_iniciais
custo_total = clientes_iniciais * cac_por_cliente
lucro_acumulado = lucro_primeira_compra * clientes_iniciais
custo_acumulado = custo_total - lucro_acumulado

# Estrutura de dados para a análise
data = {
    "Mês": [0] + meses,
    "Clientes Restantes": [clientes_iniciais],
    "Clientes Recomprando": [0],
    "Lucro Mensal (R$)": [lucro_primeira_compra * clientes_iniciais],
    "Lucro Acumulado (R$)": [lucro_acumulado],
    "Custo Acumulado (R$)": [custo_acumulado],
}

# Calculando valores para cada mês
for i, mes in enumerate(meses):
    prob = probabilidades[i]  # Probabilidade de recompra no mês atual
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

# Criando DataFrame
df = pd.DataFrame(data)

# Plotando os gráficos com matplotlib
plt.figure(figsize=(12, 6))

# Gráfico de Custo vs Lucro Acumulado
plt.subplot(2, 1, 1)
plt.plot(df["Mês"], df["Custo Acumulado (R$)"], label="Custo Acumulado (R$)", color="red", marker="o")
plt.plot(df["Mês"], df["Lucro Acumulado (R$)"], label="Lucro Acumulado (R$)", color="green", marker="o")
plt.title("Custo vs Lucro Acumulado")
plt.xlabel("Mês")
plt.ylabel("Valor (R$)")
plt.legend()
plt.grid()

# Gráfico de Clientes Recomprando
plt.subplot(2, 1, 2)
plt.bar(df["Mês"], df["Clientes Recomprando"], color="blue", alpha=0.7)
plt.title("Clientes Recomprando por Mês")
plt.xlabel("Mês")
plt.ylabel("Quantidade de Clientes")
plt.grid(axis="y")

# Ajustando layout e exibindo os gráficos
plt.tight_layout()
plt.show()
