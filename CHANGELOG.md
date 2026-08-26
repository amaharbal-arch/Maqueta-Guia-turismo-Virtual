```markdown
# Historial de Cambios y Refactorización

## [0.1.0] - 2026-08

### Añadido
- Mapeo completo de las 21 comunas de Ñuble con descripciones y recursos de imagen asociados.
- Sistema de historial de navegación mediante `page.view_history`.
- Componentes de interacción para Cobquecura (Mapa, Galería, Audios, Historia, Hospedaje, Gastronomía).

### Cambiado / Refactorizado
- **Compatibilidad Flet v0.86+ / Python 3.14:**
  - Sustitución de `page.push_route()` por asignación directa de `page.route` para evitar corrutinas no esperadas.
  - Migración de módulos legacy de maquetación: `ft.margin` $\rightarrow$ `ft.Margin` y `ft.alignment` $\rightarrow$ `ft.Alignment`.
  - Reemplazo de inicializadores globales por `ft.run()`.
