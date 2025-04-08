import json


with open("dados.json", "r") as file:
    dados = json.load(file)


valores_validos = [dia["valor"] for dia in dados if dia["valor"] > 0]


menor = min(valores_validos)
maior = max(valores_validos)
media = sum(valores_validos) / len(valores_validos)


dias_acima_media = len([v for v in valores_validos if v > media])


print(f"Menor faturamento: R$ {menor:.2f}")
print(f"Maior faturamento: R$ {maior:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
