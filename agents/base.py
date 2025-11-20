from abc import ABC, abstractmethod
from typing import Any, Dict


class AgentResult:
def __init__(self, success: bool, data: Dict[str, Any] = None, error: str | None = None):
self.success = success
self.data = data or {}
self.error = error


class BaseAgent(ABC):
def __init__(self, name: str):
self.name = name


@abstractmethod
async def run(self, ctx: Dict[str, Any]) -> AgentResult:
pass


def __repr__(self):
return f"<Agent {self.name}>"
