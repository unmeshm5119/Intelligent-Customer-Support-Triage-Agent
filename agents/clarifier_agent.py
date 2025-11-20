from .base import BaseAgent, AgentResult


class ClarifierAgent(BaseAgent):
def __init__(self, name: str, llm_adapter):
super().__init__(name)
self.llm = llm_adapter


async def run(self, ctx):
# If classifier returned a CLARIFY field, ask clarifying question
clarify = ctx.get('clarify') or ctx.get('clarify:')
if not clarify:
# also check classifier outputs
classifier = ctx.get('classifier', {})
if 'clarify' in classifier:
clarify = classifier.get('clarify')
if not clarify:
return AgentResult(True, data={})
# produce a user-facing question
# here we simply forward the text; real agent may personalize
return AgentResult(True, data={'clarifying_question': clarify})
