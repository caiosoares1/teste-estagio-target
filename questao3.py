
# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#  - O menor valor de faturamento ocorrido em um dia do mês;
#  - O maior valor de faturamento ocorrido em um dia do mês;
#  - Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#  a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#  b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
import json

with open('dados.json', 'r') as file:
    dados = json.load(file)

faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

media_mensal = sum(faturamento) / len(faturamento)

dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")