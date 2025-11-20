from .base import BaseAgent, AgentResult


class ResponderAgent(BaseAgent):
def __init__(self, name: str, llm_adapter, ticket_store):
super().__init__(name)
self.llm = llm_adapter
self.store = ticket_store


async def run(self, ctx):
# If LLM suggested a reply, use it; otherwise compose a short reply for low priority
classifier = ctx.get('classifier', {})
suggested = classifier.get('suggested_reply') or ctx.get('suggested_reply')
ticket_id = ctx.get('ticket_id')


if suggested:
reply = suggested
else:
intent = classifier.get('intent', 'general')
if intent in ('howto', 'billing'):
reply = 'Thanks — we are looking into this and will update you within 24 hours.'
else:
reply = 'Thanks for contacting support. We received your request and will follow up shortly.'


# persist action to ticket store
if ticket_id:
self.store.append_action(ticket_id, {'action': 'auto_reply', 'text': reply})
return AgentResult(True, data={'reply': reply})
