import pandas as pd
import numpy as np

dicionario_2 = {"I": 10, "II": 42, "III": 7, "V": 1_000_000}
dicionario_3 = {"I": 1, "II": 12, "III": 13, "IV": 0}

ser_8 = pd.Series(dicionario_2)
ser_9 = pd.Series(dicionario_3)

resultado = ser_8.add(ser_9)
print("\nSérie adicionada: ", resultado, sep = "\n")

resultado = ser_8.sub(ser_9)
print("\nSérie subtraída: ", resultado, sep = "\n")

dicionario_4 = {"V": 42}
ser_10 = pd.Series(dicionario_4)
print("\nSérie 10: ", ser_10, sep = "\n")

print("\nConcatenação sem índices repetidos: ", pd.concat([ser_9, ser_10]),sep = "\n")
print("\nConcatenação com índices repetidos: ", pd.concat([ser_8, ser_10]),sep = "\n")

# duplicated
# drop_duplicates

print("Série count: ", resultado.count()) # Número de valores não NaN
print("Série size: ", resultado.size) # Número total de valores

print("#"*100)

resultado = ser_8.add(ser_9)
print("\nSérie adicionada com NaN: ", resultado, sep = "\n")

print("Série count: ", resultado.count())
print("Série size: ", resultado.size)

resultado = ser_8.add(ser_9, fill_value = 42)
print("\nSérie adicionada com valores NaN substitúidos durante a operação: ", resultado, sep = "\n")

print("Série count: ", resultado.count())
print("Série size: ", resultado.size)

resultado = ser_8.add(ser_9, fill_value = "0")
print("\nSérie adicionada com valor em string: ", resultado, sep = "\n")

print("#"*100)

resultado = ser_8.add(ser_9)
resultado.dropna(inplace = True)
print("\nSérie adicionada com valores NaN descartados: ", resultado, sep = "\n")

print("Série count: ", resultado.count())
print("Série size: ", resultado.size)

print("#"*100)

resultado = ser_8.add(ser_9)
resultado.fillna(42, inplace = True)
print("\nSérie adicionada com valores NaN substituídos após a operação: ", resultado, sep = "\n")

print("Série count: ", resultado.count())
print("Série size: ", resultado.size)



































