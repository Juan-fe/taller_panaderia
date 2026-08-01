# analisis panaderia - version final FINAL (esta si funciona)
# hecho por el practicante, no tocar
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

from data import cargar_datos, separar_variables

print("cargando datos...")
def entrenar():
    df = cargar_datos()
    print("datos cargados:", len(df), "filas")

    # resumen de ventas por dia de la semana
    resumen = (
    df.groupby("dia_semana", as_index=False)
      .agg(ventas_promedio=("ventas_unidades", "mean"))
      .rename(columns={"dia_semana": "dia"})
    )

    print("--- resumen por dia ---")
    print(resumen)

    # variable: es fin de semana?
    df["es_finde"] = (
        df["dia_semana"]
        .isin(["sábado", "domingo"])
        .astype(int)
    )

    # entrenar el modelo
    X, y = separar_variables(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    pred = modelo.predict(X_test)
    print("MAE:", mean_absolute_error(y_test, pred))
    print("listo!!")

if __name__ == "__main__":
    entrenar()