# 💧 Sistema de Análise do Consumo de Água

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Consumo consciente](https://img.shields.io/badge/Consumo_Consciente_de_Água-0077B6?style=for-the-badge)
![Educação ambiental](https://img.shields.io/badge/Educação_Ambiental-2E7D32?style=for-the-badge)

## 🌱 Sobre o projeto

Programa em **Python** que analisa o consumo mensal de água de imóveis comerciais, casas e apartamentos. Seu objetivo é incentivar o uso consciente da água por meio de mensagens educativas, de acordo com o tipo de imóvel e o consumo informado em metros cúbicos (m³).

O projeto trabalha conceitos básicos de programação, como entrada de dados, operadores lógicos e estruturas condicionais (`if`, `elif` e `else`).

## 🏠 Regras de classificação

| Tipo de imóvel | Consumo mensal | Resultado |
| --- | --- | --- |
| Comercial | Qualquer consumo válido | 🏢 Tarifa comercial — consultar o plano corporativo |
| Apartamento | Menor que 10 m³ | 💚 Consumo econômico |
| Apartamento | De 10 até 25 m³ | ✅ Consumo moderado |
| Casa | De 0 até 25 m³ | ✅ Consumo moderado |
| Casa ou apartamento | Acima de 25 m³ | ⚠️ Consumo excessivo |

O programa também informa quando o tipo de imóvel é inválido ou o consumo é negativo.

## 🚀 Como executar

1. Instale o **Python 3** no computador.
2. Salve o código do programa em um arquivo chamado `consumo_agua.py`.
3. Abra a pasta do arquivo no **VS Code** e abra o terminal.
4. Execute:

   ```bash
   python consumo_agua.py
   ```

   Se o seu sistema utilizar o comando `python3`, execute:

   ```bash
   python3 consumo_agua.py
   ```

5. Digite o tipo de imóvel e o consumo mensal quando solicitado.

**Não é necessário instalar bibliotecas adicionais.** O consumo pode ser digitado com ponto ou vírgula, como `12.5` ou `12,5`. Use números para informar o consumo.

## 💻 Exemplo de uso

```text
=== Análise do consumo de água ===
Tipo de imóvel (comercial, casa ou apartamento): apartamento
Consumo mensal em m³: 8,5
Consumo econômico – excelente controle de água!
```

## 🌎 Cada gota conta!

Feche a torneira ao escovar os dentes, reduza o tempo no banho e verifique possíveis vazamentos. **1 m³ de água equivale a 1.000 litros.**
