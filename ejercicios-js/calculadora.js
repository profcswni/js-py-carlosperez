// Funcion para calcular operaciones basicas
function calcular(num1, num2, operacion) {
    switch (operacion) {
      case '+':
        return num1 + num2;
      case '-':
        return num1 - num2;
      case '*':
        return num1 * num2;
      case '/':
        return num2 === 0 ? "Error: división por cero" : num1 / num2;
      default:
        return "Operación no válida";
    }
}

// Array de números para pruebas. Genera aleatoriamente 100 números entre 0 y 100
const numeros = Array.from({ length: 10 }, () => Math.floor(Math.random() * 100));
const operaciones = ['+', '-', '*', '/'];

// Función para mostrar resultados en formato tabla
function mostrarResultados(resultados) {
    console.table(resultados);
}

// Pruebas con diferentes tipos de ciclos
console.group('🧮 Calculadora Avanzada');

// 1. Usando for tradicional
console.info('1️⃣ Operaciones con for tradicional:');
const resultadosFor = [];
for (let i = 0; i < numeros.length; i += 2) {
    for (let j = 0; j < operaciones.length; j++) {
        resultadosFor.push({
            'Número 1': numeros[i],
            'Número 2': numeros[i + 1],
            'Operación': operaciones[j],
            'Resultado': calcular(numeros[i], numeros[i + 1], operaciones[j])
        });
    }
}
mostrarResultados(resultadosFor);
console.groupEnd();