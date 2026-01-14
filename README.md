# 🫧 Ordenamiento Burbuja (Bubble Sort) — Guía para Principiantes

El **ordenamiento burbuja** es un algoritmo sencillo para ordenar listas.  
Funciona comparando **elementos vecinos** e intercambiándolos si están en el orden incorrecto, haciendo que los valores grandes “suban” hacia el final como burbujas 🫧.

---

## ✅ ¿Cuándo usar Bubble Sort?

📌 Úsalo cuando:
- Estás aprendiendo algoritmos.
- Tu lista es pequeña.
- Quieres practicar comparaciones e intercambios.

🚫 Evítalo cuando:
- Trabajas con listas grandes (se vuelve lento).

---

## 🧠 ¿Cómo funciona? (explicación simple)

Bubble Sort repite varias **pasadas** sobre la lista:

1. Compara el elemento `actual` con el `siguiente`.
2. Si `actual > siguiente`, los intercambia.
3. Al terminar una pasada, el número más grande queda al final.
4. Repite hasta que ya no existan intercambios.

---

## 🧪 Ejemplo paso a paso

Lista inicial:  
`[5, 1, 4, 2]`

**Pasada 1**
- (5, 1) → intercambio → `[1, 5, 4, 2]`
- (5, 4) → intercambio → `[1, 4, 5, 2]`
- (5, 2) → intercambio → `[1, 4, 2, 5]` ✅ el mayor ya quedó al final

**Pasada 2**
- (1, 4) → ok → `[1, 4, 2, 5]`
- (4, 2) → intercambio → `[1, 2, 4, 5]`

**Pasada 3**
- No hay intercambios ✅ entonces ya está ordenado

Resultado:  
`[1, 2, 4, 5]`

---

## 🧩 Pseudocódigo (para entender la lógica)

```text
para i desde 0 hasta n-1:
    hubo_intercambio = falso

    para j desde 0 hasta n-2-i:
        si lista[j] > lista[j+1]:
            intercambiar lista[j] con lista[j+1]
            hubo_intercambio = verdadero

    si no hubo_intercambio:
        detener (ya está ordenado)
