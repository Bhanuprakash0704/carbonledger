import pandas as pd


def parse_sap_csv(file):

    df = pd.read_csv(file)

    records = []

    for _, row in df.iterrows():

        quantity = float(row['MENGE'])

        suspicious = quantity < 0

        record = {
            "category": "Fuel",
            "scope": 1,
            "quantity": quantity,
            "unit": row['MEINS'],
            "normalized_quantity": quantity,
            "normalized_unit": "L",
            "co2e": quantity * 2.68,
            "suspicious": suspicious
        }

        records.append(record)

    return records