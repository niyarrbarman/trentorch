def detect_hallucination(claim_sentences: list[str], context_sentences: list[str]) -> list[bool]:
    """
    claim_sentences: individual sentences the model's answer asserted.
    context_sentences: the retrieved context the answer was supposed
    to be grounded in.

    A claim is flagged as hallucinated (True) iff it does NOT appear
    verbatim (as an exact substring) within ANY context sentence.
    A claim appearing verbatim in at least one context sentence is
    considered grounded (False).

    Returns one bool per claim, in the same order as claim_sentences.
    """
    # TODO: Implement the naive containment check from Theory.
    claims = []
    for cls in claim_sentences:
        flag = 0
        for ctx in context_sentences:
            if cls in ctx:
                flag = 1
        claims.append(not flag)
    return claims
