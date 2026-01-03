---
name: obsidian-vault-ops
description: Operaciones seguras sobre un vault de Obsidian: buscar, leer, escribir, mover y validar sin romper enlaces. Incluye patrones para evitar alucinaciones.
---

# Obsidian Vault Ops

## Cuándo usar
Usa esta skill para **operar archivos del vault**: localizar notas, leerlas de forma fiable, crear/editar/mover, y validar que no rompes enlaces.

## Guardrails (obligatorio)
1. **Lee primero**: antes de concluir, abre el contenido completo de los archivos relevantes (no solo metadatos).
2. Si no puedes leer un archivo requerido, responde **“no consta en la bóveda”** o pide el contenido.
3. No renombres/muevas masivamente sin un plan reversible.

## Procedimiento recomendado
1. **Buscar** candidatos:
   - por nombre de archivo, encabezados, palabras clave, tags.
2. **Leer**:
   - nota principal + notas enlazadas de primer nivel si son necesarias para la respuesta.
3. **Operar** (si aplica):
   - crear/editar con cambios mínimos y verificables.
4. **Validar**:
   - enlaces `[[...]]` siguen resolviendo
   - frontmatter no quedó roto
   - no se han tocado `_templates/` sin permiso

## Salida
- Si es una respuesta: incluye **Fuentes internas** con wikilinks precisos cuando la trazabilidad sea necesaria.
- Si son cambios: resume qué archivos se tocaron y por qué (sin inventar).


