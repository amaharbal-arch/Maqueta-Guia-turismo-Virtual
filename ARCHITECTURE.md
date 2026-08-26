---

`ARCHITECTURE.md`

```markdown
# Especificación de Arquitectura y Datos

## 📐 Mapa de Rutas y Navegación

Lógica de enrutamiento basada en `page.route` y control de pila de vistas (`page.views`):

- `/welcome`: Vista de aterrizaje inicial y presentación de marca.
- `/login`: Módulo de autenticación simulada (Interfaz de usuario).
- `/`: Dashboard principal con grilla adaptativa (`GridView`) de las 21 comunas.
- `/comuna`: Vista parametrizada según selección activa (e.g., Cobquecura con submenú interactivo).
- `/lugar`: Galería multimedia basada en grillas dinámicas de alto rendimiento.
- Vistas secundarias: `/favoritos`, `/config`, `/rutas`, `/audios`, `/juego`.

## 🗄️ Esquema de Datos Extraíble (JSON Schema)

Estructura de datos integrada en el prototipo, lista para migrar a base de datos relacional (PostgreSQL / Django ORM):

```json
{
  "comuna": {
    "type": "string",
    "properties": {
      "nombre": {"type": "string"},
      "imagen": {"type": "string"},
      "descripcion": {"type": "string"}
    }
  }
}
