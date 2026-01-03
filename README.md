# Obsidian Agent Skills (pack)

Este repositorio contiene Skills orientadas a operar un vault de Obsidian con agentes compatibles con el estándar `SKILL.md`.

## Instalación

### Codex
Copia las carpetas de `skills/` a:

- `<vault>/.codex/skills/`

(Alternativamente, puedes mantener este repo fuera del vault y copiar/sincronizar en tu flujo de bootstrap).

## Contenido
- `AGENTS.md`: bootstrap mínimo (recomendado mantenerlo ligero)
- `skills/*/SKILL.md`: skills modulares

## Skills incluidos
- `obsidian-analysis-pipeline`: Orquesta análisis semántico del vault (conceptos, grafo, embeddings y búsqueda) con procesamiento por lotes y manejo de errores.
- `obsidian-canvas`: Editar o generar archivos de Obsidian Canvas (.canvas JSON) de forma segura: nodos, conexiones, posiciones.
- `obsidian-daily-ai-summaries`: Genera o actualiza "Resumen IA" en notas diarias con lectura completa y citas internas.
- `obsidian-facet-selection`: Selecciona una faceta de trabajo según la petición y registra la decisión con fuentes.
- `obsidian-frontmatter`: Aplicar reglas consistentes de YAML frontmatter en Obsidian.
- `obsidian-links`: Crear, validar y reparar wikilinks de Obsidian (links internos, secciones y anclas).
- `obsidian-markdown-structure`: Estandarizar estructura Markdown en Obsidian sin romper Dataview/Templater ni tablas.
- `obsidian-mermaid`: Crear diagramas Mermaid compatibles con Obsidian y evitar errores comunes.
- `obsidian-rag-ops`: Ejecuta flujos RAG para responder, resumir, reorganizar o crear notas con citas trazables.
- `obsidian-reading-guardrails`: Garantiza lectura real, control de límites y validación de citas/wikilinks.
- `obsidian-recurring-expenses`: Identifica y registra gastos recurrentes desde correos y adjuntos con validación estricta y trazabilidad.
- `obsidian-safe-changes`: Cambios seguros en archivos del vault con trazabilidad y recuperación.
- `obsidian-session-close`: Cierra una sesión dejando resumen, pendientes y mejoras con trazabilidad.
- `obsidian-sop-authoring`: Crear y mantener procedimientos como skills (SKILL.md) con objetivo, cuándo usar, pasos y checklist.
- `obsidian-style-profile`: Analiza el estilo de escritura del usuario y genera un perfil con métricas y ejemplos citados.
- `obsidian-task-ops`: Gestionar tareas en notas Markdown de Obsidian (captura, inbox, priorización, daily/weekly).
- `obsidian-vault-ops`: Operaciones seguras sobre un vault de Obsidian: buscar, leer, escribir, mover y validar sin romper enlaces.
- `obsidian-dispatch`: Skill router para Codex CLI que ofrece un acceso rápido con `$obsidian-dispatch: <instrucción>` y permite redirigir peticiones comunes.
