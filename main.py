import pandas as pd
from helpers.arbolesAnt import crearTabla

tabla=pd.read_csv("./data/Siembras.csv")
arboleSembrados=tabla.query('Ciudad =="Santa Fe de Antioquia" and Arboles > 250')

crearTabla(arboleSembrados,"tabla")
