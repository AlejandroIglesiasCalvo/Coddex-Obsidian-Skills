---
name: obsidian-links
description: Crear, validar y reparar wikilinks de Obsidian (links internos, enlaces a secciones, anclas ^bloque). Incluye verificación de existencia.
---

# Obsidian Links

## Cuándo usar
- Crear enlaces `[[Nota]]`, `[[Nota|Alias]]`
- Enlaces a secciones `[[Nota#Sección]]`
- Enlaces a bloques `[[Nota#^ancla]]`
- Auditoría y reparación de enlaces rotos

## Reglas
- Preferir **alias** legibles cuando el enlace aparece en texto.
- Para trazabilidad, preferir el nivel de precisión:
  1) bloque `#^ancla`  2) sección `#Sección`  3) nota

## Procedimiento
1. Localiza el destino (archivo real) y confirma que existe.
2. Si enlazas a sección: confirma encabezado exacto.
3. Si enlazas a bloque: confirma ancla `^...` existente.
4. Normaliza:
   - sin hashtags en tags de YAML
   - enlaces en YAML: entre comillas si contiene caracteres especiales

## Checklist
- [ ] El archivo objetivo existe
- [ ] La sección/ancla existe (si aplica)
- [ ] No se han creado enlaces “fantasma”

