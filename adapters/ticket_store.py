from typing import Dict, List


class InMemoryTicketStore:
def __init__(self):
self.tickets: Dict[str, Dict] = {}
self.actions: Dict[str, List[Dict]] = {}


def create_ticket(self, ticket_id: str, text: str, meta: Dict = None):
self.tickets[ticket_id] = {'id': ticket_id, 'text': text, 'meta': meta or {}}
self.actions[ticket_id] = []


def append_action(self, ticket_id: str, action: Dict):
if ticket_id not in self.actions:
self.actions[ticket_id] = []
self.actions[ticket_id].append(action)


def get_ticket(self, ticket_id: str):
return self.tickets.get(ticket_id)


def get_actions(self, ticket_id: str):
return self.actions.get(ticket_id, [])
