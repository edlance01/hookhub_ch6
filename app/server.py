from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.data import load_hooks

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(title="HookHub")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

EVENT_TYPE_COLORS: dict[str, str] = {
    "PreToolUse": "#5b4fe0",
    "PostToolUse": "#2f9e6e",
    "Notification": "#e0a640",
    "UserPromptSubmit": "#3f8fe0",
    "Stop": "#e05f5f",
    "SubagentStop": "#c05fe0",
    "PreCompact": "#5fa8a3",
    "SessionStart": "#5fbf6e",
    "SessionEnd": "#8a8a9e",
}


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    hooks = load_hooks()
    event_types = sorted({hook.event_type.value for hook in hooks})
    return templates.TemplateResponse(
        request,
        "index.html",
        {"hooks": hooks, "event_types": event_types, "event_colors": EVENT_TYPE_COLORS},
    )
