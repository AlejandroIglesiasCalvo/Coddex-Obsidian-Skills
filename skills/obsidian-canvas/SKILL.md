---
name: obsidian-canvas
description: Editar o generar archivos de Obsidian Canvas (.canvas JSON) de forma segura: nodos, conexiones, posiciones. Evita corromper el JSON.
---

# Obsidian Canvas

## Cuándo usar
- Crear/editar un `.canvas`
- Añadir nodos (nota, texto, enlace) y conexiones
- Reorganizar posiciones sin perder referencias

## Guardrails
- Un `.canvas` es **JSON**: nunca introduzcas comentarios ni trailing commas.
- No cambies IDs existentes si el objetivo es edición incremental.
- Mantén cambios localizados.

## Procedimiento
1. Lee el JSON completo.
2. Identifica:
   - `nodes[]` (id, type, x/y/width/height, file/text/url…)
   - `edges[]` (fromNode, toNode, label…)
3. Aplica cambios:
   - añadir nodo -> generar `id` único
   - añadir edge -> referencia IDs existentes
4. Valida que sigue siendo JSON válido.

## Entrega
- Devuelve el `.canvas` actualizado.
- Incluye un resumen: nodos añadidos/modificados, edges añadidas.

