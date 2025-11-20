import asyncio
from adapters.llm_adapter import MockLLMAdapter
from adapters.ticket_store import InMemoryTicketStore
from runtime.logger import SimpleLogger
from orchestrator import TriageOrchestrator


async def demo():
llm = MockLLMAdapter()
store = InMemoryTicketStore()
logger = SimpleLogger()
orch = TriageOrchestrator(llm, store, logger)


# create demo tickets
store.create_ticket('T-100', 'I cannot login to my account, it says invalid credentials')
store.create_ticket('T-101', 'How do I update my billing address?')
store.create_ticket('T-102', 'Hi')


# process tickets
for tid in ['T-100', 'T-101', 'T-102']:
ticket = store.get_ticket(tid)
print('\n--- Processing', tid)
res = await orch.run_ticket(tid, ticket['text'])
print('Result:', getattr(res, 'data', None))
print('Actions:', store.get_actions(tid))


if __name__ == '__main__':
asyncio.run(demo())
