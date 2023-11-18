import numpy as np 

# Âge , revenus , nombre d'enfants
hugo = [21, 1400, 0]
richard = [54, 2800, 2]
emilie = [27, 3700, 3]
tableau = [hugo, richard, emilie]


# Calcul matriciel

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 10], [15, 20]])
C = np.array([[2, 4, 6], [8, 10, 12]])

D = A+B


E = A @ C

# Revenu, mensualité, âge

hugo = [1300, 400, 23]
richard = [1700, 560, 24]
emilie = [2500, 900, 30]
gaspard = [3000, 1000, 22]
yohann = [2400, 700, 28]
chloe = [3000, 700, 34]
matthieu = [3500, 900, 35] 
luc = [4000, 1200, 33]
rachel = [3300, 950, 27] 
maude = [1050, 600, 25]

tableau = [hugo, richard, emilie, gaspard, yohann, chloe, matthieu, luc, rachel, maude]

data = np.array(tableau)
print("Data : ", data)
print("Data - premier array, première colonne : " ,data[0, 0])
print("Data - première ligne) :" , data[0, :])
print("Data - première colonne : ",  data[:, 0])
print("Data - toutes les entrées qui ont max 25 ans : " , data[data[:, 2] <= 25])

fred = [1750, 700, 27]
