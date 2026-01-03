---
name: obsidian-mermaid
description: Crear diagramas Mermaid compatibles con Obsidian (flowchart, sequence, gantt). Evita errores comunes y produce diagramas simples y mantenibles.
---

# Obsidian Mermaid

## Cuándo usar
- Diagramas de arquitectura, flujos, procesos, decisiones
- Resúmenes visuales dentro de notas

## Reglas prácticas
- Mantén el diagrama **pequeño** y por bloques.
- Evita Markdown dentro de labels.
- Prefiere `flowchart TB` para lecturas verticales.
- Nombres de nodos simples; textos descriptivos en etiquetas.

## Procedimiento
1. Define objetivo del diagrama (qué decisión explica).
2. Enumera nodos y relaciones en texto.
3. Genera Mermaid en bloque:
   ```mermaid
   flowchart TB
     A[Inicio] --> B{Decisión}
     B -->|Sí| C[Acción]
     B -->|No| D[Alternativa]
   ```
4. Revisa que compila y que no hay caracteres problemáticos.

## Salida
- Inserta el bloque Mermaid en la sección correcta.
- Si el diagrama depende de una decisión documental, enlaza a las notas fuente.

