# Taller Semana 1 — "Hazlo correr" 🥐

## La historia

Una panadería  en Bogotá contrató a un practicante de para predecir sus ventas
diarias. El practicante juró que su análisis funcionaba ("en mi máquina sí corre"),
entregó el proyecto... y renunció.

Hoy el proyecto es de ustedes. **No corre.** Su trabajo es convertirlo en un proyecto
profesional que corra en cualquier máquina.

## Reglas

- Trabajo **en parejas**
- **La IA está permitida para todo.** Pero recuerden: al final, 2 parejas al azar
  defienden su solución por micrófono. Y varios de los errores requieren mirar
  SUS datos y SUS tracebacks.
- Pidan ayuda al profesor cuando estén bloqueados.

## Entregable (al final de la sesión)

Un repositorio en Git que cumpla:

1. **Corre en máquina limpia** con exactamente estos comandos:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python src/train.py
   ```

2. **Estructura profesional** (la que construimos con CaféData):

   ```
   panaderia-ml/
   ├── data/
   │   └── datos_panaderia.csv
   ├── src/
   │   ├── data.py      (carga y limpieza)
   │   └── train.py     (entrenamiento y evaluación)
   ├── requirements.txt (con versiones fijadas)
   ├── README.md        (instrucciones reales de instalación)
   └── .gitignore
   ```

3. **Historial de Git**: mínimo 5 commits incrementales con mensajes descriptivos.
   Un solo commit llamado "final" cuenta una historia; 5+ commits pequeños cuentan otra.

## Pistas generales (sin espóiler)

- Lean los tracebacks **de abajo hacia arriba**. La última línea dice QUÉ falló;
  las de arriba dicen DÓNDE.
- Arreglen UN error a la vez y hagan commit. El siguiente error aparecerá solo.
- Acuérdense del quiz de hoy: los tipos mienten en silencio, y las versiones importan.
- `df.dtypes` es su amigo. Úsenlo apenas logren cargar el CSV.
- Si el código usa algo que "ya no existe" en pandas... pregúntense para qué
  versión fue escrito, y decidan: ¿adaptar el código o fijar la versión vieja?
  (Pista: adapten el código. En la defensa les preguntamos por qué.)

## Rúbrica

| Criterio | Peso | Cómo se evalúa |
|---|---|---|
| Corre en máquina limpia | 50% | El profesor clona y ejecuta los 4 comandos. Binario: corre o no corre. |
| Calidad y estructura | 30% | Separación en módulos, funciones sin efectos colaterales, rutas relativas, limpieza de datos justificada. |
| Proceso en Git + README | 20% | ≥5 commits incrementales con mensajes claros; README con instrucciones que funcionan. |

## Bonus (si terminan antes)

- Agreguen validación de columnas en `data.py` (que falle con un mensaje claro si
  el CSV no trae las columnas esperadas).
- ¿Cuántas filas perdieron en la limpieza? Impriman el reporte: filas cargadas,
  filas descartadas y por qué.
- Escriban en el README una sección "Decisiones" explicando qué hicieron con los
  datos faltantes y por qué.
