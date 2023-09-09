import pandas as pd
import numpy as np

# Estruturas de dados iniciais

lista_1 = [1, 2, 3, 4, 5]
lista_2 = ["I", "II", "III", "IV", "V"]

dicionario_1 = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5}

ndarray_1 = np.array(lista_1)

print(lista_1)
print(lista_2)
print(dicionario_1)
print(ndarray_1)

print("#"*100)

ser_1 = pd.Series(lista_1)
print("\nSérie 1 (lista):", ser_1, sep = "\n")

ser_2 = pd.Series(lista_2)
print("\nSérie 2 (lista):", ser_2, sep = "\n")

print("\nSer_2 Shape: ", ser_2.shape)
print("\nSer_2 Values: ", ser_2.values)
print("\nSer_2 Values Type: ", type(ser_2.values))
print("\nSer_2 Index: ", ser_2.index)

ser_3 = pd.Series(lista_1, lista_2)
print("\nSérie 3 (duas listas):", ser_3, sep = "\n")

ser_4 = pd.Series(dicionario_1)
print("\nSérie 4 (dicionário):", ser_4, sep = "\n")

ser_5 = pd.Series(ndarray_1)
print("\nSérie 5 (ndarray):", ser_5, sep = "\n")

ser_6 = pd.Series(ndarray_1, lista_2)
print("\nSérie 6 (ndarray e lista):", ser_6, sep = "\n")

print("#"*100)

print("\nNumPy para lista: ", ndarray_1.tolist())
print("\nSérie para NumPy: ", ser_1.to_numpy())
print("\nSérie para lista: ", ser_1.to_list())

# Acessando os elementos

print("\nAcessando os elementos: ", ser_3[:3], sep = "\n")
print("Acessando os elementos: ", ser_3[-3:], sep = "\n")

print("\nAcessando os elementos: ", ser_3.head(3), sep = "\n")
print("Acessando os elementos: ", ser_3.tail(3), sep = "\n")

print("\nAcessando via rótulo: ", ser_3[0])
print("\nAcessando via rótulo: ", ser_3["I"])

print("\nIndex máximo: ", ser_3.idxmax())
print("\nIndex mínimo: ", ser_3.idxmin())

print("\nLoc: ", ser_3.loc["I":"III"], sep = "\n")
print("\nILoc: ", ser_3.iloc[0:3], sep = "\n")

ser_7 = pd.Series(lista_1)

# print("\nLoc: ", ser_7.loc["I":"III"], sep = "\n")
print("\nLoc: ", ser_7.loc[0:3], sep = "\n")
print("\nILoc: ", ser_7.iloc[0:3], sep = "\n")

i = 1_500_000
print(i)

dicionario_2 = {"I": 10, "II": 42, "III": 7, "V": 1_000_000}
dicionario_3 = {"I": 1, "II": 12, "III": 13, "IV": 0}

ser_8 = pd.Series(dicionario_2)
ser_9 = pd.Series(dicionario_3)

print("\nSérie 8 (dicionário):", ser_8, sep = "\n")
print("\nSérie 9 (dicionário):", ser_9, sep = "\n")
































