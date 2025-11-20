import time
from typing import Dict


class InMemorySessionService:
def __init__(self):
self.sessions: Dict[str, Dict] = {}


def create(self, session_id: str, data: Dict = None):
self.sessions[session_id] = {'created_at': time.time(), 'data': data or {}}
return self.sessions[session_id]


def get(self, session_id: str):
return self.sessions.get(session_id)


def update(self, session_id: str, patch: Dict):
if session_id not in self.sessions:
raise KeyError('session not found')
self.sessions[session_id]['data'].update(patch)
return self.sessions[session_id]
