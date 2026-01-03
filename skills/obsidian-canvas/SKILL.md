---
name: obsidian-canvas
description: "Editar o generar archivos de Obsidian Canvas (.canvas JSON) de forma segura: nodos, conexiones, posiciones. Evita corromper el JSON."
---

# Obsidian Canvas

## CuÃ¡ndo usar
- Crear/editar un `.canvas`
- AÃ±adir nodos (nota, texto, enlace) y conexiones
- Reorganizar posiciones sin perder referencias

## Guardrails
- Un `.canvas` es **JSON**: nunca introduzcas comentarios ni trailing commas.
- No cambies IDs existentes si el objetivo es ediciÃ³n incremental.
- MantÃ©n cambios localizados.

## Procedimiento
1. Lee el JSON completo.
2. Identifica:
   - `nodes[]` (id, type, x/y/width/height, file/text/urlâ€¦)
   - `edges[]` (fromNode, toNode, labelâ€¦)
3. Aplica cambios:
   - aÃ±adir nodo -> generar `id` Ãºnico
   - aÃ±adir edge -> referencia IDs existentes
4. Valida que sigue siendo JSON vÃ¡lido.

## Entrega
- Devuelve el `.canvas` actualizado.
- Incluye un resumen: nodos aÃ±adidos/modificados, edges aÃ±adidas.


