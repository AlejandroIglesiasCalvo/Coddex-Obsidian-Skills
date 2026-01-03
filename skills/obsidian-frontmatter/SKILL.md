---
name: obsidian-frontmatter
description: Aplicar reglas consistentes de YAML frontmatter en Obsidian: un bloque, claves estándar, fechas YYYY-MM-DD, tags en lista, comillas cuando proceda.
---

# Obsidian Frontmatter (YAML)

## Cuándo usar
- Añadir o corregir frontmatter
- Normalizar propiedades para Dataview
- Evitar errores YAML (comillas, duplicados, tipos)

## Reglas mínimas
1. **Un único bloque** YAML al inicio (`---` ... `---`) con una línea en blanco después.
2. Claves **en minúscula** y consistentes.
3. Fechas: `YYYY-MM-DD` (o datetime ISO si la nota ya usa hora).
4. `tags` siempre como lista:
   ```yaml
   tags:
     - area
     - tipo
   ```
5. Valores con `:`, `#`, enlaces `[[...]]` o números “sospechosos”: **entre comillas**.

## Procedimiento
1. Lee el archivo completo para no duplicar propiedades existentes.
2. Identifica el set de propiedades usado en el vault (no inventes si hay estándar previo).
3. Aplica cambios mínimos:
   - evita renombrar claves si rompe Dataview sin confirmación
4. Valida YAML:
   - sin tabs
   - indentación consistente (2 espacios)
   - sin duplicados de clave

## Salida
- Reporta qué claves se añadieron/cambiaron.
- Si detectas incertidumbre sobre el estándar del vault, detente y pregunta.

