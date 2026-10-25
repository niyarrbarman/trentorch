# Detect Hallucination Against Retrieved Context

Intermediate | agentic-systems | guardrails | evaluation

### The problem, from first principles

A RAG answer is supposed to be grounded in the context it retrieved — every factual claim it makes should trace back to something the context actually said. The cheapest possible check for this doesn't need a model call at all: split the answer into individual claims, and check whether each one appears, verbatim, somewhere in the retrieved context. A claim that doesn't is flagged as unsupported — a naive but genuinely useful first-pass faithfulness check, the same kind of exact-match philosophy behind _Track Citations So Every Claim Maps to a Source_.

### From theory to code

You're given `claim_sentences` (individual sentences the answer asserted) and `context_sentences` (the retrieved context). Implement `detect_hallucination(claim_sentences, context_sentences)`. A claim is flagged as hallucinated (`True`) iff it does **not** appear verbatim (as an exact substring) within **any** context sentence. A claim appearing verbatim in at least one context sentence is grounded (`False`).

Return one bool per claim, in the same order as `claim_sentences`.

### Constraints

- 1 to 200 claims; 0 to 200 context sentences; matching is exact-substring, case-sensitive.

### Hints

<details>
<summary>Hint 1</summary>

For each claim, `any(claim in context for context in context_sentences)` checks all context sentences in one line — a claim is grounded iff that check is true for at least one of them.

</details>

<details>
<summary>Hint 2</summary>

A claim doesn't need to match a context sentence _exactly_ — it just needs to appear somewhere _inside_ it. `claim in context` (substring containment), not `claim == context` (exact equality), is the right check.

</details>
