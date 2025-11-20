import asyncio
from agents.classifier_agent import ClassifierAgent
from agents.clarifier_agent import ClarifierAgent
from agents.responder_agent import ResponderAgent


class TriageOrchestrator:
def __init__(self, llm_adapter, ticket_store, logger):
self.llm = llm_adapter
self.store = ticket_store
self.logger = logger
# instantiate agents
self.classifier = ClassifierAgent('classifier', self.llm)
self.clarifier = ClarifierAgent('clarifier', self.llm)
self.responder = ResponderAgent('responder', self.llm, self.store)


async def run_ticket(self, ticket_id: str, ticket_text: str):
ctx = {'ticket_id': ticket_id, 'ticket_text': ticket_text}
self.logger.info('start_ticket', ticket_id=ticket_id)


# 1) classify
r1 = await self.classifier.run(ctx)
if not r1.success:
self.logger.error('classification_failed', ticket_id=ticket_id, error=r1.error)
return r1
ctx['classifier'] = r1.data


# 2) if clarifying question is required
clarify = r1.data.get('clarify') or r1.data.get('clarify:')
if clarify:
r2 = await self.clarifier.run({**ctx, **{'clarify': clarify}})
ctx.update(r2.data)
# store clarifying question as action
self.store.append_action(ticket_id, {'action': 'clarify', 'question': r2.data.get('clarifying_question')})
self.logger.info('clarify_sent', ticket_id=ticket_id)
return r2


# 3) respond (auto-reply) for simple cases
r3 = await self.responder.run(ctx)
ctx.update(r3.data)
self.store.append_action(ticket_id, {'action': 'triaged', 'classifier': r1.data, 'reply': r3.data.get('reply')})
self.logger.info('triaged', ticket_id=ticket_id, route=r1.data.get('route'))
return r3
