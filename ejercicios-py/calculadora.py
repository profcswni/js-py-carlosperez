from tabulate import tabulate
from typing import List, Dict, Any
import sys
# Definir la funcion para realizar el cálculo
def calcular(num1: float, num2: float, operacion: str) -> float:
    if operacion == '+':
        return num1 + num2
    elif operacion == '-':
        return num1 - num2
    elif operacion == '*':
        return num1 * num2
    elif operacion == '/':
        return "Error: división por cero" if num2 == 0 else num1 / num2
    else:
        return "Operación no válida"

def mostrar_resultados(resultados: List[Dict[str, Any]], titulo: str) -> None:
    print(f"\n{titulo}")
    print(tabulate(resultados, headers="keys", tablefmt="grid"))
    sys.stdout.flush()  # Forzar la salida inmediata

# Datos para pruebas
numeros = [5, 3, 10, 0, 2, 4, 10, 2]
operaciones = ['+', '-', '*', '/']

print("🧮 Calculadora avanzada en Python\n")
sys.stdout.flush()

# 1. Usando for tradicional
print("Iniciando sección 1...")
resultados_for = []
for i in range(0, len(numeros), 2):
    for op in operaciones:
        if i + 1 < len(numeros):
            resultados_for.append({
                'Número 1': numeros[i],
                'Número 2': numeros[i + 1],
                'Operación': op,
                'Resultado': calcular(numeros[i], numeros[i + 1], op)
            })
mostrar_resultados(resultados_for, "1️⃣ Operaciones con for tradicional:")

print("\n✅ Ejecución completada")
sys.stdout.flush()

