---
name: obsidian-links
description: "Crear, validar y reparar wikilinks de Obsidian (links internos, enlaces a secciones, anclas ^bloque). Incluye verificaciÃ³n de existencia."
---

# Obsidian Links

## CuÃ¡ndo usar
- Crear enlaces `[[Nota]]`, `[[Nota|Alias]]`
- Enlaces a secciones `[[Nota#SecciÃ³n]]`
- Enlaces a bloques `[[Nota#^ancla]]`
- AuditorÃ­a y reparaciÃ³n de enlaces rotos

## Reglas
- Preferir **alias** legibles cuando el enlace aparece en texto.
- Para trazabilidad, preferir el nivel de precisiÃ³n:
  1) bloque `#^ancla`  2) secciÃ³n `#SecciÃ³n`  3) nota

## Procedimiento
1. Localiza el destino (archivo real) y confirma que existe.
2. Si enlazas a secciÃ³n: confirma encabezado exacto.
3. Si enlazas a bloque: confirma ancla `^...` existente.
4. Normaliza:
   - sin hashtags en tags de YAML
   - enlaces en YAML: entre comillas si contiene caracteres especiales

## Checklist
- [ ] El archivo objetivo existe
- [ ] La secciÃ³n/ancla existe (si aplica)
- [ ] No se han creado enlaces â€œfantasmaâ€


