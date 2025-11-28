vendas = [100.5, 112.9, 75.48, 66.99, 17.12, 70.0]

total_vendas = sum(vendas)
qtd_vendas = len(vendas)

media_vendas = total_vendas / qtd_vendas

print("----- Relatório de Vendas -----")
print("Total de Vendas: R$", total_vendas)
print("Ticket Médio: R$", media_vendas)