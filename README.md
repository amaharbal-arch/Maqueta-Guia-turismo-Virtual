# Guía Turística Regional de Ñuble — UI/UX Interactive Prototype

> **Status:** `[Functional UI/UX Prototype / Proof of Concept]`
> **Stack:** Python 3.14 | Flet v0.86+ (Flutter Engine)

Prototipo interactivo desarrollado para validar la arquitectura de navegación, la jerarquía visual y la distribución de contenido para la plataforma turística de las 21 comunas de la Región de Ñuble.

## 🎯 Objetivos del Prototipo
- Validar el flujo de navegación cliente entre vistas dinámicas (`/welcome`, `/login`, `/`, `/comuna`, `/lugar`).
- Probar la respuesta del layout responsivo con grillas dinámicas de 21 entidades territoriales.
- Definir la estructura base de datos de comunas y recursos multimedia para la futura API REST.

## 🛠️ Requisitos e Instalación

### Requisitos previos
- Python 3.10+ (Probado y optimizado para Python 3.14)
- Dependencias indicadas en `requirements.txt`

### Instalación y Ejecución
```bash
# 1. Clonar el repositorio
git clone [https://github.com/tu-usuario/nuble-virtual-prototype.git](https://github.com/tu-usuario/nuble-virtual-prototype.git)
cd nuble-virtual-prototype

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar la aplicación
python main.py
