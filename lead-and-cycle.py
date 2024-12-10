import csv
import pandas as pd

# Caminho para o arquivo CSV usando string raw
csv_file = r'C:\Users\MicaelPereira\Downloads\desenvolvimentos\bugs\travel-10.csv'

# Lista para armazenar os itens convertidos
new_items = []

# Abrindo o arquivo CSV e lendo seus dados
with open(csv_file, mode='r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Adicionando cada linha como um dicionário à lista
        new_items.append({
            "ID": row["ID"],
            "Tipo de Solução": row["Tipo de Solução"],
            "Work Item Type": row["Work Item Type"],
            "Title": row["Title"],
            "Assigned To": row["Assigned To"],
            "Created Date": row["Created Date"],
            "Closed Date": row["Closed Date"],
            "State": row["State"],
            "Tags": row["Tags"],
            "Closed By": row["Closed By"],
            "Resolved By": row["Resolved By"],
            "Created By": row["Created By"],
            "Activated By": row["Activated By"],
            "Activated Date": row["Activated Date"],
            "Area Path": row["Area Path"]
        })

# Exibindo o resultado (opcional)
# print(new_items)

# Converta os dados para um DataFrame
df = pd.DataFrame(new_items)

# Converta as datas para o formato datetime
df["Created Date"] = pd.to_datetime(df["Created Date"], format="%d/%m/%Y %H:%M:%S")
df["Activated Date"] = pd.to_datetime(df["Activated Date"], format="%d/%m/%Y %H:%M:%S")
df["Closed Date"] = pd.to_datetime(df["Closed Date"], format="%d/%m/%Y %H:%M:%S")

# Calcule o cycle time
df["Cycle Time"] = (df["Closed Date"] - df["Activated Date"]).dt.days
df["Lead Time"] = (df["Closed Date"] - df["Created Date"]).dt.days

# Calcule a média do cycle time
average_cycle_time = df["Cycle Time"].mean()
print('Cycle time')
print(average_cycle_time)

average_lead_time = df["Lead Time"].mean()
print('Lead time')
print(average_lead_time)