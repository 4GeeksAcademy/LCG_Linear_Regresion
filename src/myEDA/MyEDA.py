import pandas as pd

class MyEDA:
    @staticmethod
    def explore(df):
        # Mostrar información básica
        print(f"\nRows (before cleanup): {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")

        # Detectar duplicados
        duplicates = df[df.duplicated()]
        if not duplicates.empty:
            print("\n🔴 Duplicate row(s) found and removed:\n")
            print(duplicates)
            df = df.drop_duplicates()
            print(f"\n✅ New shape after removing duplicates: {df.shape}")

        # Crear tabla resumen
        summary = pd.DataFrame({
            "Non-Null Count": df.count(),
            "Null Count": df.isnull().sum(),
            "Data Type": df.dtypes
        })
        summary["Data Category"] = summary["Data Type"].apply(lambda x: "Categorical" if x == "object" else "Numeric")

        print("\n+----------+----------------+------------+-----------+---------------+")
        print("|          | Non-Null Count | Null Count | Data Type | Data Category |")
        print("+----------+----------------+------------+-----------+---------------+")
        for index, row in summary.iterrows():
            print(f"| {index:<8} | {row['Non-Null Count']:>14} | {row['Null Count']:>10} | {str(row['Data Type']):>9} | {row['Data Category']:>13} |")
        print("+----------+----------------+------------+-----------+---------------+")

        # Separar variables categóricas y numéricas
        categorical = list(df.select_dtypes(include=["object"]).columns)
        numerical = list(df.select_dtypes(exclude=["object"]).columns)

        return categorical, numerical, df
