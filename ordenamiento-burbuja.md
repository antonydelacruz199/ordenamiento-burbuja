# 🫧 Bubble Sort OOP (Python) — Aplicación de Ordenamiento Burbuja

Aplicación en **Python orientado a objetos** que implementa el algoritmo de **ordenamiento burbuja (Bubble Sort)** para ordenar listas de números (u otros elementos comparables).

---

## 📌 ¿Qué es Bubble Sort?

Bubble Sort ordena una lista comparando **pares de elementos vecinos** e intercambiándolos si están en el orden incorrecto.  
En cada pasada, el valor más grande “sube” al final como una burbuja 🫧.

---

## 🖼️ Visual rápido (ASCII)


---

## ✅ Características

- Programación **orientada a objetos** (clase `BubbleSorter`)
- Soporta:
  - Orden ascendente ✅
  - Orden descendente ✅
  - Modo **verbose** para ver intercambios y pasadas ✅
- Optimización: si una pasada no hace intercambios, el algoritmo se detiene 🚀

---

## 🧩 Estructura sugerida del proyecto


---

## 🐍 Código: `bubble_sorter.py`

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import List, TypeVar

T = TypeVar("T")


@dataclass
class BubbleSorter:
    """
    Implementa Bubble Sort con soporte para:
    - ascendente / descendente
    - modo verbose (paso a paso)
    """

    verbose: bool = False

    def sort(self, items: List[T], reverse: bool = False) -> List[T]:
        """
        Ordena la lista usando Bubble Sort.

        :param items: Lista de elementos comparables (números, strings, etc.)
        :param reverse: Si True, ordena de mayor a menor
        :return: Una nueva lista ordenada (no modifica la original)
        """
        arr = list(items)  # copiamos para no modificar la lista original
        n = len(arr)

        if self.verbose:
            print("📌 Lista inicial:", arr)
            print("🔽 Orden:", "descendente" if reverse else "ascendente")
            print("-" * 50)

        for i in range(n):
            swapped = False

            # Cada pasada deja el elemento correcto al final (según reverse)
            for j in range(0, n - 1 - i):
                if self._should_swap(arr[j], arr[j + 1], reverse):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

                    if self.verbose:
                        print(
                            f"   🔁 swap pos {j} y {j + 1} -> {arr}"
                        )

            if self.verbose:
                print(f"✅ Fin de pasada {i + 1}: {arr}")

            # Optimización: si no hubo intercambios, ya está ordenado
            if not swapped:
                if self.verbose:
                    print("🚀 No hubo intercambios: lista ordenada.")
                break

        return arr

    @staticmethod
    def _should_swap(a: T, b: T, reverse: bool) -> bool:
        """
        Define si se debe intercambiar el par (a, b) según el tipo de orden.
        """
        if reverse:
            return a < b
        return a > b

