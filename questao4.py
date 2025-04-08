import xml.etree.ElementTree as ET

tree = ET.parse("faturamento.xml")
root = tree.getroot()

valores = {}
total = 0

for estado in root.findall("estado"):
    sigla = estado.find("sigla").text
    valor = float(estado.find("valor").text)
    valores[sigla] = valor
    total += valor

for sigla, valor in valores.items():
    percentual = (valor / total) * 100
    print(f"{sigla}: {percentual:.2f}%")
