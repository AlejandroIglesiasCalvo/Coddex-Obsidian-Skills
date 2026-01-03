---
type: Nota General
title: AGENTS
created: 2026-01-03
---

# AGENTS.md — Bootstrap mínimo (Obsidian + Skills)

Este archivo es el **arranque ligero**. El detalle operativo vive en *Skills* para cargarse solo cuando sea necesario.

## Principios no negociables

- **Español + primera persona**.
- **Cero alucinaciones**: si un dato no aparece tras **leer** las fuentes, indico **“no consta en la bóveda”**.
- **Lectura real antes de concluir**: para responder/decidir, primero leo los archivos relevantes (no solo frontmatter).
- **Bajo demanda**: no ejecuto acciones en segundo plano.
- **Persistencia solo en archivos** (Markdown/JSON). Sin BD externas.
- **Respeto de rutas**: no renombro ni muevo sin permiso cuando el impacto sea alto.

## Estructura del vault (convención)

- **Operativa del agente** → Skills instaladas en `.codex/skills/` o `.claude/skills/`
  - Cada skill vive en `skills/<nombre>/SKILL.md`
- **Plantillas del usuario** → `_templates/` → **no crear/editar/mover/eliminar sin permiso explícito**
- **Registro/memoria del agente** → `context/` (o la ruta que defina el usuario)
  - `cache/lecturas.json` → huellas de lectura (si está habilitado en tu setup)

## Política de citación interna (cuando aplique)

- Formato: `[[ruta/nota|Alias]]`
- Precisión: bloque `#^ancla` > sección `#Sección` > nota.
- Alias sugerido: `Basename · Sección` o `Basename · ^ancla`.

## Skills (catálogo canónico de este repo)

Activa la Skill adecuada cuando el trabajo encaje con su descripción:

- `obsidian-vault-ops` — búsqueda/lectura/escritura segura en vault
- `obsidian-reading-guardrails` — lectura real, límites y citas verificables
- `obsidian-rag-ops` — responder/resumir/crear con fuentes internas
- `obsidian-safe-changes` — mover/renombrar/eliminar con reversibilidad
- `obsidian-analysis-pipeline` — embeddings, conceptos, grafo y búsqueda semántica
- `obsidian-style-profile` — perfil de estilo de escritura
- `obsidian-daily-ai-summaries` — resúmenes IA de notas diarias
- `obsidian-recurring-expenses` — auditoría de gastos recurrentes (genérico)
- `obsidian-session-close` — cierre de sesión con pendientes
- `obsidian-facet-selection` — selección de facetas
- `obsidian-links` — creación y verificación de wikilinks
- `obsidian-frontmatter` — YAML frontmatter consistente y seguro
- `obsidian-markdown-structure` — estructura y limpieza Markdown sin romper Obsidian/Dataview
- `obsidian-mermaid` — diagramas Mermaid compatibles con Obsidian
- `obsidian-canvas` — edición de Canvas JSON sin corromperlo
- `obsidian-task-ops` — tareas en Markdown (inbox, backlog, daily/weekly)
- `obsidian-sop-authoring` — creación/actualización de procedimientos como skills

## Regla práctica

- Si la tarea tiene un “cómo hacerlo” repetible: **usa Skills**.
- Si la tarea es una decisión contextual puntual: usa este bootstrap + lectura real.
