import json
from enum import Enum
from pathlib import Path

from pydantic import BaseModel, TypeAdapter

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "hooks.json"


class EventType(str, Enum):
    PRE_TOOL_USE = "PreToolUse"
    POST_TOOL_USE = "PostToolUse"
    NOTIFICATION = "Notification"
    USER_PROMPT_SUBMIT = "UserPromptSubmit"
    STOP = "Stop"
    SUBAGENT_STOP = "SubagentStop"
    PRE_COMPACT = "PreCompact"
    SESSION_START = "SessionStart"
    SESSION_END = "SessionEnd"


class Hook(BaseModel):
    id: str
    name: str
    description: str
    event_type: EventType
    repo_url: str
    author: str | None = None
    language: str | None = None


_hooks_adapter = TypeAdapter(list[Hook])


def load_hooks() -> list[Hook]:
    raw = DATA_FILE.read_text()
    return _hooks_adapter.validate_json(raw)
