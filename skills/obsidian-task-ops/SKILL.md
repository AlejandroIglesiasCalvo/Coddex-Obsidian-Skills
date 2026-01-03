---
name: obsidian-task-ops
description: Gestionar tareas en notas Markdown de Obsidian (captura, inbox, priorización, daily/weekly). Respeta el formato existente de tasks.
---

# Obsidian Task Ops

## Cuándo usar
- Capturar tareas (inbox)
- Consolidar tareas desde varias notas
- Crear vistas daily/weekly (sin plugins específicos, salvo que existan en el vault)

## Reglas
- Respeta el formato ya usado en el vault:
  - `- [ ] tarea`
  - si hay fechas/IDs/etiquetas, no inventes nuevas convenciones
- Evita duplicados: si una tarea ya existe, enlaza o mueve, no copies sin control.

## Procedimiento
1. Localiza la(s) nota(s) de tareas (por ejemplo `tasks/` o notas diarias definidas por el usuario).
2. Lee y determina:
   - backlog
   - próximas (próximos 7 días)
   - bloqueadas
3. Aplica cambios:
   - mover a sección correcta
   - añadir contexto mínimo (link a nota origen)
4. Cierra con un resumen de acciones.

## Entrega
- Lista de tareas resultante + enlaces a sus notas origen.
