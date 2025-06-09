# Ejercicios JavaScript y Python

## 📈 Estado del Proyecto

[![Verificaciones de GitHub Actions](https://github.com/profcswni/js-py-carlosperez/actions/workflows/ci.yml/badge.svg)](https://github.com/profcswni/js-py-carlosperez/actions/workflows/ci.yml)
[![Forks](https://img.shields.io/github/forks/profcswni/js-py-carlosperez?style=social)](https://github.com/profcswni/js-py-carlosperez/network/members)

Este repositorio contiene una colección de ejercicios prácticos en JavaScript y Python, junto con un sistema automatizado de verificación y ejecución mediante GitHub Actions.

## 📁 Estructura del Repositorio

```
.
├── ejercicios-js/     # Ejercicios en JavaScript
├── ejercicios-py/     # Ejercicios en Python
└── .github/
    └── workflows/     # Configuración de GitHub Actions
```

## 🚀 Flujo de Trabajo

El repositorio utiliza GitHub Actions para automatizar la verificación y ejecución de los ejercicios. El proceso se divide en tres etapas:

1. **Verificación de Archivos** (`filenames.yml`)
   - Lista todos los archivos JavaScript y Python encontrados
   - Muestra un check (✅) por cada archivo válido

2. **Ejecución de Archivos** (`autorun.yml`)
   - Ejecuta cada archivo JavaScript y Python
   - Muestra el resultado de la ejecución
   - Indica éxito (✅) o error (❌) para cada archivo

3. **Pipeline Principal** (`CI.yml`)
   - Orquesta el proceso completo
   - Verifica los archivos primero
   - Si la verificación es exitosa, ejecuta los archivos

## 📝 Convenciones de Nombres

- **JavaScript**: Archivos con extensión `.js`
- **Python**: Archivos con extensión `.py`

## 🛠️ Requisitos

### JavaScript
- Node.js versión 20 (LTS)

### Python
- Python 3.11
- Dependencias:
  - tabulate==0.9.0

## 🔄 Proceso de desarrollo

1. Crea o modifica archivos en las carpetas correspondientes
2. Haz commit de tus cambios
3. Push al repositorio
4. GitHub Actions ejecutará automáticamente:
   - Verificación de archivos
   - Ejecución de los ejercicios

## 📊 Resultados

Los resultados de la ejecución se mostrarán en:
- La pestaña "Actions" de GitHub
- Los checks en cada commit
- El resumen de ejecución en el pull request

## ⚠️ Notas importantes

- Cada archivo debe ser ejecutable de forma independiente
- Los errores en cualquier archivo detendrán el proceso
- Se recomienda probar los archivos localmente antes de hacer push

## 🔍 Verificación Local

### JavaScript
```bash
cd ejercicios-js
node ejercicio1.js
```

### Python
```bash
cd ejercicios-py
python ejercicio1.py
```

## 🤝 Contribución o realizar su propio repositorio

1. Haz un fork de este repositorio
2. Clona el fork realizado y completa los ejercicios

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles. 