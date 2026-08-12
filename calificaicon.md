# taller_panaderia — Taller Semana 1: "Hazlo correr" 🥐

Repo: [github.com/Juan-fe/taller_panaderia](https://github.com/Juan-fe/taller_panaderia)

Rúbrica: Corre en máquina limpia (50% · 2.5 pts) · Calidad y estructura (30% · 1.5 pts) · Proceso en Git + README (20% · 1.0 pt) · Bonus (+0.2 máx si aplica). Escala final: 0–5.

**Nota final: 4.45 / 5.0**

| Corre limpio | Calidad/estructura | Git+README | Bonus |
|---|---|---|---|
| 2.35 / 2.5 | 1.2 / 1.5 | 0.7 / 1.0 | +0.2 |

---

### 1. Corre en máquina limpia — 2.35 / 2.5 ✅
Con Python 3.11 los 4 comandos exactos corren sin errores:

```
cargando datos...
...
Cantidad de filas con valores 'SIN DATO'
           columna  sin_dato
0            fecha         0
1       dia_semana         0
2    temperatura_c         7
3  precio_promedio         0
4  ventas_unidades         0

datos cargados: 90 filas
--- resumen por dia ---
...
MAE: 18.70374650324792
listo!!
```

Con Python 3.10 (el `python` por defecto en esta máquina) `pip install -r requirements.txt` falla: `pandas==3.0.2` no tiene versión compatible ahí. Igual que en otras entregas con estas mismas versiones, funciona en cualquier Python 3.11 o superior sin restricción de tope — algo razonablemente común — pero el README no lo menciona en ningún lado. **(-0.15)**

### 2. Calidad y estructura — 1.2 / 1.5 ✅
**Bien:** `cargar_datos()` valida columnas, castea `temperatura_c` con `pd.to_numeric(errors="coerce")`, e imputa con la mediana. El escaneo de `"SIN DATO"` revisa **todas** las columnas, no solo `temperatura_c` — más general que solo asumir dónde está el problema. `es_finde` vectorizado con `.isin().astype(int)`, sin loops ni asignación encadenada. El resumen por día usa `groupby` + `agg`, sin rastro del `.append()` original.

**Se bajó nota por:**
- **`print("cargando datos...")` está al nivel superior del módulo `train.py`**, fuera de `entrenar()` — se ejecuta con solo importar el archivo, no solo al llamar la función. **(-0.15)**
- **`train.py` conserva el comentario de cabecera original del practicante** (`# hecho por el practicante, no tocar`), pese a que el archivo fue reescrito casi por completo. **(-0.1)**
- **`print(df.info())` imprime un `None` de más**: `df.info()` ya imprime su salida directamente y devuelve `None`; envolverlo en `print()` agrega una línea `None` extra a la consola. **(-0.05)**

### 3. Proceso en Git + README — 0.7 / 1.0 ⚠️
**Bien:** 8 commits con progreso incremental real y mensajes descriptivos (`Correción codificación`, `Ajuste append y asignación fin de semana`, `Separación lógica de carga y entrenamiento`...) — supera el mínimo de 5. La sección "Ajustes" del README explica en detalle los 11 cambios realizados, incluyendo que revisaron el traceback hasta el final para encontrar la sugerencia de pandas sobre la asignación de `es_finde`. La sección "Decisiones" justifica bien la mediana sobre la media.

**Se bajó nota por:**
- **El README no tiene ninguna sección de instalación o ejecución** — no aparece en ningún lado `python -m venv .venv`, activación, `pip install` ni `python src/train.py`. El criterio pide explícitamente "instrucciones que funcionan"; aquí no hay ninguna instrucción, aunque el proceso real sí sea el estándar. **(-0.3)**

### Bonus completados — +0.2 🎉
1. **Validación de columnas**: `cargar_datos()` valida columnas esperadas y lanza `ValueError` claro si falta alguna.
2. **Reporte de limpieza**: imprime cuántas filas tienen `"SIN DATO"` por columna (y aclara en el README que como se imputó con la mediana, las 90 filas se usaron para entrenar).
3. **Sección "Decisiones" en el README**: justifica la mediana sobre la media por robustez ante posibles brechas grandes entre datos.

### Resumen para el estudiante
La parte técnica está bien resuelta: la vectorización de `es_finde`, el escaneo genérico de `"SIN DATO"` en todas las columnas y la imputación con mediana muestran buen criterio. Lo que más pesa en la nota es que el README no incluye ninguna instrucción de instalación o ejecución — solo explica qué se cambió, no cómo correr el proyecto. Para la próxima entrega: agreguen los 4 comandos de instalación al README, saquen el `print("cargando datos...")` de fuera de `entrenar()`, actualicen el comentario de cabecera de `train.py`, y cambien `print(df.info())` por solo `df.info()` (sin el `print` exterior).
