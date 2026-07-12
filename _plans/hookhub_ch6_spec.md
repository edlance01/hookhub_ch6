# Plan: Write the HookHub Specification

## Context
The user wants a **specification document** (not an implementation yet) for a web application called HookHub: a gallery site that displays available Claude Code hooks as cards, links each card to its GitHub repository, and supports filtering by hook event type. The project directory (`hookhub_ch6`) is currently an empty `uv`-managed Python 3.13 scaffold (`main.py` prints "Hello", `pyproject.toml` has no dependencies) with an empty `_plans/` folder clearly intended to hold planning docs like this one. No code will be written in this pass — only the spec document.

User decisions from clarification:
- **Data source**: static curated dataset (JSON file bundled with the app), no live GitHub API calls.
- **Tech stack**: Python backend (FastAPI + Jinja2 server-rendered HTML), matching the existing `uv`/Python 3.13 scaffold — no separate JS framework/build step.
- **Output**: a full technical spec saved to `_plans/hookhub-spec.md`, covering goals, data model, routes, UI/component breakdown, filtering behavior, and a build checklist.

## Deliverable
Create `_plans/hookhub-spec.md` containing:

1. **Overview & Goals** — what HookHub is, who it's for, MVP scope vs. non-goals (no auth, no hook submission form, no live GitHub API, no pagination/search in v1).
2. **Tech Stack** — FastAPI + Uvicorn + Jinja2 templates + vanilla CSS/JS, dependency-managed via `uv` (extends existing `pyproject.toml`). No frontend build tooling.
3. **Project Structure** — proposed file layout:
   ```
   hookhub_ch6/
     main.py                # uvicorn entrypoint
     app/
       __init__.py
       server.py            # FastAPI app + routes
       data.py              # loads/validates hooks.json into Pydantic models
     data/
       hooks.json           # curated static dataset (seed data)
     templates/
       index.html           # Jinja2 page: filter bar + card grid
     static/
       style.css
       app.js                # client-side filter logic (no reload)
   ```
4. **Data Model** — `Hook` entity fields: `id` (slug), `name`, `description`, `event_type` (enum of Claude Code hook events: PreToolUse, PostToolUse, Notification, UserPromptSubmit, Stop, SubagentStop, PreCompact, SessionStart, SessionEnd), `repo_url` (GitHub URL), `author` (optional), `language` (optional tag, e.g. Python/Bash/TypeScript). Defined as a Pydantic model; `hooks.json` validated against it at startup.
5. **Seed Dataset** — spec includes a sample table of ~6-8 example hook entries spanning multiple event types, to be used as the initial `hooks.json` content.
6. **Routes** — `GET /` renders `index.html` server-side with all hooks embedded as `data-event-type` attributes on each card; no separate JSON API needed for v1 (keeps it simple — filtering is client-side over the already-rendered DOM). Static assets served from `/static`.
7. **UI / Component Breakdown**:
   - Header with app title/tagline.
   - Filter bar: "All" + one button/pill per distinct event type present in the dataset.
   - Responsive card grid (CSS grid/flexbox): each card shows hook name, description, an event-type badge, and a "View on GitHub ↗" link (`target="_blank" rel="noopener"`).
   - Empty state message when a filter matches zero cards.
8. **Filtering Behavior** — vanilla JS (`app.js`) toggles a `.hidden` class on cards based on the active filter button and each card's `data-event-type`; default filter is "All"; state does not persist across reload (out of scope for v1).
9. **Non-functional requirements** — accessibility (semantic HTML, focusable filter buttons, sufficient contrast), responsiveness (mobile-friendly grid), no external JS framework dependency.
10. **Build Checklist** — ordered list of implementation steps for a future session (add deps via `uv add fastapi uvicorn jinja2`, create data file, implement `data.py` loader, implement `server.py` route, build template, build CSS/JS, manual verification steps: run `uv run uvicorn app.server:app --reload`, load `localhost:8000`, confirm cards render, confirm filters toggle correctly, confirm GitHub links open the right repos).
11. **Future Enhancements (explicitly out of scope for v1)** — live GitHub API sync for stars/metadata, text search, a hook-submission form, pagination.

## Verification
This pass produces a document only. Verification = read back `_plans/hookhub-spec.md` to confirm it's internally consistent (data model fields match the seed table match the UI description) and scannable. Actual functional verification (running the app) applies to a later implementation pass, not this spec-writing pass.
