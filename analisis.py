# analisis panaderia - version final FINAL (esta si funciona)
# hecho por el practicante, no tocar
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

print("cargando datos...")
df = pd.read_csv("C:\\Users\\practicante\\Desktop\\proyecto_panaderia\\datos_panaderia.csv")
print("datos cargados:", len(df), "filas")

# resumen de ventas por dia de la semana
resumen = pd.DataFrame()
for dia in df["dia_semana"].unique():
    sub = df[df["dia_semana"] == dia]
    resumen = resumen.append(
        {"dia": dia, "ventas_promedio": sub["ventas_unidades"].mean()},
        ignore_index=True,
    )
print("--- resumen por dia ---")
print(resumen)

# variable: es fin de semana?
df["es_finde"] = 0
for i in range(len(df)):
    if df["dia_semana"][i] == "sábado" or df["dia_semana"][i] == "domingo":
        df["es_finde"][i] = 1

# entrenar el modelo
X = df[["temperatura_c", "precio_promedio", "es_finde"]]
y = df["ventas_unidades"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

pred = modelo.predict(X_test)
print("MAE:", mean_absolute_error(y_test, pred))
print("listo!!")
