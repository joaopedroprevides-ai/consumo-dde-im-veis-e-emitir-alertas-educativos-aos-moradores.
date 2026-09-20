# Classificação do consumo mensal de água
print("=== Análise do consumo de água ===")

# Recebe o tipo de imóvel e transforma o texto em minúsculas.
tipo = input("Tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()

# Aceita consumo com ponto ou vírgula, como 12.5 ou 12,5.
consumo = float(input("Consumo mensal em m³: ").replace(",", "."))

# Verifica os dados e classifica o consumo.
if tipo not in ("comercial", "casa", "apartamento"):
    print("Tipo de imóvel inválido.")

elif consumo < 0:
    print("O consumo não pode ser negativo.")

elif tipo == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif tipo == "apartamento" and consumo < 10:
    print("Consumo econômico – excelente controle de água!")

elif tipo in ("apartamento", "casa") and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")

else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")