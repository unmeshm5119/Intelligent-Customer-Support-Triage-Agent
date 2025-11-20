import asyncio
from .base import BaseAgent, AgentResult


class ClassifierAgent(BaseAgent):
def __init__(self, name: str, llm_adapter):
super().__init__(name)
self.llm = llm_adapter


async def run(self, ctx):
text = ctx.get('ticket_text', '')
if not text:
return AgentResult(False, error='no ticket_text in ctx')
prompt = f"Classify this support ticket and return lines like KEY:VALUE.\nTICKET:\n{text}\n\nRespond concisely."
resp = await self.llm.generate(prompt)
out = self.parse(resp)
return AgentResult(True, data=out)


def parse(self, text: str):
data = {}
for line in text.splitlines():
if ':' in line:
k, v = line.split(':', 1)
data[k.strip().lower()] = v.strip()
return data
