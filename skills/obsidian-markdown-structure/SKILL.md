---
name: obsidian-markdown-structure
description: Estandarizar estructura Markdown en Obsidian sin romper Dataview/Templater ni tablas: headings, listas, bloques de código, separadores.
---

# Obsidian Markdown Structure

## Cuándo usar
- Reorganizar una nota para que sea legible
- Limpiar formato (listas, encabezados, espacios)
- Preparar notas para revisión/publicación

## Guardrails
- **No rompas**:
  - bloques Dataview (` ```dataview `)
  - Templater (`<% ... %>`)
  - código y fences
  - tablas (mantener pipes)
- Evita cambios cosméticos masivos si no aportan valor.

## Procedimiento
1. Lee nota completa.
2. Propón estructura:
   - H1 (título) -> H2 (secciones) -> H3 (subsecciones)
3. Mueve contenido a secciones con cambios mínimos.
4. Valida que los bloques especiales siguen intactos.

## Entrega
- Deja el contenido “listo para trabajar”: claro, navegable, sin duplicidad.

