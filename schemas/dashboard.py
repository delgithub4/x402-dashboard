from typing import Any

from pydantic import BaseModel


class DashboardRequest(BaseModel):
    filters: dict[str, Any] = {}


class DashboardResponse(BaseModel):
    success: bool
    message: str
    data: Any | None = None
