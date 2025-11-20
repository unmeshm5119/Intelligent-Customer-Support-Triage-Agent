import asyncio
from typing import Dict


class MockLLMAdapter:
"""A tiny synchronous simulator of an LLM for local testing.
Replace with (async) OpenAI/Anthropic adapter in production.
"""
async def generate(self, prompt: str, *, max_tokens: int = 256) -> str:
await asyncio.sleep(0.05)
# Very simple heuristics to simulate LLM outputs.
p = prompt.lower()
if 'billing' in p or 'invoice' in p:
return 'INTENT:billing\nPRIORITY:medium\nROUTE:finance'
if 'password' in p or 'login' in p or 'cannot access' in p:
return 'INTENT:auth_issue\nPRIORITY:high\nROUTE:it_support'
if 'how do i' in p or 'how to' in p:
return 'INTENT:howto\nPRIORITY:low\nROUTE:help_center\nSUGGESTED_REPLY:See our help doc at https://kb.example.com/article-123'
# Otherwise ask for clarification sometimes
if len(p.split()) < 6:
return 'CLARIFY:Can you provide the account id and the exact steps to reproduce?'
# fallback
return 'INTENT:general_inquiry\nPRIORITY:low\nROUTE:general_support'
