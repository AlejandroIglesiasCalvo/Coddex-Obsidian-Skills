---
name: obsidian-mermaid
description: "Crear diagramas Mermaid compatibles con Obsidian (flowchart, sequence, gantt). Evita errores comunes y produce diagramas simples y mantenibles."
---

# Obsidian Mermaid

## CuÃ¡ndo usar
- Diagramas de arquitectura, flujos, procesos, decisiones
- ResÃºmenes visuales dentro de notas

## Reglas prÃ¡cticas
- MantÃ©n el diagrama **pequeÃ±o** y por bloques.
- Evita Markdown dentro de labels.
- Prefiere `flowchart TB` para lecturas verticales.
- Nombres de nodos simples; textos descriptivos en etiquetas.

## Procedimiento
1. Define objetivo del diagrama (quÃ© decisiÃ³n explica).
2. Enumera nodos y relaciones en texto.
3. Genera Mermaid en bloque:
   ```mermaid
   flowchart TB
     A[Inicio] --> B{DecisiÃ³n}
     B -->|SÃ­| C[AcciÃ³n]
     B -->|No| D[Alternativa]
   ```
4. Revisa que compila y que no hay caracteres problemÃ¡ticos.

## Salida
- Inserta el bloque Mermaid en la secciÃ³n correcta.
- Si el diagrama depende de una decisiÃ³n documental, enlaza a las notas fuente.


