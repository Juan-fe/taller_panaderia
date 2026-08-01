"""Carga y preparación de datos para Panaderia."""
from pathlib import Path

import pandas as pd

# Ruta relativa a la raíz del proyecto — funciona en cualquier máquina.
RUTA_DATOS = Path(__file__).parent.parent / "data" / "datos_panaderia.csv"


def cargar_datos(ruta: Path = RUTA_DATOS) -> pd.DataFrame:
    """Carga el CSV y valida lo mínimo."""
    df = pd.read_csv(ruta)

    # El reflejo profesional: verificar tipos apenas se carga.
    columnas_esperadas = {"fecha", "dia_semana", "temperatura_c", "precio_promedio", "ventas_unidades"}
    faltantes = columnas_esperadas - set(df.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas en el CSV: {faltantes}")

    return df


def separar_variables(df: pd.DataFrame):
    """Devuelve (X, y) sin modificar el DataFrame recibido."""
    X = df[["temperatura_c", "precio_promedio", "es_finde"]].copy()
    y = df["ventas_unidades"].copy()
    return X, y
