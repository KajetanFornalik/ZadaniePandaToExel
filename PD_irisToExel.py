import pandas as pd

Iris = pd.read_csv("C:/Users/Kajtek/OneDrive/Pulpit/zadanie1/iris.csv")
print(Iris['variety'].unique())
species = Iris['variety'].unique()

with pd.ExcelWriter('Iris2.xlsx') as writer:
    for spec in species:
        print(Iris[Iris['variety'] == spec])
        Iris[Iris['variety'] == spec].to_excel(writer, sheet_name= spec)


