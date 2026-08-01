"""Carga y preparación de datos para Panaderia."""
from pathlib import Path

import pandas as pd

# Ruta relativa a la raíz del proyecto — funciona en cualquier máquina.
RUTA_DATOS = Path(__file__).parent.parent / "data" / "datos_panaderia.csv"


def cargar_datos(ruta: Path = RUTA_DATOS) -> pd.DataFrame:
    """Carga el CSV y valida lo mínimo."""
    df = pd.read_csv(ruta,
    encoding="latin-1",
    sep=";")

    # El reflejo profesional: verificar tipos apenas se carga.
    columnas_esperadas = {"fecha", "dia_semana", "temperatura_c", "precio_promedio", "ventas_unidades"}
    faltantes = columnas_esperadas - set(df.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas en el CSV: {faltantes}")
    
    # Imputación de la mediana para valores SIN DATO en la variable temperatura
    print(df.info())
    print(df.isna().sum())

    for columna in df.columns:
        print(f"\n--- {columna} ---")
        print(df[columna].value_counts(dropna=False).head(20))

    # Convertir textos no numéricos a NaN
    df["temperatura_c"] = pd.to_numeric(
        df["temperatura_c"],
        errors="coerce"
    )

    # Calcular la mediana sin considerar los NaN
    mediana_temperatura = df["temperatura_c"].median()

    # Imputar los valores faltantes
    df["temperatura_c"] = df["temperatura_c"].fillna(mediana_temperatura)    


    return df


def separar_variables(df: pd.DataFrame):
    """Devuelve (X, y) sin modificar el DataFrame recibido."""
    X = df[["temperatura_c", "precio_promedio", "es_finde"]].copy()
    y = df["ventas_unidades"].copy()
    return X, y
